from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "username",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
        "last_login",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
    )

    fieldsets = (
        (
            None,
            {"fields": ("username",)},
        ),
        ("Персональная информация", {"fields": ("password",)}),
        ("Права доступа", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Даты", {"fields": ("date_joined", "last_login")}),
    )
