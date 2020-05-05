from django.shortcuts import render
from .models import * 

# Create your views here.
def notes(request):

    return render(request, 'storage/notes.html',{})