from rest_framework import viewsets, status
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer, AddXpSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    """model viewset on pokemon"""

    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @action(detail=True, methods=["post"])
    def give_xp(self, request, pk=None):
        """action to give pokemon some more xp"""
        serializer = AddXpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pokemon = self.get_object()
        pokemon.add_xp(serializer.validated_data["experience"])
        pokemon.save()
        return Response(
            {
                "status": "xp added",
            },
            status=status.HTTP_200_OK,
        )
