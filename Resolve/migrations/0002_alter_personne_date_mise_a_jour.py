# Generated by Django 3.2.7 on 2021-09-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Resolve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='date_mise_a_jour',
            field=models.DateField(auto_now_add=True, verbose_name="Date d'inscription "),
        ),
    ]
