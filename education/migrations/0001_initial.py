import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название программы')),
                ('university', models.CharField(max_length=200, verbose_name='Университет')),
                ('degree_level', models.CharField(choices=[('bachelor', 'Бакалавриат'), ('master', 'Магистратура'), ('specialist', 'Специалитет')], max_length=20, verbose_name='Уровень образования')),
                ('duration_years', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)], verbose_name='Длительность (лет)')),
                ('cost_per_year', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость в год (руб.)')),
                ('study_type', models.CharField(choices=[('full_time', 'Очное'), ('part_time', 'Заочное'), ('distance', 'Дистанционное')], max_length=20, verbose_name='Форма обучения')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Образовательная программа',
                'verbose_name_plural': 'Образовательные программы',
                'ordering': ['-created_at'],
            },
        ),
    ]
