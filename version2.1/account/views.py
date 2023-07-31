import json
import jwt
import requests

from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from account.serializers import UserSerializer

from config.settings import SECRET_KEY
from .models import UserModel
from rest_framework import status
from rest_framework import viewsets

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class KakaoSignCallbackView(APIView):
    # @staticmethod
    # def _create_jwt(user_id):
    #     return jwt.encode({"id": user_id}, SECRET_KEY, algorithm="HS256")

    @staticmethod
    def _create_kakao_user(kakao_response):
        return User(
            id=kakao_response["id"],
            name=kakao_response["kakao_account"]["profile"]["nickname"],
            profile=kakao_response["kakao_account"]["profile"]["profile_image_url"],
        )

    @staticmethod
    def _get_kakao_user_info(access_token):
        url = "https://kapi.kakao.com/v2/user/me"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        }
        response = requests.post(url, headers=headers)
        return json.loads(response.text)

    @method_decorator(csrf_exempt, name="dispatch")
    def post(self, request):
        kakao_access_code = request.data.get("accessToken")

        if not kakao_access_code:
            return JsonResponse({"error": "access_token not provided"}, status=400)

        kakao_response = self._get_kakao_user_info(kakao_access_code)
        print(kakao_access_code)

        try:
            user_info = UserModel.objects.get(id=kakao_response["id"])
            token = token = "임시폐쇄"
            return JsonResponse({"id": user_info.id, "token": token, "exist": True})
        except UserModel.DoesNotExist:
            kakao_user = self._create_kakao_user(kakao_response)
            kakao_user.save()
            token = "임시폐쇄"
            return JsonResponse({"id": kakao_user.id, "token": token, "exist": False}, status=201)
        
