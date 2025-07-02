from django.contrib.auth.models import (
    AbstractBaseUser, # 모델이 커스텀유저로 상속을 받게끔
    PermissionsMixin, # 일반유저와 슈퍼유저를 구분하기위해
    BaseUserManager
)
from django.db import models

class UserManager(BaseUserManager):
    # 일반 유저 생성 함수
    def create_user(self, email, password):
        if not email:
            raise ValueError("Please enter an eamil address")
        
        user = self.model(email=email)
        user.set_password(password)
        user.save()

        return user
    
    # 슈퍼 유저 생성
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user
    
# - email
# - password
# - nickname
# - is_business
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    is_business = models.BooleanField(default=False)

    # Permissions Mixin : 유저의 권한 관리
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self): # 클래스안의 함수이기에 self를 받는다
        return f'email: {self.email}, nickname: {self.nickname}'