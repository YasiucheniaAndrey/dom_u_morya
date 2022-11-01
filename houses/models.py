from django.db import models

class House(models.Model):
    name = models.CharField("Название", max_length=50)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание")