from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Fishing


def index(request):
    fishing_list = Fishing.objects.all()
    context = {'fishing_list': fishing_list, }
    return render(request, 'fishing/index.html', context)


def detail(request, fishing_id):
    fishing = get_object_or_404(Fishing, pk=fishing_id)
    return render(request, 'fishing/detail.html', {'fishing': fishing})
