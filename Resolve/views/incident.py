from django.shortcuts import render


def incidents_list(request):
    selected = "incident"
    return render(request, "resolve/incident/Incidents.html", locals())


def connexionhm(request):
    selected = "connexionHM"
    context = {
        'text1' : "Nous avons verifier les codes"
    }
    return render(request, "resolve/incident/list_incident/connexionHM.html", context, locals())


