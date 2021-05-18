from django.shortcuts import render
from .models import Item
# Create your views here.


def item_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, "home-page.html", context)
