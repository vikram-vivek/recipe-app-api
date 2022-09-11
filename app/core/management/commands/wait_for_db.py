"""
Django Command to wait for DB to be be available
"""
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the database."""

    def handle(self, *args, **options):
        pass
