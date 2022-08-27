from curses import meta
from msilib.schema import Class
from tkinter.tix import Meter
from django.db import models

class User(models.Model):
    _id = models.CharField(max_length=20, unique=True)  #유저 키
    id = models.CharField(max_lenth=20) #유저 아이디
    pw = models.CharField(max_length=30)  #유저 비밀번호
    email = models.EmailField(max_length=128)  #유저 이메일
    name = models.CharField(max_length=10)  #유저 이름
    user_birth = models.IntegerField(max_length=6)  #유저 생년월일
    user_nickname= models.CharField(max_length=10)  #유저 닉네임
    user_school = models.CharField(max_length=15)  #유저 소속대학명
    user_major = models.CharField(max_length=15)  #유저 소속전공
    user_favor = models.CharField(max_length=20)  #유저 흥미(관심)
    user_create_date = models.DateTimeField(auto_now_add=True)  #계정 생성시간
    user_last_date = models.DateTimeField #계정 탈퇴

    def __str__(self):
        return self._id