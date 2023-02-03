from django.urls import path
from .views import index, registrar_libro, eliminar_libro,actualizar_libro, editar_curso


urlpatterns = [
    path("",  index , name='index'),
    path("registrarLibro/", registrar_libro, name='registrar'),
    path("eliminarLibro/<int:id>/", eliminar_libro, name='eliminar'),
    path("editarCurso/",editar_curso, name='editar'),
    path("edicionLibro/<int:id>/", actualizar_libro , name='actualizar')
]
