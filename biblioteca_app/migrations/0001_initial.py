# Generated by Django 5.0.6 on 2024-06-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=40)),
                ('anio_publicacion', models.IntegerField()),
            ],
        ),
    ]
