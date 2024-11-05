from django.urls import path

from blog.views import show_blog, blog_list


urlpatterns = [
    path("", blog_list),
    path("<str:content>/", show_blog),
]
