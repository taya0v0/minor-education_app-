from django.contrib import admin
from .models import EducationalProgram

@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'university', 'degree_level', 'study_type', 'cost_per_year', 'created_at']
    list_filter = ['degree_level', 'study_type']
    search_fields = ['name', 'university']
    ordering = ['-created_at']
