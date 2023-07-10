
# Create your models here.
from django.db import models
import django.utils.timezone as timezone

# user model
class User(models.Model):

    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    createAt = models.DateTimeField(auto_now_add=True)
