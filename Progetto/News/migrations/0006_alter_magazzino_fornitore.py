# Generated by Django 5.1.3 on 2024-11-21 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0005_fornitore_magazzino_fornitore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magazzino',
            name='Fornitore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FMagazzino', to='News.fornitore'),
        ),
    ]
