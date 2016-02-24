from django.conf.global_settings import MEDIA_URL, MEDIA_ROOT
from django.db import models
from biblio.apps.autores.models import Autor


class Libro(models.Model):
    #Obtenemos la ruta de la Imagen
    def rutaImagen(self, filename):
        ruta = "Libro/%s/%s" % (self.nombre, str(filename))
        return ruta

        #Atributos
    autor   = models.ManyToManyField(Autor)
    nombre  = models.CharField(max_length=50)
    resumen = models.TextField(max_length=400)
    portada = models.ImageField(upload_to=rutaImagen)

    class Meta:
        verbose_name = ('Libro')
        verbose_name_plural = ('Libros')

    def getPortada(self):
        return "http://localhost:8000/media/%s" % self.portada

    def __unicode__(self):
        return self.nombre