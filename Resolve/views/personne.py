from dal import autocomplete
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render
from django.utils.http import urlencode
from Resolve.forms.formpersonne import PersonneSearchForm
from Resolve.models.personne import Personne
from Resolve.forms.formpersonne import PersonneForm


# @login_required
def personne_list2(request):
    selected = "Personne"
    personne_list = Personne.objects.all()
    if request.method == "POST":
        form = PersonneForm(request.POST)
        if form.is_valid():
            base_url = reverse('personne')
            query_string = urlencode(form.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = PersonneForm()
        nom_form = request.GET.get("nom", "")
        prenom_form = request.GET.get("prenom", "")
        poste_form = request.GET.get("poste", "")
        if nom_form is not None:
            personne_list = personne_list.filter(nom__icontains=nom_form)
            form.fields['nom'].initial = nom_form
        if prenom_form is not None:
            personne_list = personne_list.filter(prenom__icontains=prenom_form)
            form.fields['prenom'].initial = prenom_form
        if poste_form is not None:
            personne_list = personne_list.filter(poste__icontains=poste_form)
            form.fields['poste'].initial = poste_form

    paginator = Paginator(personne_list.order_by('date_mise_a_jour'), 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
            personne_list = paginator.page(page)
    except EmptyPage:
        personne_list = paginator.page(paginator.num_pages())
    return render(request, "resolve/personne/personne_list.html", locals())


class PersonneAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Personne.object.none()
        qs = Personne.objects.all()

        if self.q:
            qs = qs.filter(nom_istartswith=self.q)
        return qs
