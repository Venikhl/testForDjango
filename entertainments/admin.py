from django.contrib import admin
from .models import Book, Movie, TVSeries, Progress

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'total_pages', 'rating', 'genre', 'publication_year')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'total_minutes', 'rating', 'genre', 'release_year')

@admin.register(TVSeries)
class TVSeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'total_episodes', 'rating', 'genre', 'release_year')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'progress_type', 'movie', 'tvseries', 'book', 'minutes_watched', 'episodes_watched', 'pages_read', 'status')
