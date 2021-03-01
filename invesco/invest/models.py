from django.db import models
from djmoney.models.fields import MoneyField

STATUS = [
    ('Single', 'SINGLE'),
    ('Married', 'MARRIED'),
    ('Divorced', 'DIVORCED')
]

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    marriage_status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)
    children = models.IntegerField(default=0, null=True, blank=True)
    annual_income = MoneyField(max_digits = 15,decimal_places=2,null=True,default_currency="INR")
    annual_expenses = MoneyField(max_digits = 15,decimal_places=2,null=True,default_currency="INR")
