from django.shortcuts import render
from .models import * 

# Create your views here.
def index(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'storage/index.html', context)

def fridgeitems(request):
    items = FridgeItem.objects.all()
    context = {'items': items}
    return render(request, 'storage/fridgeItems.html', context)