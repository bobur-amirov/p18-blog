from django.urls import path

from .views import CategoryCreateAPIView


urlpatterns = [
    path('category-create/', CategoryCreateAPIView.as_view(), name='category-create')
]