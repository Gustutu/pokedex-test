# Generated by Django 4.0.2 on 2022-02-15 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pokedex_app', '0001_initial'),
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('pokedex_creature_id', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='pokedex_app.pokedex')),
                ('trainer_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='trainer.trainer')),
            ],
        ),
    ]
