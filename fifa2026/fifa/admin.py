from django.contrib import admin
from .models import Team, Player, Position, Technical, Nacionality, Role


admin.site.register(Team)
admin.site.register(Position)
admin.site.register(Technical)
admin.site.register(Nacionality)
admin.site.register(Role)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('name_player', 'last_name_player')
    list_filter = ('team',)
    list_per_page = 5

