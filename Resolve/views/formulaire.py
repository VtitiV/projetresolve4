from django.shortcuts import render
from Resolve.formulaire import PersonneSearchForm
from Resolve.models.personne import Personne


def formuser(request):
    form = PersonneSearchForm()
    select = "userforms"
    return render(request, 'forms/userforms.html', {'form': form })
