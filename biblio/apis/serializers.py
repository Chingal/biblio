from rest_framework import serializers

from django.contrib.auth.models import User
from biblio.apps.inicio.models import Perfil

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Perfil
        fields = ('url', 'usuario','telefono',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = User
        fields = ('url', 'username','email','password','first_name', 'last_name',)
        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user