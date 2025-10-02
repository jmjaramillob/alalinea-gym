from django.contrib import admin
from .models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'bio')  # Columnas en la lista
    search_fields = ('name', 'role')  # Barra de búsqueda
    list_filter = ('role',)  # Filtro lateral por especialidad
    list_per_page = 10  # Paginación para evitar listas muy largas
