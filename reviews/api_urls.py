from django.urls import path
from .api_views import ReviewListAPIView, ReviewDetailAPIView, ReviewCreateAPIView



urlpatterns = [
    path('reviews/', ReviewListAPIView.as_view(), name='api_review_list'),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='api_review_detail'),
    path('guns/<slug:gun_slug>/reviews/add/', ReviewCreateAPIView.as_view(), name='api_review_create'),
]