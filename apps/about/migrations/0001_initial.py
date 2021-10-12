# Generated by Django 2.2.24 on 2021-10-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ally',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('description', models.CharField(max_length=220, verbose_name='Descripción')),
                ('logo', models.ImageField(blank=True, upload_to='about/allies/')),
                ('url', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
