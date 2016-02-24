from django.db import models

class Autor(models.Model):
    #Ruta de la Imagen
    def RutaImagen(self, filename):
        ruta = "foto/%s/%s" % (self.nombre,str(filename) )
        return ruta

    # TODO: Define fields here
    nombre      = models.CharField(max_length=50)
    pais        = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    foto        = models.ImageField(upload_to=RutaImagen)
    print foto

    class Meta:
        verbose_name = ('Autor')
        verbose_name_plural = ('Autores')

    def __unicode__(self):
        return self.nombre