from rest_framework import serializers
from pokemon.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    """Pokemon Serializer"""

    class Meta:
        model = Pokemon
        fields = "__all__"


class AddXpSerializer(serializers.Serializer):
    """serializer for extra action give-xp"""

    experience = serializers.IntegerField(min_value=1)
