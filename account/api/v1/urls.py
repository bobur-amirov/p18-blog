from django.urls import path

from .views import UserCreateAPIView, CustomAuthToken

urlpatterns = [
    path('create', UserCreateAPIView.as_view(), name='user_create'),
    path('token', CustomAuthToken.as_view(), name='user_login'),
]