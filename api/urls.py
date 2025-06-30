from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterAPIView, ProductListCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView, ProductBulkCreateAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:product_id>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('products/<int:product_id>/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('products/bulk/', ProductBulkCreateAPIView.as_view(), name='product-bulk-create'),
] 