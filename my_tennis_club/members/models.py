from django.db import models

# Create your models here.
class Court(models.Model):
    name = models.CharField(max_length=255)
    form = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    date = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'