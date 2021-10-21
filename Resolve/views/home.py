from django.shortcuts import render
from Resolve.models.personne import Personne
from django import forms


# @login_required
def index(request):
    selected = "home"
    return render(request, "resolve/home.html", locals())


