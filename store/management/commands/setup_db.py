from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.management.commands.seed_gadgets import Command as SeedCommand


class Command(BaseCommand):
    help = 'Setup database with initial data and admin user'

    def handle(self, *args, **options):
        # Run the seed command first
        seed_command = SeedCommand()
        seed_command.handle(*args, **options)

        # Create admin user if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Created admin user: admin/admin123'))
        else:
            self.stdout.write(self.style.SUCCESS('Admin user already exists'))

        self.stdout.write(self.style.SUCCESS('Database setup complete'))