from django.contrib import admin
from django.contrib.admin import register
from blog.models import Blog

@register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("auther", "title", "content", "date")
    list_filter = ("auther", )
