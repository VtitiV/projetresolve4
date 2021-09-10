from django.urls import path

from .views import home, personne

urlpatterns = [
    path("", home.index, name="home"),
    # Personnes
    path("personnes", personne.personne_list2, name="personne"),
]
