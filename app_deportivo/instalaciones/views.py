# instalaciones/views.py

from rest_framework import viewsets
from .models import Instalacion
from .serializers import InstalacionSerializer

class InstalacionViewSet(viewsets.ModelViewSet):
    queryset = Instalacion.objects.all()
    serializer_class = InstalacionSerializer
