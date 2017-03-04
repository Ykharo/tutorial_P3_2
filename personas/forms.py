from django import forms

from .models import Persona, Ctto

class PersonaCreateForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('dni','nombre','apellido_paterno','apellido_materno')
        labels = {
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.Textarea(attrs={'class': 'form-control'}),

        }

class CttoUpdateForm(forms.ModelForm):

    class Meta:
        model = Ctto
        fields = ['NumCtto','DescCtto','MonedaCtto','ValorCtto','IdCtta','EstCtto','FechIniCtto','IdCecoCtto','CordCtto','IdMandante' ]
        labels = {
            'FechIniCtto': 'Fecha de Inicio',
            'IdCecoCtto': 'Centro de Costo'
        }

        widgets = {
            'NumCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'DescCtto': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),
            'MonedaCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'ValorCtto': forms.NumberInput(attrs={'class': 'form-control'} ),
            #'IdCtta': forms.TextInput(attrs={'class': 'form-control'}),
            'EstCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'FechIniCtto': forms.DateInput(format='%m/%d/%Y'),
            #'IdCecoCtto': forms.TextInput(attrs={'class': 'form-control'}),
            'CordCtto': forms.TextInput(attrs={'class': 'form-control','rows':1, 'cols':60}),
            #'IdMandante': forms.Textarea(attrs={'class': 'form-control'}),

        }
