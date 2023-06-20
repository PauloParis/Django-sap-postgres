
# https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
# https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/

from django.forms import ModelForm, EmailInput, TextInput
from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):

    class Meta:
        model = Persona
        fields = '__all__' # los campos a utilizar
        # tipo de campo del formulario de tipo persona
        widgets = {
            # especificar el tipo de dato pero a nivel HTML
            'email': EmailInput(attrs={'type': 'email'}),

        }


class DomicilioForm(ModelForm):

    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'num_calle': TextInput(attrs={'type': 'number'}),

        }