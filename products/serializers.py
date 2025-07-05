from rest_framework import serializers

from products.models import Product
class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'popularity_score',
            'weight',
            'image_yellow',
            'image_rose',
            'image_white',
            'price',
            'rating'
        ]

    def get_price(self, obj):
        from .utils import get_gold_price_per_gram
        gold_price = get_gold_price_per_gram()
        return round((obj.popularity_score + 1) * obj.weight * gold_price)

    def get_rating(self, obj):
        return round(obj.popularity_score * 5, 1)

