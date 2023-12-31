# Generated by Django 4.2.7 on 2023-11-24 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nacionality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Nacionalidad',
                'verbose_name_plural': 'Nacionalidades',
                'db_table': 'nacionalidad',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=20, verbose_name='Apellido')),
                ('player_photo', models.ImageField(null=True, upload_to='images/', verbose_name='Foto del jugador')),
                ('birthdate', models.DateField()),
                ('position_in_which_you_play', models.CharField(max_length=50, verbose_name='Posicion en la que juega')),
                ('jersey_number', models.IntegerField()),
                ('is_he_a_starter', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'db_table': 'jugador',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_team', models.CharField(max_length=20, verbose_name='Nombre del equipo')),
                ('flag_image', models.ImageField(null=True, upload_to='images/', verbose_name='Bandera del quipo')),
                ('team_shield', models.ImageField(null=True, upload_to='images/', verbose_name='Escudo del equipo')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'db_table': 'equipo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=20, verbose_name='Apellido')),
                ('birthdate', models.DateField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fifa.team')),
            ],
            options={
                'verbose_name': 'Tecnico',
                'verbose_name_plural': 'Tecnicos',
                'db_table': 'tecnico',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fifa.player')),
            ],
            options={
                'verbose_name': 'Posicion',
                'verbose_name_plural': '',
                'db_table': 'posicion',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='player',
            name='equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fifa.team'),
        ),
    ]
