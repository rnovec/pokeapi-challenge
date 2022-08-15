from django.db import models

from apps.core.models import BaseModel


class Pokemon(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    team = models.ForeignKey(
        "teams.Team", on_delete=models.SET_NULL, related_name="pokemons", null=True
    )
    additional_data = models.JSONField(default=dict)

    def __str__(self):
        return self.name
