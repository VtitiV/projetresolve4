from django.shortcuts import render
from Resolve.forms.formpersonne import PersonneSearchForm


# @login_required
def index(request):
    selected = "home"
    form = PersonneSearchForm()
    return render(request, "resolve/home.html", locals())
