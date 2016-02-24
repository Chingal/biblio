from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from biblio.apps.inicio.models import Perfil
from .serializers import PerfilSerializer, UserSerializer

from .permissions import IsStaffOrTargetUser

class PerfilViewSet(viewsets.ModelViewSet):
    queryset         = Perfil.objects.all() #Obtiene todos los perfiles
    serializer_class = PerfilSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset         = User.objects.all() #Obtiene todos los Usuarios
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST'
                else IsStaffOrTargetUser()),