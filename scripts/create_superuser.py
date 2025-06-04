import os
import django
import sys

# Добавляем путь к проекту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'education_project.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    """Создание суперпользователя для админ-панели"""
    
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123'
    
    if User.objects.filter(username=username).exists():
        print(f"Пользователь {username} уже существует")
        return
    
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    
    print(f"Суперпользователь создан:")
    print(f"Логин: {username}")
    print(f"Пароль: {password}")
    print(f"Email: {email}")
    print("Теперь вы можете войти в админ-панель по адресу /admin/")

if __name__ == '__main__':
    create_superuser()
