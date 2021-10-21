from Resolve.models.personne import Personne
from Resolve.forms.formulaire import userForm


def formuser(request):
    form = userForm()

    return render(request, 'userforms.html', {'form': form})
