from django.forms import Form, CharField
from django import forms


class PersonneSearchForm(forms.ModelForm):
    nom = CharField(max_length=100, required=False)
    prenom = CharField(max_length=100, required=False)
    poste = CharField(max_length=100, required=False)
