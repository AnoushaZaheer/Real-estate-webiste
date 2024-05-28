# listings/views.py
from django.shortcuts import render
from .models import Home

def home_list(request):
    homes = Home.objects.all()
    return render(request, 'home_list.html', {'homes': homes})
