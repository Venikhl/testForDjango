from django.shortcuts import render
from django.http import HttpResponse


# Function for getting main page.
def main_page(request):
    return render(request, 'home/page.html')

