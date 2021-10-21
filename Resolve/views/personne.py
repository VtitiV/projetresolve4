from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from Resolve.models.personne import Personne
from Resolve.forms.formulaire import PersonneSearchForm
from django.template.defaultfilters import urlencode
from django.urls import reverse_lazy, reverse


# @login_required
def personne_list2(request):
    selected = "personne"
    personne_list = Personne.objects.all()
    paginator = Paginator(personne_list.order_by('date_mise_a_jour'), 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
            personne_list = paginator.page(page)
    except EmptyPage:
        personne_list = paginator.page(paginator.num_pages())
    return render(request, "resolve/personne/personne_list.html", locals())


def personne_list3(request):
    selected = "personne"
    personne_list = Personne.objects.all()

    if request.methode == "POST":
        form = PersonneSearchForm(request.Post)
        if form.is_valid():
            base_url = reverse('home')
            query_string = urlencode(form.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = PersonneSearchForm()
        nom_form = request.GET.get("nom", "")
        prenom_form = request.GET.get("prenom", "")
        poste_form = request.GET.get("poste", "")
        if nom_form is not None:
            personne_list = personne_list2.filter(nom__icontains=nom_form)
            form.fields['nom'].initial = nom_form
        if prenom_form is not None:
            personne_list = personne_list2.filter(prenom__icontains=prenom_form)
            form.fields['nom'].initial = prenom_form
        if poste_form is not None:
            personne_list = personne_list2.filter(poste__icontains=poste_form)
            form.fields['nom'].initial = poste_form
            return render(request, "resolve/home.html", locals())
