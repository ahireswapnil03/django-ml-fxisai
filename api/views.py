from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product
from .serializers import ProductSerializer, UserRegisterSerializer

# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductDeleteAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'product_id'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductBulkCreateAPIView(generics.GenericAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        products_data = request.data.get('products', [])
        created = []
        for product_data in products_data:
            product_data.pop('user', None)  # Ensure user is not set from client
            serializer = self.get_serializer(data=product_data)
            serializer.is_valid(raise_exception=True)
            created.append(serializer.save(user=request.user))
        return Response(ProductSerializer(created, many=True).data, status=status.HTTP_201_CREATED)
