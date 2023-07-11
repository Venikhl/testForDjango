from django.urls import path
from . import views

urlpatterns = [
    # Path for registering a user.
    path('register_user/', views.register_user, name='register'),

    # Path for logging in a user.
    path('login_user/', views.login_user, name='login'),

    # Path for logging out a user.
    path('logout_user/', views.logout_user, name='logout')
]
