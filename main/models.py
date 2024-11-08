from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=60, blank=False, null=False)
    password = models.CharField(max_length=48, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.full_name}"