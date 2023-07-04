from .models import Book, TVSeries, Movie, Progress
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


def entertainments_choice(request):
    return render(request, 'entertainments/entertainments_choice.html')


def all_movies(request):
    movies_list = Movie.objects.all()
    return render(request, 'entertainments/movies.html',
                  {'movies_list': movies_list})


def all_books(request):
    books_list = Book.objects.all()
    return render(request, 'entertainments/books.html',
                  {'books_list': books_list})


def all_tvseries(request):
    tvseries_list = TVSeries.objects.all()
    return render(request, 'entertainments/tvseries.html',
                  {'tvseries_list': tvseries_list})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'entertainments/movie_detail.html', {'movie': movie})


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'entertainments/book_detail.html', {'book': book})


def tvseries_detail(request, tvseries_id):
    tvseries = get_object_or_404(TVSeries, pk=tvseries_id)
    return render(request, 'entertainments/tvseries_detail.html', {'tvseries': tvseries})

def create_movie_progress(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie')
        user = request.user
        movie = Movie.objects.get(id=movie_id)
        status = request.POST.get('status')
        progress_type = request.POST.get('progress_type')

        # Check if a progress object already exists for the movie and user
        try:
            progress = Progress.objects.get(user=user, progress_type=progress_type, movie=movie)
            progress.status = status
            progress.save()
        except Progress.DoesNotExist:
            progress = Progress.objects.create(user=user, movie=movie, progress_type=progress_type, status=status)
            progress.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


def create_book_progress(request):
    if request.method == 'POST':
        book_id = request.POST.get('book')
        user = request.user
        book = Book.objects.get(id=book_id)
        status = request.POST.get('status')
        progress_type = request.POST.get('progress_type')

        # Check if a progress object already exists for the movie and user
        try:
            progress = Progress.objects.get(user=user, progress_type=progress_type, book=book)
            progress.status = status
            progress.save()
        except Progress.DoesNotExist:
            progress = Progress.objects.create(user=user, book=book, progress_type=progress_type, status=status)
            progress.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


def create_tvseries_progress(request):
    if request.method == 'POST':
        tvseries_id = request.POST.get('tvseries')
        user = request.user
        tvseries = TVSeries.objects.get(id=tvseries_id)
        status = request.POST.get('status')
        progress_type = request.POST.get('progress_type')

        # Check if a progress object already exists for the movie and user
        try:
            progress = Progress.objects.get(user=user, progress_type=progress_type, tvseries=tvseries)
            progress.status = status
            progress.save()
        except Progress.DoesNotExist:
            progress = Progress.objects.create(user=user, tvseries=tvseries, progress_type=progress_type, status=status)
            progress.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


def all_my_progress(request):
    progress_list = Progress.objects.all()
    return render(request, 'entertainments/all_my_progress.html', {'progress_list': progress_list})


# def all_entertainments(request):
#     book_list = Book.objects.all()
#     tvseries_list = Book.objects.all()
#     movies_list = Book.objects.all()
#     return render(request, 'entertainments/entertainments_choice.html',
#                   {'book_list': book_list,
#                    'tvseries_list': tvseries_list,
#                    'movies_list': movies_list})
