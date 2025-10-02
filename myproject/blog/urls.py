from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("shop/<slug:category_slug>/", views.shop, name="product_list_by_category"),
    path("shop/", views.shop, name="shop"),
    path("login/", views.login, name="login"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

    # Dashboard URLs
    path('dashboard/', views.dashboard_index, name='dashboard_index'),
    path('dashboard/product/add/', views.product_create, name='product_create'),
    path('dashboard/product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('dashboard/product/<int:pk>/delete/', views.product_delete, name='product_delete'),

    # Dashboard Post URLs
    path('dashboard/posts/', views.post_list, name='post_list'),
    path('dashboard/post/add/', views.post_create, name='post_create'),
    path('dashboard/post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('dashboard/post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # Dashboard Category URLs
    path('dashboard/categories/', views.category_list_dashboard, name='category_list_dashboard'),
    path('dashboard/category/add/', views.category_create, name='category_create'),
    path('dashboard/category/<int:pk>/edit/', views.category_update, name='category_update'),
    path('dashboard/category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Dashboard Category URLs
    path('dashboard/categories/', views.category_list_dashboard, name='category_list_dashboard'),
    path('dashboard/category/add/', views.category_create, name='category_create'),
    path('dashboard/category/<int:pk>/edit/', views.category_update, name='category_update'),
    path('dashboard/category/<int:pk>/delete/', views.category_delete, name='category_delete'),
]
