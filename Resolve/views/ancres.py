from django.shortcuts import render


# @login_required
def listancre(request):
    selected = "ancres"
    return render(request, "ancres/Ancres.html", locals())
