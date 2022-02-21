from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pokemon.views import PokemonViewSet


router = DefaultRouter(trailing_slash=False)
router.register("pokemon", PokemonViewSet, "pokemon")

urlpatterns = [
    path("", include(router.urls)),
]
