from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Post
from .forms import ProductForm, PostForm, CategoryForm

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    recent_posts = Post.objects.order_by('-created_at')[:3]
    
    featured_products = Product.objects.filter(display_category='FEATURED', available=True)
    popular_products = Product.objects.filter(display_category='POPULAR', available=True)
    arrived_products = Product.objects.filter(display_category='ARRIVED', available=True)

    context = {
        'products': products,
        'categories': categories,
        'recent_posts': recent_posts,
        'featured_products': featured_products,
        'popular_products': popular_products,
        'arrived_products': arrived_products,
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def shop(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, "shop.html", context)
def login(request):
    return render(request, "login.html")

def wishlist(request):
    return render(request, "wishlist.html")

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category_detail.html', {'category': category, 'products': products})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

# Dashboard Product CRUD views
def dashboard_index(request):
    products = Product.objects.all().order_by('-created')
    return render(request, 'admin_dashboard/index.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard_index')
    else:
        form = ProductForm()
    context = {
        'form': form,
        'title': 'Add New Product'
    }
    return render(request, 'admin_dashboard/form.html', context)

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard_index')
    else:
        form = ProductForm(instance=product)
    context = {
        'form': form,
        'title': f'Edit {product.name}'
    }
    return render(request, 'admin_dashboard/form.html', context)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard_index')
    return render(request, 'admin_dashboard/delete_confirm.html', {'product': product})

# Dashboard Post CRUD views
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard/post_list.html', {'posts': posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    context = {
        'form': form,
        'title': 'Add New Post'
    }
    return render(request, 'admin_dashboard/form.html', context)

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    context = {
        'form': form,
        'title': f'Edit {post.title}'
    }
    return render(request, 'admin_dashboard/form.html', context)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'admin_dashboard/post_delete_confirm.html', {'post': post})

# Dashboard Category CRUD views
def category_list_dashboard(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'admin_dashboard/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_list_dashboard')
    else:
        form = CategoryForm()
    context = {
        'form': form,
        'title': 'Add New Category'
    }
    return render(request, 'admin_dashboard/form.html', context)

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list_dashboard')
    else:
        form = CategoryForm(instance=category)
    context = {
        'form': form,
        'title': f'Edit {category.name}'
    }
    return render(request, 'admin_dashboard/form.html', context)

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list_dashboard')
    return render(request, 'admin_dashboard/category_delete_confirm.html', {'category': category})
