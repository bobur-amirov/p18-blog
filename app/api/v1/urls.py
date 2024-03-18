from django.urls import path

from .views import CategoryCreateAPIView, blog_create, blog_update


urlpatterns = [
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('blog-create/', blog_create, name='blog_create'),
    path('blog-update/<int:pk>', blog_update, name='blog_update'),
]