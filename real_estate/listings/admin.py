# listings/admin.py
from django.contrib import admin
from .models import Home

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'num_rooms', 'num_bathrooms', 'num_kitchens', 'address', 'price')
