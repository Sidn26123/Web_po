from django.db import models

from users.models import User
# Create your models here.

class Patient(User):
	blood_group = models.CharField(max_length = 5, default = None)