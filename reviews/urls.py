from django.urls import path
from .views import ReviewCreateView,ReviewUpdateView,ReviewDeleteView
from .api_views import ReviewListAPIView, ReviewDetailAPIView, ReviewCreateAPIView


urlpatterns = [
    path('add/<slug:gun_slug>/', ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]

urlpatterns += [
    path('api/reviews/', ReviewListAPIView.as_view(), name='api_review_list'),
    path('api/reviews/<int:pk>/', ReviewDetailAPIView.as_view(), name='api_review_detail'),
    path('api/guns/<slug:gun_slug>/reviews/add/', ReviewCreateAPIView.as_view(), name='api_review_create'),
]