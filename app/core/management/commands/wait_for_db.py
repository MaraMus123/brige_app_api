"""
Django command to wait for the database to be available.
"""

from django.core.management.base import BaseCommand # type: ignore


class Command(BaseCommand):
    """Django commant to wait for database"""

    def handle(self, *args, **options):
        pass