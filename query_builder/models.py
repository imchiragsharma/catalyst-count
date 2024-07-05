# models.py
from django.db import models

class Company(models.Model):
    keyword = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    employees = models.IntegerField()

    def __str__(self):
        return self.keyword