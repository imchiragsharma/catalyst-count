from django.db import models

class Company(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255, default = 0)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linkedin_url = models.URLField(max_length=255, default = '')
    current_employees = models.IntegerField(default = 0)
    total_employees_estimate = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
