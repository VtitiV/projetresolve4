from django.urls import path

from Resolve.views import home
from Resolve.views import personne

urlpatterns = [
    path("", home.index, name="home"),
    # Personnes
    path("personne/", personne.personne_list, name="personne"),
]
