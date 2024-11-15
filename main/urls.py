from django.urls import path

from main.views import index, aboutus, contact, service, authentication

urlpatterns = [
    path("", index, name="index"),
    path("درباره-ما", aboutus, name="aboutus"),
    path("ارتباط-با-ما", contact, name="contact"),
    path("خدمات-ما", service, name="404"),
    path("authentication/", authentication, name="authentication"),
]