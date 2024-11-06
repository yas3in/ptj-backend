from django.db import models
from main.models import User
import datetime
import jdatetime


class Blog(models.Model):
    date = jdatetime.datetime.now()
    date_str = date.strftime("%Y/%m/%d")
    now = datetime.datetime.now()
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField (max_length=48)
    content = models.TextField()
    date = models.DateField(auto_now=date_str)
    
    def __str__(self):
        return f"{self.title}"