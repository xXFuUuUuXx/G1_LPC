from django.shortcuts import render
from django.http import Http

# Create your views here.
from agenda.models import Agenda

def agendas (request):
    retorno = "<h1>AGENDAS</h1>"
    agendas = Agenda.objects.all()
    for item in agendas:
        retorno += '</br>Compromisso: {}</br>'.format(agendas.fk_agenda_compromissos.all())
    return HttpResponse(retorno)


def get_agenda_ID(request, id):
    retorno = "<h1> AGENDA PUBLICA</h1>"
    agenda = Agenda.objects.get(pk=id)
