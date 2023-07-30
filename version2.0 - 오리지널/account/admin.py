from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
class AccountAdmin(UserAdmin):
    # 관리자 화면 칼럼지정
    list_display = ("id", "name", "is_staff", "is_active")
    search_fields = (
        "id",
        "name",
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User)
