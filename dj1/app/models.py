from django.db import models

# Create your models here.
class User(models.Model):
    account       = models.CharField(max_length = 20)
    password      = models.CharField(max_length = 20)
    led_statu     = models.BooleanField(default=False)
    curtain_statu = models.BooleanField(default=False)
