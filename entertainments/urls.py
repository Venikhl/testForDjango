from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.entertainments_choice, name='choose-entertainments'),
    path('all/movies', views.all_movies, name='all_movies'),
    path('all/books', views.all_books, name='all_books'),
    path('all/tvseries', views.all_tvseries, name='all_tvseries'),
    path('all/movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('all/books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('all/tvseries/<int:tvseries_id>/', views.tvseries_detail, name='tvseries_detail'),
    path('all/movies/create_progress/', views.create_movie_progress, name='create_movie_progress'),
    path('all/books/create_progress/', views.create_book_progress, name='create_book_progress'),
    path('all/tvseries/create_progress/', views.create_tvseries_progress, name='create_tvseries_progress'),
    path('all/mine/', views.all_my_progress, name='all_my_progress'),
]
