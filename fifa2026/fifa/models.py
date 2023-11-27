from django.db import models

class Role(models.Model):
    name_role = models.CharField(max_length=50, verbose_name="Rol")

    def __str__(self):
        return self.name_role

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"
        db_table = "rol"
        ordering = ['id']

class Team(models.Model):
    name_team = models.CharField(max_length=20, verbose_name="Nombre del equipo")
    flag_image = models.ImageField(upload_to='media\images', null=True, verbose_name='Bandera del equipo')
    team_shield = models.ImageField(upload_to='media\images', null=True, verbose_name='Escudo del equipo')

    def __str__(self):
        return self.name_team

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "equipo"
        ordering = ['id']

class Position(models.Model):
    name_position = models.CharField(max_length=20, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")
    
    def __str__(self):
        return self.name_position

    class Meta:
        verbose_name = "Posicion"
        verbose_name_plural = "Posiciones"
        db_table = "posicion"
        ordering = ['id']

class Nacionality(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nacionalidad")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Nacionalidad"
        verbose_name_plural = "Nacionalidades"
        db_table = "nacionalidad"
        ordering = ['id']

class Technical(models.Model):
    name_technical = models.CharField(max_length=20, verbose_name="Nombre del tecnico", default='')
    last_name_technical = models.CharField(max_length=20, verbose_name="Apellido del tecnico", default='')
    birthdate = models.DateField()

    nacionality = models.ForeignKey('Nacionality', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return self.name_technical

    class Meta:
        verbose_name = "tecnico"
        verbose_name_plural = "tecnicos"
        db_table = "tecnico"
        ordering = ['id']

class Player(models.Model):
    name_player = models.CharField(max_length=20, verbose_name="Nombre")
    last_name_player = models.CharField(max_length=20, verbose_name="Apellido")
    player_photo = models.ImageField(upload_to='media\images', null=True, verbose_name='Foto del jugador')
    birthdate = models.DateField()
    jersey_number = models.IntegerField()
    is_he_a_starter = models.BooleanField()
    
    position = models.ForeignKey('Position', on_delete=models.CASCADE, related_name='players', default=None)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_player} {self.last_name_player}"

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadores"
        db_table = "jugador"
        ordering = ['id']
