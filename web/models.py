from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Expense(models.Model):
    text = models.CharField(max_length=255)
    data = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
    

class Income(models.Model):
    text = models.CharField(max_length=255)
    data = models.DateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{}, {}".format(self.data, self.amount)