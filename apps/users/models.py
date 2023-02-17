from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, phone_number: str, email: str):
        if not phone_number:
            raise ValueError(_('Users must have a phone number'))

        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
        )

        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number: str, email: str):
        user = self.create_user(
            email=email,
            phone_number=phone_number,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        '전화번호',
        max_length=20,
        unique=True,
    )
    email = models.EmailField(
        '이메일',
        max_length=255,
        unique=True,
    )
    created_at = models.DateTimeField(
        '생성일시',
        auto_now_add=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    @property
    def is_staff(self):
        return self.is_superuser
