from django.urls import path, include
from rest_framework import routers

from .views import SpeciesViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'person', PersonViewSet)
router.register(r'species', SpeciesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]