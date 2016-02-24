from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from models import Autor

class CreateAutor(CreateView):
    model = Autor #El modelo de donde extrameos la informacion y se pasa como una lista de objettos al template
    template_name = "autores/add.html"
    success_url =  reverse_lazy("list")  # Si toda la informacion del Formulario es correcta se redirigie

class ListAutor(ListView):
    model = Autor  #Le decimos a Django, de que modelo queremos extraer la informacion
    template_name = "autores/list.html"
    context_object_name = "autores"
