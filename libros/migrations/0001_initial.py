# Generated by Django 4.1.6 on 2023-02-03 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Libros",
            fields=[
                ("codigo", models.IntegerField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=35)),
                ("seudonimo", models.CharField(default="Escritor", max_length=35)),
            ],
        ),
    ]
