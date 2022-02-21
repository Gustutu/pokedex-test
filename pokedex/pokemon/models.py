from django.db import models
from django.db.models import OneToOneField, CharField, IntegerField, ForeignKey
from trainer.models import Trainer

# Create your models here.


class Pokemon(models.Model):
    """Pokemon Model"""

    # _id should be only in serializer only
    pokedex_creature_id = ForeignKey("pokedex_app.Pokedex", on_delete=models.PROTECT)
    trainer_id = OneToOneField(to=Trainer, on_delete=models.PROTECT, null=True)
    surname = CharField(max_length=50)
    level = IntegerField()
    experience = IntegerField()
