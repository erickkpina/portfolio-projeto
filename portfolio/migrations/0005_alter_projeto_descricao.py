# Generated by Django 4.0.4 on 2022-06-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_rename_linkedinpaginacadeira_cadeira_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
