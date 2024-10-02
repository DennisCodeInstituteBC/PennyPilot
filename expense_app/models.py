from django.db import models
from django.contrib.auth import get_user_model # importing users from allauth
from django.contrib.auth.models import User 

User = get_user_model()

# Create your models here.

# Category Model.py linked with Users from allauth
class Category(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Expense Model.py linked with Users(allauth) and Catergory


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category} - {self.amount}'

