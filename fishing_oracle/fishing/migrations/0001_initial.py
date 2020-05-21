# Generated by Django 3.0.4 on 2020-05-21 17:38

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aroma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aroma_volume', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Объем аромы в литрах')),
            ],
            options={
                'verbose_name': 'Арома в прикормочной смеси',
                'verbose_name_plural': 'Аромы в прикормочной смеси',
                'ordering': ['fishing_lure', 'aroma_base', 'aroma_volume'],
            },
        ),
        migrations.CreateModel(
            name='BottomMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottom_map_northern_degree', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N° (-90 до 90)')),
                ('bottom_map_northern_minute', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="N' (0 до 59)")),
                ('bottom_map_northern_second', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='N" (0 до 59.999)')),
                ('bottom_map_easter_degree', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='E° (-180 до 180)')),
                ('bottom_map_easter_minute', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="E' (0 до 59)")),
                ('bottom_map_easter_second', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='E" (0 до 59.999)')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Карта дна',
                'verbose_name_plural': 'Карты дна',
                'ordering': ['bottom_map_northern_degree', 'bottom_map_northern_minute', 'bottom_map_northern_second', 'bottom_map_easter_degree', 'bottom_map_easter_minute', 'bottom_map_easter_second'],
            },
        ),
        migrations.CreateModel(
            name='Crochet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crochet_manufacturer', models.CharField(blank=True, max_length=20, verbose_name='Производитель крючка')),
                ('crochet_model', models.CharField(blank=True, max_length=20, verbose_name='Модель крючка')),
                ('crochet_size', models.PositiveIntegerField(default=0, verbose_name='Размер крючка')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Крючок',
                'verbose_name_plural': 'Крючки',
                'ordering': ['crochet_manufacturer', 'crochet_model', 'crochet_size'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50, unique=True, verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
                'ordering': ['district_name'],
            },
        ),
        migrations.CreateModel(
            name='FeedCapacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_capacity_name', models.CharField(max_length=20, unique=True, verbose_name='Кормоемкость')),
            ],
            options={
                'verbose_name': 'Кормоёмкость кормушки',
                'verbose_name_plural': 'Кормоёмкость кормушек',
                'ordering': ['feed_capacity_name'],
            },
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_fish', models.CharField(max_length=20, unique=True, verbose_name='Рыба')),
                ('fish_description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Рыба',
                'verbose_name_plural': 'Рыбы',
                'ordering': ['name_of_fish'],
            },
        ),
        migrations.CreateModel(
            name='Fishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата рыбалки')),
                ('time', models.TimeField(verbose_name='Время начала')),
                ('aroma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Aroma', verbose_name='Арома')),
                ('crochet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Crochet', verbose_name='Крючек')),
            ],
            options={
                'verbose_name': 'Рыбалка',
                'verbose_name_plural': 'Рыбалки',
                'ordering': ['date', 'time'],
            },
        ),
        migrations.CreateModel(
            name='FishingLure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Прикормочная смесь',
                'verbose_name_plural': 'Прикормочные смеси',
            },
        ),
        migrations.CreateModel(
            name='Overcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overcast_name', models.CharField(max_length=30, unique=True, verbose_name='Классификация облачности')),
            ],
            options={
                'verbose_name': 'Облачность',
                'verbose_name_plural': 'Облачность',
                'ordering': ['overcast_name'],
            },
        ),
        migrations.CreateModel(
            name='Pace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pace_interval', models.CharField(max_length=30, unique=True, verbose_name='Темп')),
            ],
            options={
                'verbose_name': 'Темп',
                'verbose_name_plural': 'Темп',
                'ordering': ['pace_interval'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_locality', models.CharField(help_text='Название ближайшего населенного пункта', max_length=50, verbose_name='Населенный пункт')),
                ('place_name', models.CharField(max_length=50, verbose_name='Название места')),
                ('place_northern_degree', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N° (-90 до 90)')),
                ('place_northern_minute', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="N' (0 до 59)")),
                ('place_northern_second', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)], verbose_name='N" (0 до 59.999)')),
                ('place_easter_degree', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)], verbose_name='E° (-180 до 180)')),
                ('place_easter_minute', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(59), django.core.validators.MinValueValidator(0)], verbose_name="E' (0 до 59)")),
                ('place_easter_second', models.DecimalField(decimal_places=3, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(59.999), django.core.validators.MinValueValidator(0)], verbose_name='E" (0 до 59.999)')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['place_locality'],
            },
        ),
        migrations.CreateModel(
            name='Priming',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priming_name', models.CharField(max_length=50, unique=True, verbose_name='Грунт')),
            ],
            options={
                'verbose_name': 'Покрытие дна',
                'verbose_name_plural': 'Покрытие дна',
                'ordering': ['priming_name'],
            },
        ),
        migrations.CreateModel(
            name='WeatherPhenomena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_phenomena_name', models.CharField(max_length=20, unique=True, verbose_name='Погодные явления')),
            ],
            options={
                'verbose_name': 'Погодное явление',
                'verbose_name_plural': 'Погодные явления',
                'ordering': ['weather_phenomena_name'],
            },
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('weather_temperature', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Температура воздуха')),
                ('pressure', models.PositiveIntegerField(default=760, verbose_name='Давление')),
                ('direction_wind', models.CharField(max_length=30, verbose_name='Направление ветра')),
                ('wind_speed', models.DecimalField(decimal_places=1, default=0, max_digits=4, verbose_name='Скорость ветра')),
                ('lunar_day', models.PositiveIntegerField(default=0, verbose_name='Лунный день')),
                ('overcast', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Overcast', verbose_name='Облачность')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Place', verbose_name='Место')),
                ('weather_phenomena', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.WeatherPhenomena', verbose_name='Явления погоды')),
            ],
            options={
                'verbose_name': 'Погода',
                'verbose_name_plural': 'Погода',
                'ordering': ['date'],
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
                'ordering': ['water_name'],
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_azimuth', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(359), django.core.validators.MinValueValidator(0)], verbose_name='Азимут')),
                ('point_distance', models.PositiveIntegerField(default=0, verbose_name='Дистанция')),
                ('point_depth', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, verbose_name='Глубина')),
                ('bottom_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.BottomMap', verbose_name='Карта дна')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
                ('priming', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Priming', verbose_name='Грунт')),
            ],
            options={
                'verbose_name': 'Точка карты дна',
                'verbose_name_plural': 'Точки карт дна',
                'ordering': ['point_azimuth', 'point_distance'],
            },
        ),
        migrations.CreateModel(
            name='PlaceFishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fishing', verbose_name='Рыбалка')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Place', verbose_name='Место рыбалки')),
            ],
            options={
                'verbose_name': 'Место рыбалки',
                'verbose_name_plural': 'Места рыбалки',
            },
        ),
        migrations.AddField(
            model_name='place',
            name='water',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Water', verbose_name='Водоем'),
        ),
        migrations.CreateModel(
            name='NozzleState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=20, unique=True, verbose_name='Состояние наживки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Состояние насадки',
                'verbose_name_plural': 'Состояние насадок',
                'ordering': ['state'],
            },
        ),
        migrations.CreateModel(
            name='Nozzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bait', models.BooleanField(default=False, verbose_name='Живой компонент')),
                ('nozzle_manufacturer', models.CharField(blank=True, max_length=100, verbose_name='Производитель')),
                ('nozzle_name', models.CharField(max_length=100, verbose_name='Название')),
                ('nozzle_diameter', models.PositiveIntegerField(blank=True, default=0, verbose_name='Диаметр насадки')),
                ('nozzle_type', models.CharField(blank=True, max_length=20, verbose_name='Тип насадки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Наживка/насадка',
                'verbose_name_plural': 'Наживки/насадки',
                'ordering': ['bait', 'nozzle_manufacturer', 'nozzle_name', 'nozzle_type', 'nozzle_diameter'],
            },
        ),
        migrations.CreateModel(
            name='ModelTroughName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_trough_name', models.CharField(max_length=20, unique=True, verbose_name='Модель кормушки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Название модели кормушки',
                'verbose_name_plural': 'Названия моделей кормушек',
                'ordering': ['model_trough_name'],
            },
        ),
        migrations.CreateModel(
            name='ModelTrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_trough_plastic', models.BooleanField(default=False, verbose_name='Пластик')),
                ('model_trough_lugs', models.BooleanField(default=False, verbose_name='грунтозацепы')),
                ('model_trough_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.ModelTroughName', verbose_name='Модель кормушки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Модель кормушки',
                'verbose_name_plural': 'Модели кормушек',
                'ordering': ['model_trough_name'],
            },
        ),
        migrations.CreateModel(
            name='LureBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lure_manufacturer', models.CharField(blank=True, max_length=100, verbose_name='Производитель')),
                ('lure_name', models.CharField(max_length=100, verbose_name='Название')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Базовый прикорм',
                'verbose_name_plural': 'Базовый прикорм',
                'ordering': ['lure_manufacturer', 'lure_name'],
            },
        ),
        migrations.CreateModel(
            name='Lure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lure_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Вес прикорма')),
                ('fishing_lure', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FishingLure', verbose_name='Прикормочная смесь')),
                ('lure_base', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.LureBase', verbose_name='Базовый прикорм')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Прикорм',
                'verbose_name_plural': 'Прикорм',
                'ordering': ['lure_base', 'lure_weight'],
            },
        ),
        migrations.CreateModel(
            name='FishTrophy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fish_trophy_weight', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Вес трофея')),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fish', verbose_name='Рыба')),
                ('fishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Трофейный улов',
                'verbose_name_plural': 'Трофейные уловы',
                'ordering': ['fish_trophy_weight', 'fish'],
            },
        ),
        migrations.CreateModel(
            name='FishingTrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_trough_manufacturer', models.CharField(blank=True, max_length=50, verbose_name='Поизводитель')),
                ('fishing_trough_weight', models.PositiveIntegerField(default=0, verbose_name='Вес кормушки')),
                ('feed_capacity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FeedCapacity', verbose_name='Кормоёмкость')),
                ('model_trough', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.ModelTrough', verbose_name='Модель кормушки')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Рыболовная кормушка',
                'verbose_name_plural': 'Рыболовные кормушки',
                'ordering': ['fishing_trough_manufacturer', 'model_trough', 'fishing_trough_weight', 'feed_capacity'],
            },
        ),
        migrations.CreateModel(
            name='FishingTackle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_tackle_manufacturer', models.CharField(blank=True, max_length=20, verbose_name='Производитель')),
                ('fishing_tackle_name', models.CharField(max_length=30, verbose_name='Название')),
                ('fishing_tackle_length', models.DecimalField(decimal_places=1, default=0, max_digits=3, verbose_name='Длина (м)')),
                ('fishing_tackle_casting_weight', models.PositiveIntegerField(blank=True, default=0, verbose_name='Тест удилища (гр)')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Рыболовная снасть',
                'verbose_name_plural': 'Рыболовные снасти',
                'ordering': ['fishing_tackle_manufacturer', 'fishing_tackle_name', 'fishing_tackle_length', 'fishing_tackle_casting_weight'],
            },
        ),
        migrations.CreateModel(
            name='FishingResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_fish', models.PositiveIntegerField(blank=True, verbose_name='Количество рыб')),
                ('fish_weight', models.DecimalField(blank=True, decimal_places=1, max_digits=6, verbose_name='Вес улова')),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Fish', verbose_name='Рыба')),
                ('fishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Fishing', verbose_name='Рыбалка')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Результат рыбалки',
                'verbose_name_plural': 'Результат рыбалок',
                'ordering': ['fish'],
            },
        ),
        migrations.CreateModel(
            name='FishingPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_point_azimuth', models.PositiveIntegerField(default=0, verbose_name='Азимут')),
                ('fishing_point_distance', models.PositiveIntegerField(default=0, verbose_name='Дистанция')),
                ('fishing_poiny_depth', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=4, verbose_name='Глубина')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='fishing.Place', verbose_name='Место ловли')),
                ('priming', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Priming', verbose_name='Грунт')),
            ],
            options={
                'verbose_name': 'Точка ловли',
                'verbose_name_plural': 'Точки ловли',
                'ordering': ['fishing_point_distance'],
            },
        ),
        migrations.CreateModel(
            name='FishingMontage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_montage_name', models.CharField(max_length=15, verbose_name='Монтаж')),
                ('fishing_montage_sliding', models.BooleanField(default=False, verbose_name='Скользящий монтаж')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Монтаж',
                'verbose_name_plural': 'Монтажи',
                'ordering': ['fishing_montage_name'],
            },
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
        migrations.CreateModel(
            name='FishingLeash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fishing_leash_material', models.CharField(max_length=20, verbose_name='Поводочный материал')),
                ('fishing_leash_diameter', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Диамет поводочного материла')),
                ('fishing_leash_length', models.PositiveIntegerField(default=0, verbose_name='Длина поводка')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Поводок',
                'verbose_name_plural': 'Поводки',
                'ordering': ['fishing_leash_material', 'fishing_leash_diameter', 'fishing_leash_length'],
            },
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
            name='weather',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.Weather', verbose_name='Погода'),
        ),
        migrations.AddField(
            model_name='bottommap',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fishing.Place', verbose_name='Место'),
        ),
        migrations.CreateModel(
            name='AromaBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aroma_manufacturer', models.CharField(blank=True, max_length=100, verbose_name='Производтель')),
                ('aroma_name', models.CharField(max_length=100, verbose_name='Название')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи')),
            ],
            options={
                'verbose_name': 'Арома базовая',
                'verbose_name_plural': 'Аромы базовые',
                'ordering': ['aroma_manufacturer', 'aroma_name'],
            },
        ),
        migrations.AddField(
            model_name='aroma',
            name='aroma_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.AromaBase', verbose_name='Арома базовая'),
        ),
        migrations.AddField(
            model_name='aroma',
            name='fishing_lure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fishing.FishingLure', verbose_name='Прикормочная смесь'),
        ),
        migrations.AddField(
            model_name='aroma',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Владелец записи'),
        ),
    ]
