# Generated by Django 5.0.6 on 2024-06-27 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_movie_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
