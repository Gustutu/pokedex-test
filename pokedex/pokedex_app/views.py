from rest_framework.viewsets import ModelViewSet
from pokedex_app.models import Pokedex
from pokedex_app.serializers import PokedexSerializer


class PokedexView(ModelViewSet):
    """pokedex view"""

    queryset = Pokedex.objects.all()
    serializer_class = PokedexSerializer
    filterset_fields = ("type_1", "type_2", "generation", "legendary")
