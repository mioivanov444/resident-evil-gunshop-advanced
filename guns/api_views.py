from rest_framework import generics, status
from .models import Gun, Category
from .serializers import GunSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import send_welcome_email
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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


@method_decorator(csrf_exempt, name='dispatch')
class SendEmailAPIView(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if not email:
            return Response(
                {"error": "Email field is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            send_welcome_email(email)
        except Exception as e:
            return Response(
                {"error": f"Failed to send email: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {"message": "Email sent successfully."},
            status=status.HTTP_200_OK
        )