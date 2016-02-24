from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    usuario  = models.OneToOneField(User)
    telefono = models.IntegerField(max_length=15)

    class Meta:
        verbose_name = ('Perfil')
        verbose_name_plural = ('Perfiles')

    def __unicode__(self):
        return self.usuario.username
    