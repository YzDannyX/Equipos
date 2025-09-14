from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'founded', 'stadium', 'coach')
    search_fields = ('name', 'city')
    list_filter = ('city', 'founded')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model._meta.verbose_name = "Equipo"

admin.site.site_header = "Administración de Equipos de Fútbol"
admin.site.site_title = "Administración de Equipos"
admin.site.index_title = "Bienvenido al panel de administración"
