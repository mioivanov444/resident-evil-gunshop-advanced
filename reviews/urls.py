from django.urls import path
from .views import ReviewCreateView,ReviewUpdateView,ReviewDeleteView


urlpatterns = [
    path('add/<slug:gun_slug>/', ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]
