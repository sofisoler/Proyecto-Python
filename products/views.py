from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from products.models import Product

def list_products(request):
    if "search" in request.GET:
        search = request.GET["search"]
        products = Product.objects.filter(nombre__icontains=search)
    else:
        products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products/list_products.html", context=context)

def list_face(request):
    face = Product.objects.filter(categoria__icontains="face")
    context = {
        "face": face
    }
    return render(request, "products/list_face.html", context=context)

def list_body(request):
    body = Product.objects.filter(categoria__icontains="body")
    context = {
        "body": body
    }
    return render(request, "products/list_body.html", context=context)

@login_required
def admin_products(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "products/admin_products.html", context=context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail_product.html'
    fields = "__all__"

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'products/create_product.html'
    fields = "__all__"
    success_url = '/products/admin-products/'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'products/update_product.html'
    fields = "__all__"
    success_url = '/products/admin-products/'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = '/products/admin-products/'