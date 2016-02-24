from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from biblio.apps.libros.models import Libro
from biblio.apps.autores.models import Autor


class BuscarView(TemplateView):
    template_name = "libros/buscar.html"

    def post(self,request,*args, **kwargs):
        txtBuscar = request.POST['txtBuscar']
        libros = Libro.objects.filter(nombre__contains=txtBuscar)
        if libros:
            datos = []
            for l in libros:
                autores = l.autor.all()
                datos.append(dict( [(l,autores)] ))
            return render(request,'libros/buscar.html', {'datos': datos})
        else:
            autores = Autor.objects.filter(nombre__contains=txtBuscar)
        return render(request, 'libros/buscar.html', {'autores': autores, 'esAutor': True } )

class BusquedaView(ListView):
    model               = Autor
    template_name       = "libros/busqueda.html"
    context_object_name = "autores"

class BusquedaAjaxView(TemplateView):
    #Sobreescribimos el metodo GET
    def get(self,request, *args, **kwargs):
        idAutor = request.GET['id']
        print idAutor
        libros = Libro.objects.filter(autor__id=idAutor)
        print libros
        data   = serializers.serialize('json', libros, fields=('nombre','resumen') )
        print data
        return HttpResponse(data, mimetype='application/json')
