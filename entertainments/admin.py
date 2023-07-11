# Page that is needed for showing all the modules in admin panel.
from django.contrib import admin
from .models import Book, Movie, TVSeries, Progress, Episode

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'total_pages', 'rating', 'genre', 'publication_year')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'total_minutes', 'rating', 'genre', 'release_year')

@admin.register(TVSeries)
class TVSeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'total_episodes', 'rating', 'genre', 'release_year')

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'tvseries', 'image', 'description')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'progress_type', 'movie', 'tvseries', 'book', 'get_episodes_watched', 'pages_read', 'status')

    def get_episodes_watched(self, obj):
        return ', '.join([str(episode) for episode in obj.episodes_watched.all()])
    get_episodes_watched.short_description = 'Episodes Watched'
