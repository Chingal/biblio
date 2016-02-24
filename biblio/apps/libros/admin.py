from django.contrib import admin
from models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display      = ('id', 'nombre', 'resumen' ,'portada','getImagen',)
    list_filter       = ('autor',)
    search_fields     = ('nombre','autor__nombre')
    list_editable     = ('nombre', 'resumen',)
    filter_horizontal = ('autor',)

    def getImagen(self,libro):
        url = libro.getPortada()
        tag = "<img  src='%s' width=100 height=140>" % url
        return tag

    getImagen.allow_tags = True

admin.site.register( Libro, LibroAdmin)

