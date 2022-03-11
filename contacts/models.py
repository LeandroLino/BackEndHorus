from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15) ##unique=True)
    ddd = models.CharField(max_length=3)
    deleted = models.BooleanField(default=False)
