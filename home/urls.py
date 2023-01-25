from django.urls import path
from home.views import HomeCreateView, HomeUpdateView, HomeDeleteView

urlpatterns = [
    path('create-card/', HomeCreateView.as_view()),
    path('update-card/<int:pk>/', HomeUpdateView.as_view()),
    path('delete-card/<int:pk>/', HomeDeleteView.as_view()),
]