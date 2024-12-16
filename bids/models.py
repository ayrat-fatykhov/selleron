from django.db import models


class Bid(models.Model):
    """
    Определяет поля для модели Заявка
    """
    STATUS_CHOICES = [
        ('1', 'создана'),
        ('2', 'товар передан в доставку'),
        ('3', 'товар доставлен'),
    ]

    title = models.CharField(max_length=255, verbose_name='наименование')
    state = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1', verbose_name='статус')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Заявка
        """
        return f'{self.title} - {self.state}'

    class Meta:
        """
        Определяет отображение модели Заявка в админке. Сортирует по порядковому номеру
        """
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'
        ordering = ('pk',)
