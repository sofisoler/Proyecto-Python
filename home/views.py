from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from home.models import Card

class HomeCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = 'home/create_card.html'
    fields = "__all__"
    success_url = '/'

class HomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    template_name = 'home/update_card.html'
    fields = "__all__"
    success_url = '/'

class HomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = 'home/delete_card.html'
    success_url = '/'