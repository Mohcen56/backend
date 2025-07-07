from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.http import QueryDict

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        # Filtering by popularity score
        min_popularity = request.query_params.get('min_popularity')
        max_popularity = request.query_params.get('max_popularity')
        if min_popularity is not None:
            products = products.filter(popularity_score__gte=float(min_popularity))
        if max_popularity is not None:
            products = products.filter(popularity_score__lte=float(max_popularity))

        # Filtering by price (dynamic, so filter in Python)
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        serializer = ProductSerializer(products, many=True)
        data = serializer.data
        if min_price is not None:
            data = [item for item in data if item['price'] >= float(min_price)]
        if max_price is not None:
            data = [item for item in data if item['price'] <= float(max_price)]
        return Response(data)
# This view handles GET requests to list all products.
# It retrieves all Product instances from the database, serializes them using ProductSerializer, and returns
