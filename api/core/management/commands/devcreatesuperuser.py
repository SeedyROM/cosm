from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Creating a temporary debug admin')
        get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'password123')
        self.stdout.write('Created!')