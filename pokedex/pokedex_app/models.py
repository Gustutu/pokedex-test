from django.db import models

#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary

class Pokedex(models.Model):
    """ pokedex model"""

    # many fields could be enum
    name  = models.CharField(max_length=50)
    type_1 = models.CharField(max_length=50)
    type_2 = models.CharField(max_length=50,null= True)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack =models.IntegerField()
    sp_defense = models.IntegerField()
    speed=models.IntegerField()
    generation  = models.IntegerField()
    legendary  = models.BooleanField()
