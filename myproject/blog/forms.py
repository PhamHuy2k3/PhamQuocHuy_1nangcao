from django import forms
from .models import Product, Post, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'slug',
            'image',
            'description',
            'price',
            'available',
            'display_category',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'category',
            'title',
            'slug',
            'author',
            'content',
            'image',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']
