from django.db import models
from main.models import User 

class Blog(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField (max_length=48)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.title