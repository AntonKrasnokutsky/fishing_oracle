# Generated by Django 3.0.4 on 2020-04-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overcast',
            name='overcast_name',
            field=models.CharField(max_length=30, verbose_name='Классификация облачности'),
        ),
    ]