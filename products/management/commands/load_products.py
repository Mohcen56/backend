import json
from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load products from products.json'

    def handle(self, *args, **kwargs):
        with open('products.json') as f:
            data = json.load(f)
            for item in data:
                Product.objects.create(
                    name=item['name'],
                    popularity_score=item['popularityScore'],
                    weight=item['weight'],
                    image_yellow=item['images']['yellow'],
                    image_rose=item['images']['rose'],
                    image_white=item['images']['white'],
                )
        self.stdout.write(self.style.SUCCESS('Products loaded successfully!'))
# This command reads a JSON file named 'products.json' and creates Product instances in the database.