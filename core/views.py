from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import get_gemini_recommendation
import re



def login(request):
    return render(request, 'login_page.html')
def recommend(request):
    return render(request, 'recommend.html')

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

 