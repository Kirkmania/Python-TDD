from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Info on render request extra args in
# https://www.obeythetestinggoat.com/book/chapter_post_and_database.html
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })