from django.shortcuts import redirect, render
from lists.models import Item
from django.http import HttpResponse

# Create your views here.
# Info on render request extra args in
# https://www.obeythetestinggoat.com/book/chapter_post_and_database.html
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})