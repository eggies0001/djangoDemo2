from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=128)
    user_email = models.CharField(max_length=128)