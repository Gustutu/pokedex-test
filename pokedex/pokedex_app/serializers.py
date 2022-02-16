from rest_framework import serializers
from pokedex_app.models import Pokedex


class PokedexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokedex
        fields = '__all__'
