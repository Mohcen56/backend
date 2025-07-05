import requests
from django.core.cache import cache
from django.conf import settings

def get_gold_price_per_gram():
    cached_price = cache.get('gold_price_per_gram')
    if cached_price:
        return cached_price

    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": settings.GOLD_API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code != 200 or 'price' not in data:
            raise Exception('Invalid response from gold API')

        price_per_ounce = data['price']
        price_per_gram = price_per_ounce / 31.1035

        # Cache it for 10 minutes
        cache.set('gold_price_per_gram', price_per_gram, timeout=600)

        return price_per_gram

    except Exception as e:
        # Handle failures (fallback or error)
        print(f"Error fetching gold price: {e}")
        return 60  # fallback default price per gram (USD)
