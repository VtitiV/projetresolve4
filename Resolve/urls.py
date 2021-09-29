from django.urls import path

from .views import home, personne
from .views import incident


urlpatterns = [
    path("", home.index, name="home"),
    # Personnes
    path("personne/", personne.personne_list2, name="personne"),
    # vue incident/demande
    path("incidents/", incident.incidents_list, name="incident"),
]
