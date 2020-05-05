from django.shortcuts import render
from .models import * 

# Create your views here.
def notes(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'storage/notes.html', context)