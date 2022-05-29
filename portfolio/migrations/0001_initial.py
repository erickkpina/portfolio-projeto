# Generated by Django 4.0.4 on 2022-05-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=25)),
                ('titulo', models.CharField(max_length=70)),
                ('descricao', models.CharField(max_length=250)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
