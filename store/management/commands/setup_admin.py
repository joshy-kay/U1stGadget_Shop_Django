from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Category, Product

class Command(BaseCommand):
    help = 'Set up initial admin user and seed basic data'

    def handle(self, *args, **options):
        # Create admin user if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(
                self.style.SUCCESS('Admin user created: admin/admin123')
            )
        else:
            self.stdout.write('Admin user already exists')

        # Create basic categories if they don't exist
        categories_data = [
            {'name': 'Phones', 'description': 'Mobile phones and smartphones'},
            {'name': 'Laptops', 'description': 'Laptops and notebooks'},
            {'name': 'Accessories', 'description': 'Phone and computer accessories'},
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )

        self.stdout.write(self.style.SUCCESS('Setup complete!'))