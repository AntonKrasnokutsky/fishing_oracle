# Generated by Django 3.0.4 on 2020-04-12 16:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aroma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aroma_manufacturer', models.CharField(max_length=100, verbose_name='Производтель')),
                ('aroma_name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Арома',
                'verbose_name_plural': 'Аромы',
            },
        ),
        migrations.CreateModel(
            name='Bottom_Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottom_map_northern_degree', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N° (-90 до 90)')),
                ('bottom_map_northern_minute', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="N' (0 до 59)")),
                ('bottom_map_northern_second', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='N" (0 до 59.999)')),
                ('bottom_map_easter_degree', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='E° (-180 до 180)')),
                ('bottom_map_easter_minute', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="E' (0 до 59)")),
                ('bottom_map_easter_second', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='E" (0 до 59.999)')),
            ],
            options={
                'verbose_name': 'Карта дна',
                'verbose_name_plural': 'Карты дна',
            },
        ),
        migrations.CreateModel(
            name='Crochet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crochet_manufacturer', models.CharField(max_length=20, verbose_name='Производитель крючка')),
                ('crochet_model', models.CharField(max_length=20, verbose_name='Модель крючка')),
                ('crochet_size', models.PositiveIntegerField(default=0, verbose_name='Размер крючка')),
            ],
            options={
                'verbose_name': 'Крючок',
                'verbose_name_plural': 'Крючки',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Feed_Capacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_capacity_name', models.CharField(max_length=20, verbose_name='Кормоемкость')),
            ],
            options={
                'verbose_name': 'Кормоёмкость кормушки',
                'verbose_name_plural': 'Кормоёмкость кормушек',
            },
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_fish', models.CharField(max_length=20, verbose_name='Рыба')),
                ('fish_description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Рыба',
                'verbose_name_plural': 'Рыбы',
            },
        ),
        migrations.CreateModel(
            name='Fishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата рыбалки')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Время начала')),
                ('aroma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Aroma', verbose_name='Арома')),
                ('crochet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Crochet', verbose_name='Крючек')),
            ],
            options={
                'verbose_name': 'Рыбалка',
                'verbose_name_plural': 'Рыбалки',
            },
        ),
        migrations.CreateModel(
            name='Fishing_Leash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_leash_material', models.CharField(max_length=20, verbose_name='Поводочный материал')),
                ('fishing_leash_diameter', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Диамет поводочного материла')),
                ('fishing_leash_length', models.PositiveIntegerField(default=0, verbose_name='Длина поводка')),
            ],
            options={
                'verbose_name': 'Поводок',
                'verbose_name_plural': 'Поводки',
            },
        ),
        migrations.CreateModel(
            name='Fishing_Lure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Прикормочная смесь',
                'verbose_name_plural': 'Прикормочные смеси',
            },
        ),
        migrations.CreateModel(
            name='Fishing_Montage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_montage_name', models.CharField(max_length=15, verbose_name='Монтаж')),
                ('fishing_montage_sliding', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Монтаж',
                'verbose_name_plural': 'Монтажи',
            },
        ),
        migrations.CreateModel(
            name='Fishing_Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_point_azimuth', models.PositiveIntegerField(default=0, verbose_name='Азимут')),
                ('fishing_point_distance', models.PositiveIntegerField(default=0, verbose_name='Дистанция')),
                ('fishing_poiny_depth', models.PositiveIntegerField(default=0, verbose_name='Глубина')),
            ],
            options={
                'verbose_name': 'Точка ловли',
                'verbose_name_plural': 'Точки ловли',
            },
        ),
        migrations.CreateModel(
            name='Fishing_Tackle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_tackle_name', models.CharField(max_length=30, verbose_name='Снасть')),
            ],
            options={
                'verbose_name': 'Рыболовная снасть',
                'verbose_name_plural': 'Рыболовные снасти',
            },
        ),
        migrations.CreateModel(
            name='Model_Trough_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_trough_name', models.CharField(max_length=20, verbose_name='Модель кормушки')),
            ],
            options={
                'verbose_name': 'Название модели кормушки',
                'verbose_name_plural': 'Названия моделей кормушек',
            },
        ),
        migrations.CreateModel(
            name='Nozzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bait', models.BooleanField(default=False, verbose_name='Живой компонент')),
                ('nozzle_manufacturer', models.CharField(max_length=100, verbose_name='Производитель')),
                ('nozzle_name', models.CharField(max_length=100, verbose_name='Название')),
                ('nozzel_diameter', models.PositiveIntegerField(default=0, verbose_name='Диаметр насадки')),
                ('nozzel_type', models.CharField(max_length=20, verbose_name='Тип насадки')),
            ],
            options={
                'verbose_name': 'Наживка/насадка',
                'verbose_name_plural': 'Наживки/насадки',
            },
        ),
        migrations.CreateModel(
            name='Nozzle_State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20, verbose_name='Состояние наживки')),
            ],
            options={
                'verbose_name': 'Состояние насадки',
                'verbose_name_plural': 'Состояние насадок',
            },
        ),
        migrations.CreateModel(
            name='Overcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overcast_name', models.CharField(max_length=20, verbose_name='Классификация облачности')),
            ],
            options={
                'verbose_name': 'Облачность',
                'verbose_name_plural': 'Облачность',
            },
        ),
        migrations.CreateModel(
            name='Pace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pace_interval', models.CharField(max_length=20, verbose_name='Темп')),
            ],
            options={
                'verbose_name': 'Темп',
                'verbose_name_plural': 'Темп',
            },
        ),
        migrations.CreateModel(
            name='Priming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priming_name', models.CharField(max_length=50, verbose_name='Грунт')),
            ],
            options={
                'verbose_name': 'Покрытие дна',
                'verbose_name_plural': 'Покрытие дна',
            },
        ),
        migrations.CreateModel(
            name='Weather_Phenomena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_phenomena_name', models.CharField(max_length=20, verbose_name='Погодные явления')),
            ],
            options={
                'verbose_name': 'Погодное явление',
                'verbose_name_plural': 'Погодные явления',
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_temperature', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Температура воздуха')),
                ('pressure', models.PositiveIntegerField(default=760, verbose_name='Давление')),
                ('direction_wind', models.CharField(max_length=30, verbose_name='Направление ветра')),
                ('wind_speed', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Скорость ветра')),
                ('lunar_day', models.PositiveIntegerField(default=0, verbose_name='Лунный день')),
                ('overcast', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Overcast', verbose_name='Облачность')),
                ('weather_phenomena', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Weather_Phenomena', verbose_name='Явления погоды')),
            ],
            options={
                'verbose_name': 'Погода',
                'verbose_name_plural': 'Погода',
            },
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water_name', models.CharField(max_length=100, verbose_name='Водоем')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.District', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Водоем',
                'verbose_name_plural': 'Водоемы',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_azimuth', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(359), django.core.validators.MinValueValidator(0)], verbose_name='Азимут')),
                ('point_distance', models.PositiveIntegerField(default=0, verbose_name='Дистанция')),
                ('point_depth', models.PositiveIntegerField(default=0, verbose_name='Глубина')),
                ('bottom_map', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fishing.Bottom_Map', verbose_name='Карта дна')),
                ('priming', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Priming', verbose_name='Грунт')),
            ],
            options={
                'verbose_name': 'Точка карты дна',
                'verbose_name_plural': 'Точки карт дна',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_locality', models.CharField(max_length=50, verbose_name='Начеленный пункт')),
                ('place_northern_degree', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N° (-90 до 90)')),
                ('place_northern_minute', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="N' (0 до 59)")),
                ('place_northern_second', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N" (0 до 59.999)')),
                ('place_easter_degree', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='E° (-180 до 180)')),
                ('place_easter_minute', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="E' (0 до 59)")),
                ('place_easter_second', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='E" (0 до 59.999)')),
                ('fishing_point', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fishing_Point', verbose_name='Точка ловли')),
                ('water', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Water', verbose_name='Водоем')),
            ],
            options={
                'verbose_name': 'Место рыбалки',
                'verbose_name_plural': 'Места рыбалок',
            },
        ),
        migrations.CreateModel(
            name='Model_Trough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_trough_plastic', models.BooleanField(default=False, verbose_name='Пластик')),
                ('model_trough_lugs', models.BooleanField(default=False, verbose_name='грунтозацепы')),
                ('model_trough_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Model_Trough_Name', verbose_name='Модель кормушки')),
            ],
            options={
                'verbose_name': 'Модель кормушки',
                'verbose_name_plural': 'Модели кормушек',
            },
        ),
        migrations.CreateModel(
            name='Lure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lure_manufacturer', models.CharField(max_length=100, verbose_name='Производитель')),
                ('lure_name', models.CharField(max_length=100, verbose_name='Название')),
                ('fishing_lure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fishing_Lure', verbose_name='Прикормочная смесь')),
            ],
            options={
                'verbose_name': 'Прикорм',
                'verbose_name_plural': 'Прикорм',
            },
        ),
        migrations.CreateModel(
            name='Fishing_Trough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_trough_manufacturer', models.CharField(max_length=50, verbose_name='Поизводитель')),
                ('fishing_trough_weight', models.PositiveIntegerField(default=0, verbose_name='Вес кормушки')),
                ('feed_capacity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Feed_Capacity', verbose_name='Кормоёмкость')),
                ('model_trough', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Model_Trough', verbose_name='Модель кормушки')),
            ],
            options={
                'verbose_name': 'Рыболовная кормушка',
                'verbose_name_plural': 'Рыболовные кормушки',
            },
        ),
        migrations.CreateModel(
            name='Fishing_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nuber_of_fish', models.PositiveIntegerField(verbose_name='Количество рыб')),
                ('fish_weight', models.PositiveIntegerField(verbose_name='Вес улова')),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fish', verbose_name='Рыба')),
                ('fishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка')),
            ],
            options={
                'verbose_name': 'Результат рыбалки',
                'verbose_name_plural': 'Результат рыбалок',
            },
        ),
        migrations.AddField(
            model_name='fishing_point',
            name='priming',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Priming', verbose_name='Грунт'),
        ),
        migrations.AddField(
            model_name='fishing_lure',
            name='nozzle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Nozzle', verbose_name='Наживка'),
        ),
        migrations.AddField(
            model_name='fishing_lure',
            name='nozzle_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Nozzle_State', verbose_name='Состояние наживки'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_leash',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fishing_Leash', verbose_name='Поводок'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_lure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fishing_Lure', verbose_name='Прикормочная смесь'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_montage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fishing_Montage', verbose_name='Монтаж'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_tackle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fishing_Tackle', verbose_name='Снасть'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='fishing_trough',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fishing_Trough', verbose_name='Кормушка'),
        ),
        migrations.AddField(
            model_name='fishing',
            name='nozzle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Nozzle', verbose_name='Наживка/насадка'),
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
        migrations.CreateModel(
            name='Fish_Trophy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish_trophy_weight', models.PositiveIntegerField(verbose_name='Вес трофея')),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fish', verbose_name='Рыба')),
                ('fishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка')),
            ],
            options={
                'verbose_name': 'Трофейный улов',
                'verbose_name_plural': 'Трофейные уловы',
            },
        ),
        migrations.AddField(
            model_name='bottom_map',
            name='water',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='fishing.Water', verbose_name='Водоем'),
        ),
    ]
