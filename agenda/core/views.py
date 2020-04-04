from django.shortcuts import render
from core.models import Evento

# Create your views here.
def lista_eventos(request):
    eventos = Evento.objects.all()
    response = {'eventos':eventos}
    return render(request, 'agenda.html', response)