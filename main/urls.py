from django.urls import path

from main.views import index, aboutus, contact

urlpatterns = [
    path("", index, name="index"),
    path("درباره-ما", aboutus, name="aboutus"),
    path("ارتباط-با-ما", contact, name="contact"),
]