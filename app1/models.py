import os

from django.db import models

class Profession (models.Model):
    title = models.CharField('Назввание',max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Професcия"
        verbose_name_plural = 'Профессии'

