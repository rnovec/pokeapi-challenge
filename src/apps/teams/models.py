from django.db import models

from apps.core.models import BaseModel


class Team(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    trainer = models.ForeignKey(
        "trainers.Trainer", on_delete=models.SET_NULL, related_name="teams", null=True
    )

    def __str__(self):
        return self.name
