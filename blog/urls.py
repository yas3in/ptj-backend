from django.urls import path

from blog.views import show_blog, blog_list


urlpatterns = [
    path("", blog_list),
    path("<int:pk>/", show_blog),
]
