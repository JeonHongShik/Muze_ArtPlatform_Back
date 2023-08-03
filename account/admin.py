from django.contrib import admin
from .models import UserModel


class UserAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ("id", "name", "Type")

연창현

admin.site.register(UserModel, UserAdmin)
