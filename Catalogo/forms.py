from django import forms

class Peliform(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=10)
    sinopsis = forms.CharField(max_length=100)
class Serieform(forms.Form):
    nombre =  forms.CharField(max_length=40)
    genero = forms.CharField(max_length=10)
    sinopsis = forms.CharField(max_length=100)
class Opinionform(forms.Form):
    texto = forms.CharField(max_length=100)   
class buscarform(forms.Form):
    titulo = forms.CharField(max_length=40)