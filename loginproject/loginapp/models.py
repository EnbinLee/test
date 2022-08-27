from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class User(AbstractUser):
    _id = models.CharField(primary_key=True)
    name = models.CharField(max_length=10)
    id = models.CharField()
    pw = models.CharField()
    email = models.EmailField()
    user_nickname = models.CharField()
    user_school = models.CharField()
    user_major = models.CharField()
    user_favor = models.CharField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField()

    # USERNAME_FIELD: 'user_nickname'
    # REQUIRED_FIELDS: ['email']

    def __str__(self):
        return self.email

class Usermanager(BaseUserManager):
    def _create_user(self, email, id, pw = None):
        if not email :
            raise ValueError('The given email mist be set')
        email = self.normalize_email(email)
        name = self.model.normalize_name(name)
        user = self.model(email = email, name = name)
        user.set_password(pw)
        user.save(using = self._db)
        return user
    
    def create_user(self, email, id='', pw=None):
        return self._create_user(self, email, id, pw)

    def create_superuser(self, email, pw):
        return self._create_user(email, id, pw)