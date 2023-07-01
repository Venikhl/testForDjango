from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.entertainments_choice, name='choose-entertainments'),
    path('all/movies', views.all_movies, name='all_movies')
]
