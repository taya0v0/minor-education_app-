from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q, Avg, Count
from .models import EducationalProgram
from .forms import EducationalProgramForm, FilterForm

def home(request):
    """Главная страница"""
    total_programs = EducationalProgram.objects.count()
    recent_programs = EducationalProgram.objects.all()[:3]

    context = {
        "total_programs": total_programs,
        "recent_programs": recent_programs,
    }
    return render(request, "education/home.html", context)

def add_program(request):
    """Добавление новой образовательной программы"""
    if request.method == "POST":
        form = EducationalProgramForm(request.POST)
        if form.is_valid():
            program = form.save()
            messages.success(request, f'Программа "{program.name}" успешно добавлена!')
            return redirect("program_list")
    else:
        form = EducationalProgramForm()

    return render(request, "education/add_program.html", {"form": form})

def program_list(request):
    """Список всех программ с фильтрацией и сортировкой"""
    form = FilterForm(request.GET)
    programs = EducationalProgram.objects.all()

    if form.is_valid():
        # Поиск по университету
        university = form.cleaned_data.get("university")
        if university:
            programs = programs.filter(university__icontains=university)

        # Фильтрация по уровню образования
        degree_level = form.cleaned_data.get("degree_level")
        if degree_level:
            programs = programs.filter(degree_level=degree_level)

        # Фильтрация по форме обучения
        study_type = form.cleaned_data.get("study_type")
        if study_type:
            programs = programs.filter(study_type=study_type)

        # Сортировка
        sort_by = form.cleaned_data.get("sort_by")
        if sort_by:
            programs = programs.order_by(sort_by)

    context = {
        "form": form,
        "programs": programs,
        "total_count": programs.count(),
    }
    return render(request, "education/program_list.html", context)

def statistics(request):
    """Статистика по образовательным программам"""
    # Статистика по уровням образования
    degree_stats = (
        EducationalProgram.objects.values("degree_level")
        .annotate(
            count=Count("id"), 
            avg_cost=Avg("cost_per_year")
        )
        .order_by("-count")
    )

    # Статистика по формам обучения
    study_type_stats = (
        EducationalProgram.objects.values("study_type")
        .annotate(
            count=Count("id"), 
            avg_cost=Avg("cost_per_year")
        )
        .order_by("-count")
    )


    context = {
        "degree_stats": degree_stats,
        "study_type_stats": study_type_stats,
    }
    return render(request, "education/statistics.html", context)
