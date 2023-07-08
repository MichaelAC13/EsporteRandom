from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    template = 'index.html'
    teste = 'Teste'

    return render(request, template , locals())