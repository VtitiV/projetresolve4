from django.shortcuts import render


def index(request):
    select = "home"
    return render(request, "resolve/home.html", locals())
