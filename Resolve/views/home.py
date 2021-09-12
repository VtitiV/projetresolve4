from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    selected = "home"
    return render(request, "resolve/home.html", locals())
