import email
from django.db import models

class Crud(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name
