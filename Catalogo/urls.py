from django.urls import path
from .views import lista_opiniones, lista_peliculas,lista_series, index, detalle_pelicula, detalle_serie, detalle_opiniones
app_name = 'Catalogo'
urlpatterns = [
    path('peliculas/', lista_peliculas, name='lista_peliculas'),
#    path('peliculas/<int:pk>/', detalle_pelicula, name='detalle_pelicula'),
    path('series/', lista_series, name='lista_series'),
#    path('series/<int:id>/', detalle_serie, name='detalle_serie'),
    path('opiniones/', lista_opiniones, name='lista_opiniones'),
#    path('opiniones/<int:id>/', detalle_opiniones, name='detalle_opiniones'),
]