from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    title = "Neuromedical App"
    return render(request, 'main/main.html', {'title': title})

