from django.contrib import admin
from django.contrib.admin import register

from main.models import User

@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active')
    