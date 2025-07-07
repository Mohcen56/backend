# Gold Products API

This project is a Django REST API for managing and retrieving gold product data, including dynamic price calculation based on real-time gold prices.

## Features

- List all products with images, weight, popularity score, and dynamic price in USD
- Price is calculated as: `(popularity_score + 1) * weight * gold_price_per_gram`
- Gold price is fetched in real-time from an external API and cached for performance
- Admin interface for managing products

## Project Structure

```text
backend/
    backend/           # Django project settings and URLs
    products/          # App for product models, views, serializers, utils
        models.py      # Product model
        serializers.py # ProductSerializer with dynamic price
        views.py       # API views
        utils.py       # Gold price fetching logic
        urls.py        # App URL routing
    db.sqlite3         # SQLite database
    manage.py          # Django management script
    products.json      # Sample product data for import
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone <https://github.com/Mohcen56/backend.git>
cd backend
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Add a `.env` file in the project root with your gold price API key

```env
GOLD_API_KEY=your_actual_gold_api_key
```

### 4. Run migrations and load initial data

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py load_products  # Or use the custom management command
```

### 5. Run the development server

```bash
python manage.py runserver
```

### 6. Access the API

- List products: `GET /api/products/`
- Admin: `http://localhost:8000/admin/`

## API Endpoints

- `GET /api/products/` — List all products with dynamic price and rating

## Gold Price Source

- Gold price is fetched from [goldapi.io](https://www.goldapi.io/) using your API key
- Price is cached for 10 minutes to reduce API calls

## Custom Management Command

- `python manage.py load_products` — Loads products from `products.json` into the database

## Requirements

- Python 3.10+
- Django 5.x
- djangorestframework
- python-decouple
- requests


