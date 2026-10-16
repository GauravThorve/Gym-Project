
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create or update the deployment admin account"

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_ADMIN_USERNAME")
        password = os.environ.get("DJANGO_ADMIN_PASSWORD")

        if not username or not password:
            raise CommandError(
                "DJANGO_ADMIN_USERNAME and DJANGO_ADMIN_PASSWORD "
                "must be configured."
            )

        User = get_user_model()
        login_field = User.USERNAME_FIELD

        user, created = User._default_manager.get_or_create(
            **{login_field: username}
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        action = "Created" if created else "Updated"
        self.stdout.write(
            self.style.SUCCESS(
                f"{action} deployment admin account."
            )
        )
