from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("shop/<slug:category_slug>/", views.ShopListView.as_view(), name="product_list_by_category"),
    path("shop/", views.ShopListView.as_view(), name="shop"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("wishlist/", views.WishlistView.as_view(), name="wishlist"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),

    # Dashboard URLs
    path('dashboard/', views.DashboardIndexView.as_view(), name='dashboard_index'),
    path('dashboard/product/add/', views.ProductCreateView.as_view(), name='product_create'),
    path('dashboard/product/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('dashboard/product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # Dashboard Post URLs
    path('dashboard/posts/', views.PostListView.as_view(), name='post_list'),
    path('dashboard/post/add/', views.PostCreateView.as_view(), name='post_create'),
    path('dashboard/post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('dashboard/post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Dashboard Category URLs
    path('dashboard/categories/', views.CategoryDashboardListView.as_view(), name='category_list_dashboard'),
    path('dashboard/category/add/', views.CategoryCreateView.as_view(), name='category_create'),
    path('dashboard/category/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('dashboard/category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
]
