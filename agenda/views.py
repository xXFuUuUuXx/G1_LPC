from django.shortcuts import render

# Create your views here.
from agenda.models import Agenda, Agenda_Institucional


def agendas (request):
    retorno = "<h1>AGENDAS</h1>"
    agendas = Agenda.objects.all()
    for item in agendas:
        retorno += '</br>Compromisso: {}</br>'.format(agendas.fk_agenda_compromissos.all())
    return HttpResponse(retorno)

def institucional(request):
    retorno = "<h1>Institucional<h1>"
    institucional = Agenda_Institucional.objects.all()
    for item in institucional:
        retorno += '</br> Compromisso: {}</br>'.format(institucional.fk_institucional.all())

def get_agenda_ID(request, id):
    retorno = "<h1> AGENDA PUBLICA</h1>"
    agenda = Agenda.objects.get(pk=id)
