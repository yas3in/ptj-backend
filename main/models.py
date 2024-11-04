from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32, blank=False, null=False)
    password = models.CharField(max_length=48, blank=False, null=False)
    is_active = models.BooleanField(default=False)
    email = models.EmailField(blank=True, default=" ")
    
    def __str__(self):
        return f"{self.username}"