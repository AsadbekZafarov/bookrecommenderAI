# gemini_utils.py
import google.generativeai as genai
from django.conf import settings
import json
import re

genai.configure(api_key=settings.GEMINI_API_KEY)

import requests

def fetch_book_info_from_google(title):
    url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            book = data['items'][0]['volumeInfo']
            return {
                'Title': book.get('title'),
                'Author': ', '.join(book.get('authors', [])),
                'Description': book.get('description', 'No description available.'),
                'Image_Url': book.get('imageLinks', {}).get('thumbnail', '')
            }
    #     {
    #     "model": "app.Books_seller",  # Replace 'app' with your actual app name
    #     "fields": {
    #         'Title': book.get('title'),
    #         'Author': ', '.join(book.get('authors', [])),
    #         'Description': book.get('description', 'No description available.'),
    #         'Image_Url': book.get('imageLinks', {}).get('thumbnail', '')
    #     }
    # }
    return None

def get_gemini_recommendation(prompt_text):
    model = genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content(prompt_text)

    text = response.text.strip()
    text = text.replace("```json", "").replace("```", "").strip()
    match = re.search(r'\[.*\]', text, re.DOTALL)

    recommendations = []
    if match:
        try:
            books = json.loads(match.group(0))
            for book in books:
                info = fetch_book_info_from_google(book['Title'])
                if info:
                    recommendations.append(info)
        except json.JSONDecodeError as e:
            print("❌ JSON parse error:", e)
    return recommendations

# import pandas as pd
# df = pd.read_csv('core/books_seller.csv')
# books_best_seller = []
# for i in df['Title']:
#     books_best_seller.append(fetch_book_info_from_google(i))

# df = pd.DataFrame(books_best_seller)
# df.to_json('core/books_best_seller.json', orient='records', lines=True)
