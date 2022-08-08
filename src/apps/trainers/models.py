from django.contrib.auth.models import User
from django.db import models

from apps.core.models import BaseModel


class Trainer(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="trainer",
    )

    def __str__(self):
        return self.user
