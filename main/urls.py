from django.urls import path

from main.views import index_page, aboutus

urlpatterns = [
    path("", index_page, name="index_page"),
    path("درباره-ما", aboutus, name="aboutus"),
]