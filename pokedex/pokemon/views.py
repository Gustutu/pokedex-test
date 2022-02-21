from rest_framework import viewsets
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    """model viewset on pokemon"""

    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
