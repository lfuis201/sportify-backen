from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FederacionViewSet

# Definir un router
router = DefaultRouter()
router.register(r'federaciones', FederacionViewSet)

# Incluir las rutas generadas por el router en las rutas de Django
urlpatterns = [
    path('', include(router.urls)),
]
