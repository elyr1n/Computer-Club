from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "id",
        "get_avatar",
        "username",
        "is_staff",
        "is_vip",
        "is_active",
        "date_joined",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_vip",
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Персональная информация",
            {"fields": ("avatar", "get_avatar_preview", "is_vip")},
        ),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Даты", {"fields": ("date_joined", "last_login")}),
    )

    readonly_fields = ("get_avatar_preview", "date_joined", "last_login")

    @admin.display(description="Аватар")
    def get_avatar(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src="{obj.avatar.url}" width="35" height="35" style="border-radius: 5px; object-fit: cover;">'
            )
        return "—"

    @admin.display(description="Текущий аватар")
    def get_avatar_preview(self, obj):
        if obj.avatar:
            return mark_safe(
                f'<img src="{obj.avatar.url}" width="150" style="border-radius: 10px; border: 2px solid #9333ea;">'
            )
        return "Аватар не установлен"
