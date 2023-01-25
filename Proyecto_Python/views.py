from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from home.models import Card

def index(request):
    cards = Card.objects.all()
    context = {
        "cards": cards,
    }
    return render(request, "index.html", context=context)

def about(request):
    return render(request, "about.html", context={})

@login_required
def location(request):
    return render(request, "location.html", context={})