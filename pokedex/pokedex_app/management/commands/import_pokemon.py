from django.core.management.base import BaseCommand
from pokedex_app.models import Pokedex
import csv


class Command(BaseCommand):
    help = 'add pokedex from csv exemple :  ./manage import_pokedex /home/user/mypathto/filename.csv'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=1, type=str)

    def handle(self, *args, **options):
        print(options['path'][0])
        with open(options['path'][0]) as f:

            pokedexs = []
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                pokedexs.append(
                    Pokedex(name=row[1], type_1=row[2], type_2=row[3],total  =row[4], hp=row[5], attack=row[6], defense=row[7], sp_attack=row[8], sp_defense=row[9], speed=row[10], generation=row[11], legendary=row[12]))

        Pokedex.objects.bulk_create(pokedexs)
        self.stdout.write(self.style.SUCCESS('Success'))
