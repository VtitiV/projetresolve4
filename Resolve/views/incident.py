from django.shortcuts import render


def incidents_list(request):
    selected = "incident"
    return render(request, "resolve/incident/Incidents.html", locals())


def connexionhm(request):
    selected = "connexionHM"
    return render(request, "resolve/incident/list_incident/connexionHM.html", locals())
