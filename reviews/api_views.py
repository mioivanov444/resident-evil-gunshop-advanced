from rest_framework import generics, permissions
from django.core.exceptions import PermissionDenied
from .models import Review, Gun
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        gun_slug = self.kwargs.get('gun_slug')
        return Review.objects.filter(gun__slug=gun_slug)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self):
        review = super().get_object()
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if review.user != self.request.user:
                raise PermissionDenied("You can't modify this review.")
        return review


class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        gun_slug = self.kwargs.get('gun_slug')
        gun = generics.get_object_or_404(Gun, slug=gun_slug)
        serializer.save(user=self.request.user, gun=gun)