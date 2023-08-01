import json
import jwt
import requests

from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from account.serializers import UserSerializer
from rest_framework import viewsets
from config.settings import SECRET_KEY
from .models import UserModel
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UserListView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class KakaoSignCallbackView(APIView):
    # JWT 토큰을 생성하는 함수
    @staticmethod
    def _create_jwt(user_id):
        return jwt.encode({"id": user_id}, SECRET_KEY, algorithm="HS256")

    # 카카오 회원 정보를 받아와서 새로운 User 인스턴스를 생성하는 함수
    @staticmethod
    def _create_kakao_user(kakao_response):
        return User(
            id=kakao_response["id"],
            name=kakao_response["kakao_account"]["profile"]["nickname"],
            profile=kakao_response["kakao_account"]["profile"]["profile_image_url"],
        )

    # 카카오 액세스 토큰을 통해 사용자 정보를 반환하는 함수
    @staticmethod
    def _get_kakao_user_info(access_token):
        url = "https://kapi.kakao.com/v2/user/me"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        }
        response = requests.post(url, headers=headers)
        return json.loads(response.text)

    # 카카오 로그인의 콜백을 처리하는 post 메소드
    @method_decorator(csrf_exempt, name="dispatch")
    def post(self, request):
        # 요청에서 액세스 토큰을 가져옵니다.
        kakao_access_code = request.data.get("accessToken")

        # 액세스 토큰이 제공되지 않았을 경우 에러 메시지와 함께 400 상태 코드를 반환합니다.
        if not kakao_access_code:
            return JsonResponse({"error": "access_token not provided"}, status=400)

        # 액세스 토큰을 사용하여 카카오 회원 정보를 얻습니다.
        kakao_response = self._get_kakao_user_info(kakao_access_code)

        try:
            # 기존 디비에 있는 사용자 정보를 찾습니다.
            user_info = UserModel.objects.get(id=kakao_response["id"])
            # 기존 사용자의 경우, JWT 토큰을 생성하고 응답에 포함합니다.
            token = self._create_jwt(user_info.id)
            return JsonResponse({"id": user_info.id, "token": token, "exist": True})

        except UserModel.DoesNotExist:
            # 사용자 정보를 찾을 수 없는 경우 새 사용자를 생성합니다.
            kakao_user = self._create_kakao_user(kakao_response)
            kakao_user.save()
            # 새 사용자의 경우, JWT 토큰을 생성하고 응답에 포함합니다.
            token = self._create_jwt(kakao_user.id)
            return JsonResponse(
                {"id": kakao_user.id, "token": token, "exist": False}, status=201
            )
