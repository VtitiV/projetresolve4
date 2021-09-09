from django.db import models


class Personne(models.Model):

    date_mise_a_jour = models.DateField(verbose_name="date de mise a jour", auto_now=True)
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    telephone = models.CharField(max_length=10)
    lieu = models.CharField(max_length=30, blank=True)


def __str__(self):
    return f"{self.prenom} {self.nom}"
