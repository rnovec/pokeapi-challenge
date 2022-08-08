from rest_framework import routers

from apps.pokemons.views import PokemonViewSet
from apps.teams.views import TeamViewSet
from apps.trainers.views import TrainerViewSet

router = routers.DefaultRouter()

router.register(r"pokemons", PokemonViewSet)
router.register(r"trainers", TrainerViewSet)
router.register(r"teams", TeamViewSet)
