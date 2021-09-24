from django.urls import path

from .views import home, personne, incident

urlpatterns = [
    path("", home.index, name="home"),
    # Personnes
    path("personne/", personne.personne_list2, name="personne"),
    # vue incident/demande
    path("incident/", incident.incidents_list, name="incident"),
]
