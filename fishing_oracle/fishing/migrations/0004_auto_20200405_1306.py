# Generated by Django 3.0.4 on 2020-04-05 10:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fishing', '0003_auto_20200404_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aroma',
            options={'verbose_name': 'Арома', 'verbose_name_plural': 'Аромы'},
        ),
        migrations.AlterModelOptions(
            name='bottom_map',
            options={'verbose_name': 'Карта дна', 'verbose_name_plural': 'Карты дна'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'Район', 'verbose_name_plural': 'Районы'},
        ),
        migrations.AlterModelOptions(
            name='fish',
            options={'verbose_name': 'Рыба', 'verbose_name_plural': 'Рыбы'},
        ),
        migrations.AlterModelOptions(
            name='fish_trophy',
            options={'verbose_name': 'Трофейный улов', 'verbose_name_plural': 'Трофейные уловы'},
        ),
        migrations.AlterModelOptions(
            name='fishing',
            options={'verbose_name': 'Рыбалка', 'verbose_name_plural': 'Рыбалки'},
        ),
        migrations.AlterModelOptions(
            name='fishing_point',
            options={'verbose_name': 'Точка ловли', 'verbose_name_plural': 'Точки ловли'},
        ),
        migrations.AlterModelOptions(
            name='fishing_result',
            options={'verbose_name': 'Результат рыбалки', 'verbose_name_plural': 'Результат рыбалок'},
        ),
        migrations.AlterModelOptions(
            name='fishing_tackle',
            options={'verbose_name': 'Рыболовная снасть', 'verbose_name_plural': 'Рыболовные снасти'},
        ),
        migrations.AlterModelOptions(
            name='lure',
            options={'verbose_name': 'Прикорм', 'verbose_name_plural': 'Прикорм'},
        ),
        migrations.AlterModelOptions(
            name='nozzle',
            options={'verbose_name': 'Наживка/насадка', 'verbose_name_plural': 'Наживки/насадки'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место рыбалки', 'verbose_name_plural': 'Места рыбалок'},
        ),
        migrations.AlterModelOptions(
            name='point',
            options={'verbose_name': 'Точка карты дна', 'verbose_name_plural': 'Точки карт дна'},
        ),
        migrations.AlterModelOptions(
            name='priming',
            options={'verbose_name': 'Покрытие дна', 'verbose_name_plural': 'Покрытие дна'},
        ),
        migrations.AlterModelOptions(
            name='water',
            options={'verbose_name': 'Водоем', 'verbose_name_plural': 'Водоемы'},
        ),
        migrations.AlterModelOptions(
            name='weather',
            options={'verbose_name': 'Погода', 'verbose_name_plural': 'Погода'},
        ),
        migrations.AlterModelOptions(
            name='weather_phenomena',
            options={'verbose_name': 'Погодное явление', 'verbose_name_plural': 'Погодные явления'},
        ),
        migrations.AlterField(
            model_name='aroma',
            name='aroma_manufacturer',
            field=models.CharField(max_length=100, verbose_name='Производтель'),
        ),
        migrations.AlterField(
            model_name='aroma',
            name='aroma_name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='bottom_map',
            name='bottom_map_easter_degree',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='E° (-180 до 180)'),
        ),
        migrations.AlterField(
            model_name='bottom_map',
            name='bottom_map_easter_minute',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="E' (0 до 59)"),
        ),
        migrations.AlterField(
            model_name='bottom_map',
            name='bottom_map_easter_second',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='E" (0 до 59.999)'),
        ),
        migrations.AlterField(
            model_name='bottom_map',
            name='bottom_map_northern_degree',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N° (-90 до 90)'),
        ),
        migrations.AlterField(
            model_name='bottom_map',
            name='bottom_map_northern_minute',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="N' (0 до 59)"),
        ),
        migrations.AlterField(
            model_name='bottom_map',
            name='bottom_map_northern_second',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='N" (0 до 59.999)'),
        ),
        migrations.AlterField(
            model_name='bottom_map',
            name='water',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Water', verbose_name='Водоем'),
        ),
        migrations.AlterField(
            model_name='district',
            name='district_name',
            field=models.CharField(max_length=50, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='fish',
            name='name_of_fish',
            field=models.CharField(max_length=20, verbose_name='Рыба'),
        ),
        migrations.AlterField(
            model_name='fish_trophy',
            name='fish',
            field=models.PositiveIntegerField(default=0, verbose_name='Трофейная рыба'),
        ),
        migrations.AlterField(
            model_name='fish_trophy',
            name='fish_trophy_weight',
            field=models.PositiveIntegerField(default=0, verbose_name='Вес трофея'),
        ),
        migrations.AlterField(
            model_name='fish_trophy',
            name='fishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка'),
        ),
        migrations.AlterField(
            model_name='fishing_point',
            name='fishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка'),
        ),
        migrations.AlterField(
            model_name='fishing_point',
            name='fishing_point_azimuth',
            field=models.PositiveIntegerField(default=0, verbose_name='Азимут'),
        ),
        migrations.AlterField(
            model_name='fishing_point',
            name='fishing_point_distance',
            field=models.PositiveIntegerField(default=0, verbose_name='Дистанция'),
        ),
        migrations.AlterField(
            model_name='fishing_point',
            name='fishing_poiny_depth',
            field=models.PositiveIntegerField(default=0, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='fishing_point',
            name='priming',
            field=models.PositiveIntegerField(verbose_name='Грунт'),
        ),
        migrations.AlterField(
            model_name='fishing_result',
            name='fish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fish', verbose_name='Рыба'),
        ),
        migrations.AlterField(
            model_name='fishing_result',
            name='fish_weight',
            field=models.PositiveIntegerField(default=0, verbose_name='Вес улова'),
        ),
        migrations.AlterField(
            model_name='fishing_result',
            name='fishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка'),
        ),
        migrations.AlterField(
            model_name='fishing_result',
            name='nuber_of_fish',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество рыб'),
        ),
        migrations.AlterField(
            model_name='fishing_tackle',
            name='fishing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка'),
        ),
        migrations.AlterField(
            model_name='fishing_tackle',
            name='fishing_tackle_name',
            field=models.CharField(max_length=30, verbose_name='Снасть'),
        ),
        migrations.AlterField(
            model_name='lure',
            name='lure_manufacturer',
            field=models.CharField(max_length=100, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='lure',
            name='lure_name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='nozzle',
            name='bait',
            field=models.BooleanField(default=False, verbose_name='Живой компонент'),
        ),
        migrations.AlterField(
            model_name='nozzle',
            name='nozzle_manufacturer',
            field=models.CharField(max_length=100, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='nozzle',
            name='nozzle_name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='place',
            name='bottom_map',
            field=models.PositiveIntegerField(verbose_name='Карта дна'),
        ),
        migrations.AlterField(
            model_name='place',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.District', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='place',
            name='fishing_point',
            field=models.PositiveIntegerField(verbose_name='Точка ловли'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_easter_degree',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='E° (-180 до 180)'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_easter_minute',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="E' (0 до 59)"),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_easter_second',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='E" (0 до 59.999)'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_locality',
            field=models.CharField(max_length=50, verbose_name='Начеленный пункт'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_northern_degree',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N° (-90 до 90)'),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_northern_minute',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="N' (0 до 59)"),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_northern_second',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N" (0 до 59.999)'),
        ),
        migrations.AlterField(
            model_name='place',
            name='water',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Water', verbose_name='Водоем'),
        ),
        migrations.AlterField(
            model_name='point',
            name='bottom_map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Bottom_Map', verbose_name='Карта дна'),
        ),
        migrations.AlterField(
            model_name='point',
            name='point_azimuth',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(359), django.core.validators.MinValueValidator(0)], verbose_name='Азимут'),
        ),
        migrations.AlterField(
            model_name='point',
            name='point_depth',
            field=models.PositiveIntegerField(default=0, verbose_name='Глубина'),
        ),
        migrations.AlterField(
            model_name='point',
            name='point_distance',
            field=models.PositiveIntegerField(default=0, verbose_name='Дистанция'),
        ),
        migrations.AlterField(
            model_name='point',
            name='priming',
            field=models.PositiveIntegerField(verbose_name='Грунт'),
        ),
        migrations.AlterField(
            model_name='priming',
            name='priming_name',
            field=models.CharField(max_length=50, verbose_name='Грунт'),
        ),
        migrations.AlterField(
            model_name='water',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.District', verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='water',
            name='water_name',
            field=models.CharField(max_length=100, verbose_name='Водоем'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='direction_wind',
            field=models.CharField(max_length=30, verbose_name='Направление ветра'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='lunar_day',
            field=models.PositiveIntegerField(default=0, verbose_name='Лунный день'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='overcast',
            field=models.CharField(max_length=30, verbose_name='Облачность'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='pressure',
            field=models.PositiveIntegerField(default=760, verbose_name='Давление'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='weather_locality',
            field=models.CharField(max_length=30, verbose_name='Населенный пункт'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='weather_temperature',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Температура воздуха'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='wind_speed',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Скорость ветра'),
        ),
        migrations.AlterField(
            model_name='weather_phenomena',
            name='weather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Weather', verbose_name='Погода'),
        ),
        migrations.AlterField(
            model_name='weather_phenomena',
            name='weather_phenomena_name',
            field=models.CharField(max_length=20, verbose_name='Погодные явления'),
        ),
    ]
