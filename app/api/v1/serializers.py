from rest_framework import serializers

from app.models import Category, Blog

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category']


class BlogUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'description']





