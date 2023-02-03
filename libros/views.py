from django.shortcuts import render,redirect
from .models import Libros
from django.contrib import messages


# Create your views here.
def  index (request):
    
    libros = Libros.objects.all()
    messages.success(request,'cursos listados')
    
    return render(request, 'index.html', {'libros':libros})


def registrar_libro( request):
    codigo=int(request.POST['codigo'])
    autor =request.POST['autor']
    libro =request.POST['libro']

    print( codigo, autor, libro)
    a = Libros.objects.filter(codigo=codigo).first()

    
    
    if a  is not  None:
       return redirect('/')
    Libro = Libros.objects.create( codigo=codigo, nombre=libro, seudonimo=autor )

    return redirect('/')


def eliminar_libro (request, id):

    libro = Libros.objects.filter(codigo=id).first()

    libro.delete()
    return redirect('/')


def actualizar_libro( request,id ):

    libro = Libros.objects.filter(codigo=id).first()
    return render(request, "edicion.html" , {'libro':libro})

def editar_curso (request):
    codigo=int(request.POST['codigo'])
    autor =request.POST['autor']
    libro =request.POST['libro']

    libro_ = Libros.objects.get(codigo=codigo)

    libro_.nombre = libro
    libro_.seudonimo = autor

    libro_.save()

    return redirect('/')
    