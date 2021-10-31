from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from Resolve.models.personne import Personne


@admin.register(Personne)
class PersonneAdmin(ImportExportModelAdmin):
    list_display = ('nom', 'prenom', 'telephone', 'poste')
    pass
