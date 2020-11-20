from django.shortcuts import render


def index(request):
    """
    Главная страница
    """
    return render(request, 'fishing/index.html')
