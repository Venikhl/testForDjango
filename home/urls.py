from django.urls import path
from . import views

urlpatterns = [
    # Path for getting main page
    path('', views.main_page, name='main_page'),
]