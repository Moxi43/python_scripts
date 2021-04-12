from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from time import strftime


class UserManager(BaseUserManager):
    def create_user(self, username, password=''):
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, username, password=None):
        user = self.create_user(
            username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    # auth vars
    username = models.CharField("Username", max_length=42, unique=True)
    password = models.CharField("Password", max_length=50)
    last_login = models.DateTimeField(default=strftime("%Y-%m-%d %H:%M:%S.%u"))
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField("first_name", default="man", max_length=10)
    last_name = models.CharField(default="man", max_length=10)
    email = models.EmailField(default="some@gmail.com")
    date_joined = models.DateTimeField(default=strftime("%Y-%m-%d %H:%M:%S.%u"))
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()
    # parameters
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password1", "password2"]

    # functions
    def __str__(self):
        return self.username, self.header_text

    @property
    def is_staff(self):
        return self.is_admin
