import pytest
from pokedex_app.test.factories import PokedexCharmeleonFactory
from pokedex_app.models import Pokedex
from rest_framework.test import APIClient
@pytest.mark.django_db
def test_charmeleon_factory():
    charmeleon = PokedexCharmeleonFactory()
    assert Pokedex.objects.all().count() == 1


@pytest.mark.django_db
def test_list_pokedex():
    PokedexCharmeleonFactory()
    PokedexCharmeleonFactory()
    c = APIClient()
    response = c.get('/pokedex')
    assert response.status_code == 200
    assert len(response.data)==2


@pytest.mark.django_db
def test_get_pokedex():
    charmeleon = PokedexCharmeleonFactory()
    PokedexCharmeleonFactory()
    c = APIClient()
    response = c.get('/pokedex/{}'.format(charmeleon.id))
    assert response.status_code == 200

@pytest.mark.django_db
def test_list_pokedex():
    PokedexCharmeleonFactory()
    PokedexCharmeleonFactory(type_1='Grass')
    c = APIClient()
    response = c.get('/pokedex?type_1=Grass')
    assert response.status_code == 200
    assert len(response.data)==1




