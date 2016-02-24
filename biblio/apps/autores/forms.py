from django.forms import forms
from models import Autor

class AutorForm(forms.Form):
    class Meta:
        model = Autor
    