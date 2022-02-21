from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pokedex_app.views import PokedexView


router = DefaultRouter(trailing_slash=False)
router.register("pokedex", PokedexView, "pokedex")

urlpatterns = [
    path("", include(router.urls)),
]
