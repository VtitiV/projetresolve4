from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render

from Resolve.models.personne import Personne


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
