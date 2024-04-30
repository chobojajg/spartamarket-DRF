from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from .models import Products


class ProductListAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        permissions = super().get_permissions()

        if self.request.method.lower() == 'post':
            permissions.append(IsAuthenticated())

        return permissions

    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['author'] = request.user.id
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, productId):
        return get_object_or_404(Products, pk=productId)

    def get(self, request, productId):
        product = self.get_object(productId)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, productId):
        product = self.get_object(productId)
        if product.author == request.user:
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    def delete(self, request, productId):
        product = self.get_object(productId)
        if product.author == request.user:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
