from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'index.html')


def recommend(request):
    books = [
        {'title': 'The Girl on the Train', 'cover_url': 'https://example.com/cover1.jpg'},
        {'title': 'The Great Gatsby', 'cover_url': 'https://example.com/cover2.jpg'},
        {'title': 'The Catcher in the Rye', 'cover_url': 'https://example.com/cover3.jpg'},
        {'title': 'The Hitchhiker\'s Guide', 'cover_url': 'https://example.com/cover4.jpg'},
        {'title': 'The Da Vinci Code', 'cover_url': 'https://example.com/cover5.jpg'},
        {'title': 'The Alchemist', 'cover_url': 'https://example.com/cover6.jpg'},
    ]
    return render(request, 'recommend.html', {'books': books})

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
def last_read_search(request):
    if request.method == 'POST':
        # Bu yerda foydalanuvchi kiritgan kitob nomlarini o‘qish mumkin
        title1 = request.POST.get('title1')
        title2 = request.POST.get('title2')
        title3 = request.POST.get('title3')
        # TODO: Bu yerda tavsiya logikasini yozing
        books = [
            {'title': f'Similar to {title1}', 'cover_url': 'https://via.placeholder.com/150'},
            {'title': f'Similar to {title2}', 'cover_url': 'https://via.placeholder.com/150'},
        ]
        return render(request, 'recommend.html', {'books': books})
    return render(request, 'recommend.html', {'books': []})