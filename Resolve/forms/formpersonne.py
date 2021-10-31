from django.forms import ModelForm, Form, CharField
from Resolve.models.personne import Personne
from dal import autocomplete


class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ['nom', 'prenom', 'poste']
        widgets = {
            "Personne": autocomplete.ModelSelect2(url="personne/autocomplete/")
        }


class PersonneSearchForm(Form):
    nom = CharField(max_length=100, required=False)
    prenom = CharField(max_length=100, required=False)
    poste = CharField(max_length=100, required=False)
