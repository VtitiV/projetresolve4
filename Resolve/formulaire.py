from django import forms
from Resolve.models.personne import Personne


class PersonneSearchForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom']
