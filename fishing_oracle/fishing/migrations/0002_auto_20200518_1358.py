# Generated by Django 3.0.4 on 2020-05-18 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fishing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='point',
            name='priming',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Priming', verbose_name='Грунт'),
        ),
        migrations.AddField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='place',
            name='water',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Water', verbose_name='Водоем'),
        ),
        migrations.AddField(
            model_name='nozzlestate',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='nozzle',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='modeltroughname',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='modeltrough',
            name='model_trough_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.ModelTroughName', verbose_name='Модель кормушки'),
        ),
        migrations.AddField(
            model_name='modeltrough',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='lurebase',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='lure',
            name='fishing_lure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FishingLure', verbose_name='Прикормочная смесь'),
        ),
        migrations.AddField(
            model_name='lure',
            name='lure_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.LureBase', verbose_name='Базовый прикорм'),
        ),
        migrations.AddField(
            model_name='lure',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishtrophy',
            name='fish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fish', verbose_name='Рыба'),
        ),
        migrations.AddField(
            model_name='fishtrophy',
            name='fishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка'),
        ),
        migrations.AddField(
            model_name='fishtrophy',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishingtrough',
            name='feed_capacity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FeedCapacity', verbose_name='Кормоёмкость'),
        ),
        migrations.AddField(
            model_name='fishingtrough',
            name='model_trough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.ModelTrough', verbose_name='Модель кормушки'),
        ),
        migrations.AddField(
            model_name='fishingtrough',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishingtackle',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishingresult',
            name='fish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fish', verbose_name='Рыба'),
        ),
        migrations.AddField(
            model_name='fishingresult',
            name='fishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка'),
        ),
        migrations.AddField(
            model_name='fishingresult',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishingpoint',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishingpoint',
            name='place',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='fishing.Place', verbose_name='Место ловли'),
        ),
        migrations.AddField(
            model_name='fishingpoint',
            name='priming',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Priming', verbose_name='Грунт'),
        ),
        migrations.AddField(
            model_name='fishingmontage',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishinglure',
            name='nozzle',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='fishing.Nozzle', verbose_name='Наживка'),
        ),
        migrations.AddField(
            model_name='fishinglure',
            name='nozzle_state',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='fishing.NozzleState', verbose_name='Состояние наживки'),
        ),
        migrations.AddField(
            model_name='fishinglure',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishingleash',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='aroma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Aroma', verbose_name='Арома'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='crochet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Crochet', verbose_name='Крючек'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_leash',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FishingLeash', verbose_name='Поводок'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_lure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FishingLure', verbose_name='Прикормочная смесь'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_montage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FishingMontage', verbose_name='Монтаж'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_tackle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FishingTackle', verbose_name='Снасть'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_trough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FishingTrough', verbose_name='Кормушка'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='nozzle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Nozzle', verbose_name='Наживка/насадка'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='pace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Pace', verbose_name='Темп'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Place', verbose_name='Место рыбалки'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='weather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Weather', verbose_name='Погода'),
        ),
        migrations.AddField(
            model_name='crochet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='bottommap',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
        migrations.AddField(
            model_name='bottommap',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Place', verbose_name='Место'),
        ),
        migrations.AddField(
            model_name='aroma',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
    ]