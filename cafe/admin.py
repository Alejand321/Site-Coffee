from django.contrib import admin
from .models import Cafe

class cafeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'cantidad')
admin.site.register(Cafe, cafeAdmin)
