from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Ник-нейм должен быть заполнен!")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_vip", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперюзер должен иметь is_staff=True!")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперюзер должен иметь is_staff=True!")

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16, unique=True, verbose_name="Ник-нейм")
    avatar = models.ImageField(
        upload_to="avatars/", null=True, blank=True, verbose_name="Аватар"
    )
    is_vip = models.BooleanField(default=False, verbose_name="VIP Статус")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.username}"
