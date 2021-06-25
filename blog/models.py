from django.db import models
from users.models import CustomUser
from django.utils import timezone


class Post(models.Model):
    class Meta:
        verbose_name='Пост'
        verbose_name_plural='Посты'
    #Владелец записи
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Владелец записи")
    #Тема
    title = models.CharField(
        max_length=200,
        verbose_name='Тема')
    #Краткое описание
    discription = models.TextField(
        default="",
        verbose_name='Краткое содержание')
    #Подробное описание
    text = models.TextField(
        verbose_name='Текст статьи')
    #Дата создания
    created_date = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания')
    #Дата публикации
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата публикации')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
