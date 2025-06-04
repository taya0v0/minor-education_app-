import os
import django
import sys
from decimal import Decimal

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'education_project.settings')
django.setup()

from education.models import EducationalProgram

def seed_database():
    """Заполнение базы данных тестовыми данными"""
    
    # Очистка существующих данных
    EducationalProgram.objects.all().delete()
    
    # Тестовые данные
    programs_data = [
        {
            'name': 'Программная инженерия',
            'university': 'МГУ им. М.В. Ломоносова',
            'degree_level': 'bachelor',
            'duration_years': 4,
            'cost_per_year': Decimal('350000.00'),
            'study_type': 'full_time',
        },
        {
            'name': 'Прикладная математика и информатика',
            'university': 'МФТИ',
            'degree_level': 'bachelor',
            'duration_years': 4,
            'cost_per_year': Decimal('400000.00'),
            'study_type': 'full_time',
        },
        {
            'name': 'Экономика предприятий и организаций',
            'university': 'НИУ ВШЭ',
            'degree_level': 'master',
            'duration_years': 2,
            'cost_per_year': Decimal('450000.00'),
            'study_type': 'full_time',
        },
        {
            'name': 'Психология развития',
            'university': 'СПбГУ',
            'degree_level': 'specialist',
            'duration_years': 5,
            'cost_per_year': Decimal('280000.00'),
            'study_type': 'part_time',
        },
        {
            'name': 'Международные отношения',
            'university': 'МГИМО',
            'degree_level': 'bachelor',
            'duration_years': 4,
            'cost_per_year': Decimal('500000.00'),
            'study_type': 'full_time',
        },
        {
            'name': 'Биоинженерия и биоинформатика',
            'university': 'МГУ им. М.В. Ломоносова',
            'degree_level': 'master',
            'duration_years': 2,
            'cost_per_year': Decimal('380000.00'),
            'study_type': 'full_time',
        },
        {
            'name': 'Дизайн и архитектура',
            'university': 'МАРХИ',
            'degree_level': 'specialist',
            'duration_years': 6,
            'cost_per_year': Decimal('320000.00'),
            'study_type': 'full_time',
        },
        {
            'name': 'Цифровая экономика',
            'university': 'НИУ ВШЭ',
            'degree_level': 'bachelor',
            'duration_years': 4,
            'cost_per_year': Decimal('420000.00'),
            'study_type': 'distance',
        }
    ]
    
    # Создание записей
    for data in programs_data:
        EducationalProgram.objects.create(**data)
    
    print(f"Создано {len(programs_data)} образовательных программ")
    print("База данных успешно заполнена тестовыми данными!")

if __name__ == '__main__':
    seed_database()
