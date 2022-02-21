import factory
from pokedex_app.test.factories import PokedexCharmeleonFactory


class PokemonCharmeleonFactory(factory.django.DjangoModelFactory):
    """pokemon factory"""

    pokedex_creature_id = factory.SubFactory(PokedexCharmeleonFactory)
    trainer_id = None
    surname = "mycharmeleon"
    level = 1
    experience = 10

    class Meta:
        model = "pokemon.Pokemon"  # Equivalent to ``model = myapp.models.User``
