from django.db import models


class Fishing(models.Model):
    pass


class Fish(models.Model):
    """
    Таблица хранящая в себе информацию о породах рыб,
    в дальнейшем планируется добавление изображение рыб
    """
    # Название рыбы https://gdekluet.ru/directory/fish/
    name_of_fish = models.CharField(max_length=20)

    def __str__(self):
        return self.name_of_fish


class Fishing_Result(models.Model):
    """
    Содержит информацию о результате рыбалки, принимает
    в себя несколько значений пойманной рыбы
    """
    # Привязка к рыбалке
    fishing = models.ForeignKey(Fishing, on_delete=models.CASCADE)
    # Рыба
    fish = models.PositiveIntegerField(default=0)
    # Количество хвостов
    nuber_of_fish = models.PositiveIntegerField(default=0)
    # Масса улова по выбранной рыбе
    fish_weight = models.PositiveIntegerField(default=0)


class Fish_Trophy(models.Model):
    # Привязка к рыбалке
    fishing = models.ForeignKey(Fishing, on_delete=models.CASCADE)
    # Порода трофея
    fish = models.PositiveIntegerField(default=0)
    # Вес трофея
    fish_trophy_weight = models.PositiveIntegerField(default=0)
#    fish_trophy_photo=models.ImageField()


class Weather(models.Model):
    """
    Содержит сводные сведения о погоде
    опираясь на ручной ввод
    """
    # облачность
    overcast = models.CharField(max_length=30)
    # Город
    weather_locality = models.CharField(max_length=30)
    # Температура воздуха
    weather_temperature = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=0)
    # Давление
    pressure = models.PositiveIntegerField(default=750)
    # Направление ветра
    direction_wind = models.CharField(max_length=30)
    # Скорость ветра
    wind_speed = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        default=0)
    # Лунный день
    lunar_day = models.PositiveIntegerField(default=0)


class Weather_Phenomena(models.Model):
    """
    Явления погоды, возможно несколько записей
    для одного выезда
    """
    # Привязка к погоде
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE)
    # Погодные явления
    weather_phenomena_name = models.CharField(max_length=20)


class Aroma(models.Model):
    """
    Содержит информацию о производителе и названию аромы
    """
    # Название производителя
    aroma_manufacturer = models.CharField(max_length=100)
    # Название аромы
    aroma_name = models.CharField(max_length=100)


class Lure(models.Model):
    """
    Содежит информацию о названии
    производителя и названии прикормки
    """
    # Название производителя прикорки
    lure_manufacturer = models.CharField(max_length=100)
    # Название прикормки
    lure_name = models.CharField(max_length=100)


class Fishing_Tackle(models.Model):
    """
    Содержит информацию о снасти: донная, поплавочная и т.д.
    """
    # Привязка к рыбалке
    fishing = models.ForeignKey(Fishing, on_delete=models.CASCADE)
    # Инормация о используемой снасти
    fishing_tackle_name = models.CharField(max_length=30)


class nozzle(models.Model):
    """
    Сожердит информацию о наживках/насадках
    При bait=True наживка (поле nozzle_manufacturer
    неактивно) иначе насадка
    """
    # True наживка иначе насадка
    bait = models.BooleanField(default=False)
    # Производитель насадки
    nozzle_manufacturer = models.CharField(max_length=100)
    # Название насадки/наживки
    nozzle_name = models.CharField(max_length=100)


class District(models.Model):
    """
    Содержит информацию о районе рыбалки
    """
    # Название района
    district_name = models.CharField(max_length=50)
