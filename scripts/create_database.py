import os
import django
import sys

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'education_project.settings')
django.setup()

from django.core.management import execute_from_command_line

def create_database():
    """Создание базы данных и применение миграций"""
    print("Применение миграций...")
    execute_from_command_line(['manage.py', 'migrate'])
    
    print("База данных успешно создана!")

if __name__ == '__main__':
    create_database()
