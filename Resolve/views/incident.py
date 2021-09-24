from django.shortcuts import render


def incidents_list(request):
    select = "incident"
    return render(request, "resolve/incident/Incidents.html", locals())
