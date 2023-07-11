from .models import Book, TVSeries, Movie, Progress, Episode
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


# Getting page for choosing entertainment page to view
def entertainments_choice(request):
    return render(request, 'entertainments/entertainments_choice.html')


# Getting list of all available movies
def all_movies(request):
    movies_list = Movie.objects.all()
    return render(request, 'entertainments/movies.html',
                  {'movies_list': movies_list})


# Getting list of all available books
def all_books(request):
    books_list = Book.objects.all()
    return render(request, 'entertainments/books.html',
                  {'books_list': books_list})


# Getting list of all available TV series
def all_tvseries(request):
    tvseries_list = TVSeries.objects.all()
    return render(request, 'entertainments/tvseries.html',
                  {'tvseries_list': tvseries_list})


# Function for getting information about concrete movie
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        progress_element = Progress.objects.get(user=request.user, movie=movie)
    except Progress.DoesNotExist:
        progress_element = "none"
        pass
    return render(request, 'entertainments/movie_detail.html',
                  {'movie': movie, 'progress_element': progress_element})


# Function for getting information about concrete book
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    try:
        progress_element = Progress.objects.get(user=request.user, book=book)
    except Progress.DoesNotExist:
        progress_element = "none"
        pass
    return render(request, 'entertainments/book_detail.html',
                  {'book': book, 'progress_element': progress_element})


# Function for getting information about concrete TV series
def tvseries_detail(request, tvseries_id):
    tvseries = get_object_or_404(TVSeries, pk=tvseries_id)
    try:
        progress_element = Progress.objects.get(user=request.user, tvseries=tvseries)
    except Progress.DoesNotExist:
        progress_element = "none"
        pass
    episodes = Episode.objects.filter(tvseries=tvseries)
    return render(request, 'entertainments/tvseries_detail.html',
                  {'tvseries': tvseries, 'progress_element': progress_element, 'episodes': episodes})


# Function for getting information about a concrete episode corresponding to a concrete TV series
def episode_detail(request, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id)
    has_watched = False
    try:
        progress_element = Progress.objects.get(user=request.user, tvseries=episode.tvseries)
        if progress_element.episodes_watched.filter(pk=episode_id).exists():
            has_watched = True
    except Progress.DoesNotExist:
        progress_element = None
        pass

    return render(request, 'entertainments/episode_detail.html',
                  {'episode': episode, 'has_watched': has_watched, 'progress_element': progress_element})


# Function for creating an object of "Progress" to a concrete movie
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


# Function for creating an object of "Progress" to a concrete book
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


# Function for creating an object of "Progress" to a concrete TV series
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


# Function for creating an object of a concrete episode of a concrete TV series object in the "Progress" table
def create_episode_progress(request):
    if request.method == 'POST':
        episode_id = request.POST.get('episode_id')
        user = request.user
        episode = get_object_or_404(Episode, id=episode_id)
        status = request.POST.get('status')
        progress_type = 'tvseries'

        try:
            progress = Progress.objects.get(user=user, tvseries=episode.tvseries)
        except Progress.DoesNotExist:
            progress = Progress.objects.create(user=user, tvseries=episode.tvseries, progress_type=progress_type, status=status)

        progress.episodes_watched.add(episode)
        progress.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


def remove_episode_progress(request):
    if request.method == 'POST':
        episode_id = request.POST.get('episode_id')
        user = request.user
        episode = get_object_or_404(Episode, id=episode_id)

        try:
            progress = Progress.objects.get(user=user, tvseries=episode.tvseries)
            progress.episodes_watched.remove(episode)
            progress.save()
            return JsonResponse({'status': 'success'})
        except Progress.DoesNotExist:
            pass

    return JsonResponse({'status': 'error'})


# Function for deleting an object of a concrete episode of a concrete TV series object in the "Progress" table
def all_my_progress(request):
    progress_list = Progress.objects.all()
    return render(request, 'entertainments/all_my_progress.html', {'progress_list': progress_list})