import pytest
from pokemon.models import Pokemon
from pokemon.test.factories import PokemonCharmeleonFactory
from rest_framework.test import APIClient
from pokemon.serializers import PokemonSerializer
from rest_framework.renderers import JSONRenderer



@pytest.mark.django_db
def test_charmeleon_factory():
    charmeleon = PokemonCharmeleonFactory()
    assert Pokemon.objects.all().count() == 1


@pytest.mark.django_db
def test_list_pokemon():
    c = APIClient()
    PokemonCharmeleonFactory()
    response = c.get('/pokemon')
    assert response.status_code == 200
    assert len(response.data)==1



@pytest.mark.django_db
def test_get_pokemon():
    c = APIClient()
    pokemon_charmeleon = PokemonCharmeleonFactory()
    response = c.get('/pokemon/{}'.format(pokemon_charmeleon.id))
    assert response.status_code == 200



@pytest.mark.django_db
def test_create_pokemon():
    c = APIClient()
    pokemon_charmeleon = PokemonCharmeleonFactory()
    serializer = PokemonSerializer(instance=pokemon_charmeleon)
    data = serializer.data
    data.pop('id')
    
    response = c.post('/pokemon',data = data,format = 'json')
    assert response.status_code == 201