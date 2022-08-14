from django.conf import settings

import requests


class PokemonAPI:
    def get_pokemon(self, name):
        return requests.get(f"{settings.POKEAPI_BASE_URL}/pokemon/{name}/")
