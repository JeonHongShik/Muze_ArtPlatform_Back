import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

from config.settings import SECRET_KEY
from .models import User
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests
import jwt

# Create your views here.
# @csrf_exempt
# def home(request):
#     user_id = request.session.get("user")

#     if user_id:
#         user = User.objects.get(pk=user_id)
#         return JsonResponse({"user_email": user.email})

#     return JsonResponse({"status": "Home"})


# @csrf_exempt
# def register(request):
#     if request.method == "GET":
#         return JsonResponse({"status": "GET method is unsupported for register."})
#     elif request.method == "POST":
#         email = request.POST.get("email", None)
#         name = request.POST.get("name", None)
#         password = request.POST.get("password", None)
#         repassword = request.POST.get("repassword", None)

#         res_data = {}
#         if not (email and name and password and repassword):
#             res_data["error"] = "모든 값을 입력해야 합니다."
#         elif password != repassword:
#             res_data["error"] = "비밀번호가 다릅니다."
#         else:
#             user = User(email=email, name=name, password=make_password(password))
#             user.save()
#             res_data["status"] = "success"

#         return JsonResponse(res_data)


# @csrf_exempt
# def login(request):
#     if request.method == "GET":
#         return JsonResponse({"status": "GET method is unsupported for login."})
#     elif request.method == "POST":
#         useremail = request.POST.get("useremail", None)
#         password = request.POST.get("password", None)

#         res_data = {}
#         try:
#             User = User.objects.get(useremail=useremail)
#             if check_password(password, User.password):
#                 # 비밀번호가 일치하면 세션 생성
#                 request.session["user"] = User.id
#                 res_data["status"] = "1"
#             else:
#                 res_data["status"] = "0"
#             return JsonResponse(res_data)
#         except User.DoesNotExist:
#             # 대문자 User 임에 주의
#             res_data["status"] = "0"

#         return JsonResponse(res_data)


# @csrf_exempt
# def logout(request):
#     if request.session.get("user"):
#         del request.session["user"]

#     return JsonResponse({"status": "redirect", "url": "/account/login/"})


@method_decorator(csrf_exempt, name="dispatch")
class KakaoSignCallbackView(View):  # 카카오톡 소셜 로그인을 위한 클래스
    # 카카오의 사용자 토크을 이용해 카카오에 사용자 정보를 요청함
    def get(self, request):
        kakao_access_code = request.GET.get("access_token", None)
        print(kakao_access_code)
        url = "https://kapi.kakao.com/v2/user/me"
        headers = {
            "Authorization": f"Bearer {kakao_access_code}",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        }
        kakao_response = requests.post(url, headers=headers)
        kakao_response = json.loads(kakao_response.text)  # 유저의 정보를 json으로 변환

        # 관리자가(employee) 기존에 카카오톡 계정이 DB에 저장되어 있는지 확인
        if User.objects.filter(id=kakao_response.get("id")).exists():
            user_info = User.objects.get(
                id=kakao_response.get("id")
            )  # 지금 접속한 카카오 아이디가 데이터베이스에 존재하는지 확인

            encoded_jwt = jwt.encode(  # 존재하는 카카오 아이디를 가진 유저 객체를 가져옴
                {"id": user_info.id}, SECRET_KEY, algorithm="HS256"
            )
            return JsonResponse(  # jwt토큰 발행
                {"id": user_info.id, "token": encoded_jwt, "exist": True}
            )

        else:
            User(  # 닉네임 카카오계정 프로필사진
                id=kakao_response["id"],
                email=kakao_response["email"],
                name=kakao_response["name"],
                # profile=kakao_response["profile"],
            ).save()
            user_info = User.objects.get(id=kakao_response["id"])
            encoded_jwt = jwt.encode(
                {
                    "id": user_info.id,
                },
                SECRET_KEY,
                algorithm="HS256",
            )  # JWT 토큰 발행
            return JsonResponse(
                print(kakao_response),
                {"id": user_info.id, "token": encoded_jwt, "exist": False},
            )
