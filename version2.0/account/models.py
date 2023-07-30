from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    # 일반 user 생성 , Username이 userID
    def create_user(self, id, name, email, password=None):
        if not name:
            raise ValueError("You must have a Name")
        if not email:
            raise ValueError("You must have an email")
        if not id:
            raise ValueError("You must have an id")

        user = self.model(id=id, email=self.normalize_email(email), name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 User 생성
    def create_superuser(self, id, email, name, password):
        user = self.create_user(
            id=id,
            email=self.normalize_email(email),
            name=name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.CharField(unique=True, primary_key=True, max_length=20)

    email = models.EmailField(  # ID == EMAIL
        verbose_name="email", max_length=254, unique=True
    )
    name = models.CharField(
        verbose_name="name",
        max_length=100,
        null=False,
        blank=False,
        default="name",
    )
    # profile = models.ImageField(
    #     upload_to="media/profile",
    #     null=False,
    #     blank=False,
    #     default="",
    # )

    POST = "PT"
    CONSUMER = "CO"
    USE_APP = [
        (POST, "POST"),
        (CONSUMER, "CONSUMER"),
    ]

    Type = models.CharField(max_length=2, choices=USE_APP, default=POST)  # 사용자 종류

    create_at = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    object = UserManager()  # 헬퍼클라스 사용

    USERNAME_FIELD = "email"  # 로그인ID 로 사용할 필드
    REQUIRED_FIELDS = ["name", "id", "email"]  # 필수로 작성 필드

    def __str__(self):
        return f"{self.id}({self.name})"

    def has_perm(self, perm, obj=None):  # 권한 확인
        return self.is_admin

    def has_module_perms(self, app_label):  # 특정 어플리케이션에 대한 권한 확인
        return True
