from django.urls import path

from Resolve.views import home

urlpatterns = [
    path("",home.index, name ="home"),
]