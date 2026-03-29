from rest_framework import generics
from .models import Gun, Category
from .serializers import GunSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class GunListAPIView(generics.ListCreateAPIView):
    queryset = Gun.objects.all()
    serializer_class = GunSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GunDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gun.objects.all()
    serializer_class = GunSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'