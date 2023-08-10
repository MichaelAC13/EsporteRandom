import json

from django.shortcuts import render
from controles.models import local,agendamento,esporte
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
    res = json.loads(serializers.serialize("json", local.objects.all()))
    for a in res:
        a["fields"]["agendamento"]=json.loads(serializers.serialize("json",agendamento.objects.filter(local=a["pk"])))
        for t in a["fields"]["tipo"]:
            a["fields"]["tipo"] = json.loads(serializers.serialize("json",esporte.objects.filter(pk=t)))
    print(res)
    return HttpResponse(json.dumps(res))

def agendamentos(request):
    res = json.loads(serializers.serialize("json", agendamento.objects.all()))
    for a in res:
        a["fields"]["local"]=json.loads(serializers.serialize("json",local.objects.filter(pk=a["fields"]["local"])))[0]
    print(res)
    return HttpResponse(json.dumps(res))

