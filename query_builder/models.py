from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)  # Keep locality field if needed
    city = models.CharField(max_length=255, null=True, blank=True)  # New field for city
    state = models.CharField(max_length=255, null=True, blank=True)  # New field for state
    country = models.CharField(max_length=255)
    linkedin_url = models.CharField(max_length=255, null=True, blank=True)
    current_employees = models.IntegerField()
    total_employees_estimate = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.locality:
            locality_parts = self.locality.split(', ')
            if len(locality_parts) > 0:
                self.city = locality_parts[0]
            if len(locality_parts) > 1:
                self.state = locality_parts[1]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
