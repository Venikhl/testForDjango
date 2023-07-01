from django.shortcuts import render

# Create your views here.
from .models import Book, TVSeries, Movie


def entertainments_choice(request):
    return render(request, 'entertainments/entertainments_choice.html')

# def all_entertainments(request):
#     book_list = Book.objects.all()
#     tvseries_list = Book.objects.all()
#     movies_list = Book.objects.all()
#     return render(request, 'entertainments/entertainments_choice.html',
#                   {'book_list': book_list,
#                    'tvseries_list': tvseries_list,
#                    'movies_list': movies_list})
