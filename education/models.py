from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class EducationalProgram(models.Model):
    STUDY_TYPES = [
        ('full_time', 'Очное'),
        ('part_time', 'Заочное'),
        ('distance', 'Дистанционное'),
    ]
    
    DEGREE_LEVELS = [
        ('bachelor', 'Бакалавриат'),
        ('master', 'Магистратура'),
        ('specialist', 'Специалитет'),
    ]
    
    name = models.CharField(
        max_length=200, 
        verbose_name="Название программы"
    )
    university = models.CharField(
        max_length=200,
        verbose_name="Университет"
    )
    degree_level = models.CharField(
        max_length=20,
        choices=DEGREE_LEVELS,
        verbose_name="Уровень образования"
    )
    duration_years = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(6)],
        verbose_name="Длительность (лет)"
    )
    cost_per_year = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Стоимость в год (руб.)"
    )
    study_type = models.CharField(
        max_length=20,
        choices=STUDY_TYPES,
        verbose_name="Форма обучения"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления"
    )
    
    class Meta:
        verbose_name = "Образовательная программа"
        verbose_name_plural = "Образовательные программы"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.university})"
    
    @property
    def total_cost(self):
        """Общая стоимость обучения"""
        return self.cost_per_year * self.duration_years
