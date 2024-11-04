from django.contrib import admin
from blog.models import Blog

admin.site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("ahther", "title", "content")
