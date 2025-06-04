from django import forms
from .models import EducationalProgram

class EducationalProgramForm(forms.ModelForm):
    class Meta:
        model = EducationalProgram
        fields = [
            'name', 'university', 'degree_level', 
            'duration_years', 'cost_per_year', 'study_type'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название программы'}),
            'university': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название университета'}),
            'degree_level': forms.Select(attrs={'class': 'form-control'}),
            'duration_years': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '6'}),
            'cost_per_year': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'study_type': forms.Select(attrs={'class': 'form-control'}),
        }

class FilterForm(forms.Form):
    university = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Поиск по университету'})
    )
    degree_level = forms.ChoiceField(
        choices=[('', 'Все уровни')] + EducationalProgram.DEGREE_LEVELS,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    study_type = forms.ChoiceField(
        choices=[('', 'Все формы обучения')] + EducationalProgram.STUDY_TYPES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sort_by = forms.ChoiceField(
        choices=[
            ('name', 'По названию'),
            ('university', 'По университету'),
            ('cost_per_year', 'По стоимости'),
            ('duration_years', 'По длительности'),
            ('created_at', 'По дате добавления'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
