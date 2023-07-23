import json

from django.shortcuts import render
from controles.models import local,agendamento
from django.core import serializers
from django.http import HttpResponse,JsonResponse

def index(request):
    template = 'index.html'
    if request.POST.get("main-street"):
        local.objects.get_or_create(
        rua=request.POST.get("main-street"),
        numero=request.POST.get("main-number"),
        bairro=request.POST.get("main-county"),
        cidade=request.POST.get("main-city"),
        estado=request.POST.get("main-state"),
        pais=request.POST.get("main-country"),
        lat=request.POST.get("main-lat"),
        lon=request.POST.get("main-lon"), 
        cep=request.POST.get("main-postalcode"))
    return render(request, template , locals())

def locais(request):
    return HttpResponse(json.dumps(serializers.serialize("json", local.objects.all())))

def agendamentos(request):
    return HttpResponse(json.dumps(serializers.serialize("json", agendamento.objects.all())))

