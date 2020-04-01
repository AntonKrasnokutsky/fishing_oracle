from django.db import models

# Create your models here.


class Fishing(models.Model):
    pass


class Fish(models.Model):
    """
    Таблица хранящая в себе информацию о породах рыб,
    в дальнейшем планируется добавление изображение рыб
    """
    name_of_fish = models.CharField(max_length=20)

    def __str__(self):
        return self.name_of_fish


class Fishing_Result(models.Model):
    """
    Содержит информацию о результате рыбалки, принимает
    в себя несколько значений пойманной рыбы
    """
    fishing = models.ForeignKey(Fishing, on_delete=models.CASCADE)
    fish = models.PositiveIntegerField(default=0)
    nuber_of_fish = models.PositiveIntegerField(default=0)
    fish_weight = models.PositiveIntegerField(default=0)


class Fish_Trophy(models.Model):
    fishing = models.ForeignKey(Fishing, on_delete=models.CASCADE)
    fish = models.PositiveIntegerField(default=0)
    fish_trophy_weight = models.PositiveIntegerField(default=0)
#    fish_trophy_photo=models.ImageField()
