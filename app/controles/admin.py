from django.contrib import admin
from controles.models import local,esporte, agendamento
from django.utils.translation import gettext_lazy as _

@admin.register(local)
class localAdmin(admin.ModelAdmin):
    title=_(u'Local')
    
@admin.register(esporte)
class esporteAdmin(admin.ModelAdmin):
    title=_(u'esporte')
    
@admin.register(agendamento)
class agendamentoAdmin(admin.ModelAdmin):
    title=_(u'agendamento')

# @admin.register(esporte)
# @admin.register(agendamento)