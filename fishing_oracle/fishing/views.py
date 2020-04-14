#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Fishing


def index(request):
    fishing_list = Fishing.objects.all()
    template = loader.get_template('fishing/index.html')
    context = {
        'fishing_list': fishing_list,
    }
    #output = ', '.join([str(f.date) for f in fishing_list])
    # output)  # "Запустим приложение 'Рыболовный оракул'")
    return HttpResponse(template.render(context, request))
