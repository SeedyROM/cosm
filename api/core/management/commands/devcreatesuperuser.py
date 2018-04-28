from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            self.stdout.write('Creating a temporary debug admin')
            if not get_user_model().objects.filter(username='admin').exists():
                get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'password123')
                self.stdout.write('Created!')
            else:
                self.stdout.write('Already exists!')                
        except:
            pass