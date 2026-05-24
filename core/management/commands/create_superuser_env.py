import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a superuser from environment variables'

    def handle(self, *args, **options):
        User = get_user_model()
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', email)
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not email or not password:
            self.stderr.write('Set DJANGO_SUPERUSER_EMAIL and DJANGO_SUPERUSER_PASSWORD env vars.')
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write('Superuser already exists. Skipping.')
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.stdout.write(self.style.SUCCESS(f'Superuser "{email}" created successfully.'))
