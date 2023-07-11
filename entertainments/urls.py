from django.urls import path
from . import views

urlpatterns = [
    # Getting page for choosing the type of entertainment. (Books, Movies, TV Series)
    path('all/', views.entertainments_choice, name='choose-entertainments'),

    # Getting with all available movies listed
    path('all/movies', views.all_movies, name='all_movies'),
    # Getting with all available books listed
    path('all/books', views.all_books, name='all_books'),
    # Getting with all available TV series listed
    path('all/tvseries', views.all_tvseries, name='all_tvseries'),

    # Page for visualising information about concrete movie
    path('all/movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    # Page for visualising information about concrete book
    path('all/books/<int:book_id>/', views.book_detail, name='book_detail'),
    # Page for visualising information about concrete TV series
    path('all/tvseries/<int:tvseries_id>/', views.tvseries_detail, name='tvseries_detail'),

    # Path for creating an object of "Progress" to a concrete movie
    path('all/movies/create_progress/', views.create_movie_progress, name='create_movie_progress'),
    # Path for creating an object of "Progress" to a concrete book
    path('all/books/create_progress/', views.create_book_progress, name='create_book_progress'),
    # Path for creating an object of "Progress" to a concrete TV series
    path('all/tvseries/create_progress/', views.create_tvseries_progress, name='create_tvseries_progress'),

    # Getting page with all progress objects that a concrete user has
    path('all/mine/', views.all_my_progress, name='all_my_progress'),

    # Path for getting information about a concrete episode corresponding to a concrete TV series
    path('all/episodes/<int:episode_id>/', views.episode_detail, name='episode_detail'),

    # Path for creating an object of a concrete episode of a concrete TV series object in the "Progress" table
    path('all/episodes/create_progress/', views.create_episode_progress, name='create_episode_progress'),
    # Path for deleting an object of a concrete episode of a concrete TV series object in the "Progress" table
    path('all/episodes/remove_progress/', views.remove_episode_progress, name='remove_episode_progress'),
]
