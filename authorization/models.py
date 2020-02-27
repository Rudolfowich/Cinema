from django.db import models
from django.contrib.auth.models import AbstractUser


# Расширение модели стандартного пользователя с добавлением нескольких полей.
class User(AbstractUser):
    image = models.ImageField(verbose_name="Аватарка", default='default.jpg', upload_to='profile_pics')
    money = models.PositiveIntegerField(verbose_name="Деньги", help_text="Сколько денег добавить пользователю?",
                                        blank=True, null=True)
    sum_all = models.IntegerField(default=0, blank=True)
