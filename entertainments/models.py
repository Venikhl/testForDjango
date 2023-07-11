# Page for creating all the tables (and connections between them) in the database.
from django.db import models
from django.contrib.auth.models import User


# Movie model for database.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100, null=True)
    total_minutes = models.PositiveIntegerField()
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=100, null=True)
    release_year = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    description = models.TextField(null=True)


# TV Series model for database.
class TVSeries(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100, null=True)
    total_episodes = models.PositiveIntegerField()
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=100, null=True)
    release_year = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='tvseries/', null=True, blank=True)
    description = models.TextField(null=True)


# Episode model for database.
class Episode(models.Model):
    title = models.CharField(max_length=100)
    tvseries = models.ForeignKey(TVSeries, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='episodes/', null=True, blank=True)
    description = models.TextField(null=True)
    release_date = models.DateField(null=True)


# Book model for database.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True)
    total_pages = models.PositiveIntegerField()
    rating = models.FloatField(default=0)
    genre = models.CharField(max_length=100, null=True)
    publication_year = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='books/', null=True, blank=True)
    description = models.TextField(null=True)


# Progress model for database.
class Progress(models.Model):
    # Available types of entertainments to store in Progress model.
    # User can choose one of them in a single Progress object.
    PROGRESS_TYPE_CHOICES = (
        ('movie', 'Movie'),
        ('tvseries', 'TV Series'),
        ('book', 'Book'),
    )

    # Possible status list for a Progress model. User can choose one of them in a single Progress object.
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

    # Can be used in future work. Used to store how many minutes of a movie a concrete user watched.
    minutes_watched = models.PositiveIntegerField(default=0)

    # Can be used in future work. Used to store how many episodes of a TV series a concrete user watched.
    episodes_watched = models.ManyToManyField(Episode, blank=True)

    # Can be used in future work. Used to store how many pages of a book a concrete user watched.
    pages_read = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='watching_reading')

    # Function for making sure that user cannot choose illegal progress in a concrete progress type.
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
