from django.db import models
from main.models import User
import datetime


class Blog(models.Model):
    now = datetime.datetime.now()
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField (max_length=48)
    content = models.TextField()
    date = models.DateField(auto_now=now)
    
    def __str__(self):
        return f"{self.title}"