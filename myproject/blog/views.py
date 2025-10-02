from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Product, Category, Post
from .forms import ProductForm, PostForm, CategoryForm

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()
        context['recent_posts'] = Post.objects.order_by('-created_at')[:3]
        context['featured_products'] = Product.objects.filter(display_category='FEATURED', available=True)
        context['popular_products'] = Product.objects.filter(display_category='POPULAR', available=True)
        context['arrived_products'] = Product.objects.filter(display_category='ARRIVED', available=True)
        return context

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class ShopListView(ListView):
    model = Product
    template_name = "shop.html"
    context_object_name = 'products'
    paginate_by = 10 

    def get_queryset(self):
        queryset = super().get_queryset().filter(available=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if hasattr(self, 'category'):
            context['category'] = self.category
        return context

class LoginView(TemplateView):
    template_name = "login.html"

class WishlistView(TemplateView):
    template_name = "wishlist.html"

class CartView(TemplateView):
    template_name = "cart.html"

class CheckoutView(TemplateView):
    template_name = "checkout.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'product'

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.object)
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    slug_url_kwarg = 'slug'
    context_object_name = 'post'

# Dashboard Product CRUD views
class DashboardIndexView(ListView):
    model = Product
    template_name = 'admin_dashboard/index.html'
    context_object_name = 'products'
    ordering = ['-created']

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('dashboard_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Product'
        return context

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('dashboard_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit {self.object.name}'
        return context

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admin_dashboard/delete_confirm.html'
    success_url = reverse_lazy('dashboard_index')

# Dashboard Post CRUD views
class PostListView(ListView):
    model = Post
    template_name = 'admin_dashboard/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Post'
        return context

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('post_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit {self.object.title}'
        return context

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'admin_dashboard/post_delete_confirm.html'
    success_url = reverse_lazy('post_list')

# Dashboard Category CRUD views
class CategoryDashboardListView(ListView):
    model = Category
    template_name = 'admin_dashboard/category_list.html'
    context_object_name = 'categories'
    ordering = ['name']

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('category_list_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Category'
        return context

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'admin_dashboard/form.html'
    success_url = reverse_lazy('category_list_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit {self.object.name}'
        return context

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'admin_dashboard/category_delete_confirm.html'
    success_url = reverse_lazy('category_list_dashboard')
