from django.db import models
from django.contrib.auth.backends import ModelBackend
from users.models import User
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Site_admin(User):

    #Save obj với args đưa vào
    def save(self, *args, **kwargs):
    #super để kế thừa save lại các phần đã có trước đó
        super().save(*args, **kwargs)

#Set value mặc định cho trường inherited
# class Site_admin_web(Site_admin):
#     ad = models.ForeignKey(Site_admin, on_delete=models.CASCADE)
#     is_admin = models.BooleanField(default = True)

#     def __str__(self):
#         return self.is_admin