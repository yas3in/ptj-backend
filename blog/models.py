from django.db import models
from main.models import User
import jdatetime
from django_jalali.db import models as jmodels

class Blog(models.Model):
    date = jdatetime.datetime.now()
    date_str = date.strftime("%Y/%m/%d")
    
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField (max_length=48)
    content = models.TextField()
    date = jmodels.jDateField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"