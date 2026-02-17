# Script to load all the data we need from the API
import requests
from django.core.management.base import BaseCommand

from games.models import Game, Shop, Availability

class Command(BaseCommand):
    help = 'Loads the games and offers data from CheapSharkAPI'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Initializing data load from CheapSharkAPI..."))

        # Loading logic

            # Load shops

            # Load offers (Game + Availability)

            # Model.objects.update_or_create(...)

        self.stdout.write(self.style.SUCCESS("Data loaded successfully"))