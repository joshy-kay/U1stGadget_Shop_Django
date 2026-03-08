from django.core.management.base import BaseCommand
from django.utils.text import slugify

from store.models import Category, Product


class Command(BaseCommand):
    help = 'Seed the database with sample categories and products for presentations.'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Phones', 'description': 'Smartphones, feature phones and accessories.'},
            {'name': 'Laptops', 'description': 'Laptops, notebooks and ultrabooks.'},
            {'name': 'Accessories', 'description': 'Chargers, cases, cables and more.'},
            {'name': 'Audio', 'description': 'Headphones, speakers and audio devices.'},
        ]

        created_categories = []
        for cat in categories:
            slug = slugify(cat['name'])
            category, _ = Category.objects.get_or_create(name=cat['name'], defaults={'slug': slug, 'description': cat['description']})
            created_categories.append(category)

        products = [
            {'name': 'Galaxy S Ultra', 'price': '1299.99', 'category': 'Phones', 'description': 'Flagship smartphone with brilliant display.', 'is_featured': True},
            {'name': 'Budget Phone X', 'price': '199.99', 'category': 'Phones', 'description': 'Affordable smartphone with great battery life.', 'is_featured': False},
            {'name': 'ProBook 14', 'price': '899.99', 'category': 'Laptops', 'description': 'Lightweight laptop for professionals.', 'is_featured': True},
            {'name': 'Gaming Beast 17', 'price': '1499.99', 'category': 'Laptops', 'description': 'High performance gaming laptop.', 'is_featured': False},
            {'name': 'FastCharge 30W', 'price': '29.99', 'category': 'Accessories', 'description': 'Fast USB-C charger.', 'is_featured': False},
            {'name': 'NoiseCancel Pro', 'price': '199.99', 'category': 'Audio', 'description': 'Premium noise-cancelling headphones.', 'is_featured': True},
        ]

        created_products = []
        for p in products:
            cat = Category.objects.filter(name=p['category']).first()
            if not cat:
                continue
            slug = slugify(p['name'])
            product, created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    'name': p['name'],
                    'description': p['description'],
                    'price': p['price'],
                    'category': cat,
                    'is_featured': p.get('is_featured', False),
                }
            )
            if not created:
                # update fields to match seed data
                product.name = p['name']
                product.description = p['description']
                product.price = p['price']
                product.category = cat
                product.is_featured = p.get('is_featured', False)
                product.save()

            created_products.append(product)

        self.stdout.write(self.style.SUCCESS(f'Created/updated {len(created_categories)} categories and {len(created_products)} products.'))
