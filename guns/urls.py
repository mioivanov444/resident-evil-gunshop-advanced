from django.urls import path
from .views import (
    GunListView, GunDetailView, GunCreateView, GunUpdateView, GunDeleteView,
    CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
)
from .api_views import GunListAPIView, GunDetailAPIView, CategoryListAPIView, CategoryDetailAPIView

urlpatterns = [
    path('', GunListView.as_view(), name='gun_list'),
    path('create/', GunCreateView.as_view(), name='gun_create'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<slug:slug>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('<slug:slug>/edit/', GunUpdateView.as_view(), name='gun_update'),
    path('<slug:slug>/delete/', GunDeleteView.as_view(), name='gun_delete'),
    path('<slug:slug>/', GunDetailView.as_view(), name='gun_detail'),
]



# DRF API URLs
urlpatterns += [
    path('api/guns/', GunListAPIView.as_view(), name='api_gun_list'),
    path('api/guns/<slug:slug>/', GunDetailAPIView.as_view(), name='api_gun_detail'),

    path('api/categories/', CategoryListAPIView.as_view(), name='api_category_list'),
    path('api/categories/<slug:slug>/', CategoryDetailAPIView.as_view(), name='api_category_detail'),
]