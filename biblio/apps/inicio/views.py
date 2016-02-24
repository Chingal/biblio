from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, RequestContext
from django.views.generic import TemplateView,FormView

from forms import UserForm
from models import Perfil

class Index(TemplateView):
    #template_name = "inicio/index.html"	#Aqui heredamos el metodo Get del TemplateView

    #Sobreescrimos el metodo GET
    def get(self, request, *args, **kwargs):
        return render_to_response('inicio/index.html', context_instance=RequestContext(request))

class Registrarse(FormView):
    template_name = "inicio/registrarse.html"
    form_class    = UserForm
    success_url   = reverse_lazy('login')

    # Sobreescribimos el metodo form_valid() del formulario
    #Si los datos del form son validos, entra a este metodo
    def form_valid(self, form):
        '''
        :Se valida el Formulario, se guarda, regresa el objeto, pero no te insertes a la BD
        '''
        user       = form.save();
        print user
        #print self
        p          = Perfil()
        p.usuario  = user
        p.telefono = form.cleaned_data['telefono']
        p.save()
        return super(Registrarse, self).form_valid(form)