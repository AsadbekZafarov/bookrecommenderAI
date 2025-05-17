from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import get_gemini_recommendation
import json
from .models import Book, Books_seller
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

def best_sellers(request):
    books = Books_seller.objects.all()
    return render(request, 'best_seller.html', {'books': books})

def home(request):
    best_sellers= Books_seller.objects.all()
    return render(request, 'home.html', {'best_sellers': best_sellers})

@login_required(login_url='login')
def recommend(request):
    return render(request, 'recommend.html')

# @login_required(login_url='login')
def book_detail(request, book_id):
    book = get_object_or_404(Books_seller, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

@csrf_exempt
def filter_search(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # TODO: bu yerda filtering logikasini yozing
        books = [
            {'title': 'Filtered Book 1', 'cover_url': 'https://via.placeholder.com/150'},
            {'title': 'Filtered Book 2', 'cover_url': 'https://via.placeholder.com/150'},
        ]
        return render(request, 'recommend.html', {'books': books})
    return render(request, 'recommend.html', {'books': []})

@csrf_exempt


def by_ai(request):
    if request.method == 'POST':
        title1 = request.POST.get('title1')
        title2 = request.POST.get('title2')
        title3 = request.POST.get('title3')
        genre = request.POST.get('genre')

        prompt = f"""
        I recently read the following books: "{title1}", "{title2}", and "{title3}" from the {genre} genre.
        Please recommend 8 books that are similar in style. For each, include:

        - Title
        - Author
        - Description
    Do NOT include explanations or text before or after. Just return the JSON array inside triple backticks like this:
        ```json
        [
            {{
            "Title": "Book Title",
            "Author": "Author Name",
            "Description": "Short description...",
                }}, 
            ]
        ```
        """

        books = get_gemini_recommendation(prompt)
        return render(request, 'recommend.html', {'books': books})
  # Modelingizni moslashtiring
# def country_books(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         country = data.get('country')
#         if country:
#             books = get_books_by_country(country)
#         else:
#             books = get_books_by_country('Uzbekistan')
#         return JsonResponse({'books': books})
    # if request.method == 'GET':
    #     country = 'Uzbekistan'
    #     books = get_books_by_country(country)
    #     return JsonResponse({'books': books})
    # return JsonResponse({'error': 'Invalid request'}, status=400)   