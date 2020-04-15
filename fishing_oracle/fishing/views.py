from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Fishing


def index(request):
    fishing_list = Fishing.objects.all()
    context = {'fishing_list': fishing_list, }
    return render(request, 'fishing/index.html', context)


def detail(request, fishing_id):
    return HttpResponse("Просмоотр результатов рыбалки %s." % fishing_id)
