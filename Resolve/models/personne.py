from django.db import models


class Personne(models.Model):
    date_mise_a_jour = models.DateField(verbose_name="date de mise a jour", auto_now=True)
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=10)
    poste = models.CharField(max_length=30, blank=True)
    date_mise_a_jour = models.DateField(verbose_name="Date inscription ", auto_now_add=True)
    db_table = "Personne"


def __str__(self):
    return f"{self.prenom} {self.nom}"
