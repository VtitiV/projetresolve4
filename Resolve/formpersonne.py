from django.forms import ModelForm

from Resolve.models.personne import Personne


class PersonneSearchForm(ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom']
