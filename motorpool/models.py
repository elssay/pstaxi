from django.db import models


class Brand(models.Model):
  title = models.CharField(max_length=100, verbose_name='Название')

  def __str__(self):
    return self.title

  class Meta:
    verbose_name_plural = 'Бренды'
    verbose_name = 'Бренд'

  def __str__(self):
    return self.title

