import factory


class PokedexCharmeleonFactory(factory.django.DjangoModelFactory):
    name = 'Charmeleon'
    type_1= 'Fire'
    type_2 = None
    total = 405 
    hp = 58
    attack = 64
    defense = 58
    sp_attack  =80
    sp_defense = 65
    speed =  80
    generation = 1
    legendary = False
    
    class Meta:
        model = 'pokedex_app.Pokedex'  # Equivalent to ``model = myapp.models.User``
