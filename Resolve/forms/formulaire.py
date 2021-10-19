from  django.forms import  ModelForm
from Resolve.models import personne

class userForm(ModelForm):
    class Meta:
        model = Personne
        fields = ('nom', 'prenom', 'poste', 'telephone','service')