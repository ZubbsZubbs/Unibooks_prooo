from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model, User

class Command(BaseCommand):
    help = 'Creates a superuser from environment variables'

    def handle(self, *args, **options):
        User = get_user_model()
        username = 'btech'
        password = '1789'
        email = 'thankgodazubuike194@gmail.com'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))
