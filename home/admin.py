from django.contrib import admin
from home.models import Card

@admin.register(Card)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')