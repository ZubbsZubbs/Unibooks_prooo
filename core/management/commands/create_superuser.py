from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a superuser automatically'

    def handle(self, *args, **options):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('budingtech', 'thankgodazubuike@gmail.com', '1789')
            self.stdout.write(self.style.SUCCESS('Successfully created a new superuser'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists.'))






