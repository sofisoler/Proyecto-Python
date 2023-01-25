from django.urls import path
from products.views import list_products, list_face, list_body, admin_products, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

urlpatterns = [
    path('list-products/', list_products),
    path('list-face/', list_face),
    path('list-body/', list_body),
    path('admin-products/', admin_products),
    path('create-product/', ProductCreateView.as_view()),
    path('update-product/<int:pk>/', ProductUpdateView.as_view()),
    path('delete-product/<int:pk>/', ProductDeleteView.as_view()),
    path('detail-product/<int:pk>/', ProductDetailView.as_view()),
]