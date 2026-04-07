from django.urls import path
from .api_views import GunListAPIView, GunDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, SendEmailAPIView

urlpatterns = [
    path('guns/', GunListAPIView.as_view(), name='api_gun_list'),
    path('guns/<slug:slug>/', GunDetailAPIView.as_view(), name='api_gun_detail'),

    path('categories/', CategoryListAPIView.as_view(), name='api_category_list'),
    path('categories/<slug:slug>/', CategoryDetailAPIView.as_view(), name='api_category_detail'),

    path('send-email/', SendEmailAPIView.as_view(), name='send_email'),
]