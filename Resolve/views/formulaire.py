from django.shortcuts import render
from Resolve.forms.formpersonne import PersonneSearchForm


def formuser(request):
    form = PersonneSearchForm()
    return render(request, 'forms/userforms.html', {'form': form})


