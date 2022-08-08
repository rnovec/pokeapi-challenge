from rest_framework import viewsets

from .models import Trainer
from .serializers import TrainerSerializer


# Create your views here.
class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
