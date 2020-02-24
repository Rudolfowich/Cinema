from django.db import models


class Movie(models.Model):
    Category = [
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Боевик', 'Боевик'),
        ('Драма', 'Драма'),
        ('Детектив', 'Детектив'),
        ('Фентези', 'Фентези')
    ]
    name = models.CharField(verbose_name="Название", max_length=64, null=False)
    description = models.TextField(verbose_name="Описание", max_length=3000)
    category = models.CharField(verbose_name="Категория", max_length=120, choices=Category)
    poster = models.ImageField(verbose_name="Постер", upload_to='image')
    year = models.PositiveIntegerField(verbose_name="Дата выхода", default=2020)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return f"{self.name}"


class Images(models.Model):
    movie = models.ForeignKey(Movie, verbose_name='Фильм', default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="review/", blank=True)

    def __str__(self):
        return f"{self.movie.name}"


class Session(models.Model):
    name = models.ForeignKey('Movie', on_delete=models.CASCADE)
    room_name = models.ForeignKey('MovieRoom', verbose_name="Название зала", on_delete=models.CASCADE)
    start = models.DateTimeField(verbose_name='Когда начинаем сеанс')
    end = models.DateTimeField(verbose_name='Окончание сеанса')
    price = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self):
        return f"{self.name}"


class MovieRoom(models.Model):
    room_name = models.CharField(max_length=120)
    room_size = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"{self.room_name} - {self.room_size}"
