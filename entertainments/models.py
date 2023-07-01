from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100, null=True)
    total_minutes = models.PositiveIntegerField()
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=100, null=True)
    release_year = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    description = models.TextField(null=True)

class TVSeries(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100, null=True)
    total_episodes = models.PositiveIntegerField()
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=100, null=True)
    release_year = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='tvseries/', null=True, blank=True)
    description = models.TextField(null=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    total_pages = models.PositiveIntegerField()
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=100, null=True)
    publication_year = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    description = models.TextField(null=True)



class Progress(models.Model):
    PROGRESS_TYPE_CHOICES = (
        ('movie', 'Movie'),
        ('tvseries', 'TV Series'),
        ('book', 'Book'),
    )

    STATUS_CHOICES = (
        ('favorite', 'Favorite'),
        ('watching_reading', 'Watching/Reading'),
        ('completed', 'Completed'),
        ('abandoned', 'Abandoned'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    progress_type = models.CharField(max_length=8, choices=PROGRESS_TYPE_CHOICES)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    tvseries = models.ForeignKey(TVSeries, on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, blank=True)
    minutes_watched = models.PositiveIntegerField(default=0)
    episodes_watched = models.PositiveIntegerField(default=0)
    pages_read = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='watching_reading')

    def save(self, *args, **kwargs):
        if self.progress_type == 'movie':
            self.episodes_watched = 0
            self.pages_read = 0
        elif self.progress_type == 'tvseries':
            self.minutes_watched = 0
            self.pages_read = 0
        elif self.progress_type == 'book':
            self.minutes_watched = 0
            self.episodes_watched = 0

        super().save(*args, **kwargs)
