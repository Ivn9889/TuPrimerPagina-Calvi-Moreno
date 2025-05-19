from django.shortcuts import render, get_object_or_404
from .models import Pelicula, Serie, Opinion
from .forms import Peliform, Serieform, Opinionform, buscarform
def index(request):
    return render(request, 'Main/index.html')
# Create your views here.
def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    contexto = {'Peliculas':peliculas}
    return render(request, 'Catalogo/peliculas.html', contexto)

def detalle_pelicula(request,pk):
    pelicula = get_object_or_404(Pelicula,pk=pk)
    contexto = {'Pelicula':pelicula}
    return render(request, 'Catalogo/detalle_peliculas.html', contexto)

def lista_series(request):
    series = Serie.objects.all()
    contexto = {'Series':series}
    return render(request, 'Catalogo/series.html', contexto)

def detalle_serie(request,id):
    serie = get_object_or_404(Serie,pk=id)
    contexto = {'Serie':serie}
    return render(request, 'Catalogo/detalle_series.html', contexto)


def lista_opiniones(request):
    opiniones = Opinion.objects.all()
    contexto = {'Opiniones':opiniones}
    return render(request, 'Catalogo/opiniones.html', contexto)

def detalle_opiniones(request,id):
    opinion = get_object_or_404(Serie,pk = id)
    contexto = {'Opinion':opinion}
    return render(request, 'Catalogo/detalle_opiniones.html', contexto)

def agregar_pelicula(request):
    if request.method == "POST":
        peli = Peliform(request.POST)
    if peli.is_valid():
        peli.save()
        return render(request,"formulario.html")
    else:
        peli = Peliform()
    return render(request, "Catalogo/agregar_pelicula.html", {"form": peli})

def agregar_serie(request):
    if request.method == "POST":
        series = Serieform(request.POST)
    if series.is_valid():
        series.save()
        return render(request,"formulario.html")
    else:
        series = Serieform()
    return render(request, "Catalogo/agregar_serie.html", {"form": series})

def agregar_opinion(request):
    if request.method == "POST":
        opiniones = Opinionform(request.POST)
    if opiniones.is_valid():
        opiniones.save()
        return render(request,"formulario.html")
    else:
        series = Serieform()
    return render(request, "Catalogo/agregar_opinion.html", {"form": opiniones})