from django.urls import path
from .views import home, personne, formulaire
from .views import incident, ancres
from .views.personne import PersonneAutocomplete

urlpatterns = [
    path("", home.index, name="home"),
    # Personnes
    path("personne/", personne.personne_list2, name="personne"),
    # vue incident/demande
    path("incidents/", incident.incidents_list, name="incident"),
    # vue incidenthm
    path("connexionhm/", incident.connexionhm, name="incidenthm"),
    # vue ancres
    path("ancres/", ancres.listancre, name="ancres"),
    # vue user
    path("userforms/", formulaire.formuser, name="user"),
    # vue personne autocomplete
    path("personne/autocomplete/", PersonneAutocomplete.as_view(), name="personne_autocomplete"),

]
