# Generated by Django 4.0.4 on 2022-05-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_pontuacaoquizz_alter_post_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontuacaoquizz',
            name='pontuacao',
            field=models.IntegerField(default=0),
        ),
    ]