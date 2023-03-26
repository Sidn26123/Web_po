from django.db import models

from django.contrib.auth.models import AbstractUser

from datetime import datetime

from django.utils import timezone

# from django.contrib.auth.backends import ModelBackend
# Create your models here.
class User(AbstractUser):
	MAN = "MN"
	WOMAN = "WM"
	THEM = "TH"
	GENDER_CHOICES = [
		(MAN, "Men"),
		(WOMAN, "Phu nu"),
		(THEM, "Khong xac dinh"),
	]
	gender_choice = models.CharField(
			max_length = 2,
			choices = GENDER_CHOICES,
			default = THEM,
		)
	phone = models.CharField(max_length = 15, default = None, null = True, blank = True)
	citizen_identification = models.CharField(max_length = 20, unique = False, null = True)
	address = models.CharField(max_length = 255, null = True, blank = True)
	avatar = models.FileField(upload_to = 'media', storage = None, max_length = 100, default = None, null = True, blank = True)
	time_join = models.DateTimeField(auto_now_add = True)
	is_admin = models.BooleanField(default = False)


