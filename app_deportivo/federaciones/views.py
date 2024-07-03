# federaciones/views.py

from urllib import response
from rest_framework import viewsets
from .models import Federacion
from .serializers import FederacionSerializer
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Federacion
from .serializers import FederacionSerializer

class FederacionViewSet(viewsets.ModelViewSet):
    queryset = Federacion.objects.all()
    serializer_class = FederacionSerializer

