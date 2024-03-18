from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from app.models import Category, Blog
from .serializers import CategorySerializer, BlogCreateSerializer, BlogUpdateSerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]


@api_view(http_method_names=['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def blog_create(request):
    serializer = BlogCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author = request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(http_method_names=['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    serializer = BlogUpdateSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
