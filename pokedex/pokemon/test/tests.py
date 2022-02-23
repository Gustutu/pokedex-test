import pytest
from pokemon.models import Pokemon
from pokemon.test.factories import PokemonCharmeleonFactory
from rest_framework.test import APIClient
from pokemon.serializers import PokemonSerializer


@pytest.mark.django_db
def test_charmeleon_factory():
    """test charmeleon factory"""
    PokemonCharmeleonFactory()
    assert Pokemon.objects.all().count() == 1


@pytest.mark.django_db
def test_list_pokemon():
    """test list pokemon"""
    c = APIClient()
    PokemonCharmeleonFactory()
    response = c.get("/pokemon")
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_get_pokemon():
    """test get pokemon"""
    c = APIClient()
    pokemon_charmeleon = PokemonCharmeleonFactory()
    response = c.get("/pokemon/{}".format(pokemon_charmeleon.id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_pokemon():
    """test create pokemon"""
    c = APIClient()
    pokemon_charmeleon = PokemonCharmeleonFactory()
    serializer = PokemonSerializer(instance=pokemon_charmeleon)
    data = serializer.data
    data.pop("id")

    response = c.post("/pokemon", data=data, format="json")
    assert response.status_code == 201


@pytest.mark.django_db
def test_action_give_xp():
    """test action give xp to pokemon"""

    charmeleon = PokemonCharmeleonFactory()
    c = APIClient()
    response = c.post(
        "/pokemon/{}/give_xp".format(charmeleon.id),
        data={"experience": 20},
        format="json",
    )
    assert response.status_code == 200
