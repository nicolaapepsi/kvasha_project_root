from django.http import HttpResponse
from django.shortcuts import render

def about (request):
    return HttpResponse('Це інформація про проєкт')

def home (request):
    return render(request, 'home.html', {'greeting':'Доброго дня!'})

def resume_view(request):
    context = {
        'author_name': 'Ім’я',
        'professional_interests': 'Професійний напрямок',
        'work_experience': 'Досвід роботи',
        'education': 'Освіта',
    }
    return render(request, 'resume.html', context)
