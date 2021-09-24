from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# @login_required
def index(request):
    selected = "home"
    return render(request, "resolve/home.html", locals())

