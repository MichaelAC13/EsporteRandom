from django.db import models
from django.utils import timezone

class local(models.Model):
    rua = models.CharField(max_length=300, verbose_name='Rua', null=True, blank=True)
    numero = models.PositiveIntegerField(verbose_name='Número', null=True, blank=True)
    bairro = models.CharField(max_length=250, verbose_name='Bairro', null=True, blank=True)
    cidade = models.CharField(max_length=250, verbose_name='Cidade', null=True, blank=True)
    estado = models.CharField(max_length=50, verbose_name='Estado', null=True, blank=True)
    cep = models.CharField(max_length=10, verbose_name='CEP', null=True, blank=True)
    pais = models.CharField(max_length=100, verbose_name='País', null=True, blank=True)
    lat = models.CharField(max_length=30, verbose_name='Latitude', null=True, blank=True)
    lon = models.CharField(max_length=30, verbose_name='Longitude', null=True, blank=True)
    tipo = models.ManyToManyField('esporte', verbose_name='Tipo', blank=True)
     
    @property
    def place_id(self):
        return 0
    
    class Meta:
        verbose_name_plural = "Locais"
ESPORTE_CHOICES = (
    (u"Futebol",u"Futebol"),
    (u"Futebol G. Sintetica",u"Futebol G. Sintetica"),
    (u"Futebol Campo",u"Futebol Campo"),
    (u"Volei Quadra",u"Voleu Quadra"),
)
class esporte(models.Model):    
    tipo = models.CharField(max_length=30, verbose_name='Tipo', choices=ESPORTE_CHOICES, blank=True)
    cor = models.CharField(max_length=10, verbose_name='Cor', null=True, blank=True)
    icon_url = models.ImageField(verbose_name='Icone', upload_to="media/leaflet/images/", max_length=100, default="media/leaflet/images/marker-icon.png")

    class Meta:
        verbose_name_plural = "Esportes"  
          
class agendamento(models.Model):
    local = models.ForeignKey('Local', on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(verbose_name='Data', null=True, blank=True)
    hora = models.TimeField(max_length=10, verbose_name='Hora', null=True, blank=True)
    duracao = models.CharField(max_length=10, verbose_name='Duração', null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Agendamentos"


