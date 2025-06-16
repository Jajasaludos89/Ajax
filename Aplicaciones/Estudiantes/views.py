from django.shortcuts import render
from django.http import JsonResponse
from .models import Estudiante

# Vista principal que se muestra al acceder a la raíz o /estudiantes/
def inicio(request):
    return render(request, 'estudiantes.html')

def listadoEstudiantes(request):
    estudiantes = list(Estudiante.objects.values())
    return JsonResponse({'estudiantes': estudiantes})

def nuevoEstudiante(request):
    nombre = request.POST.get('nombre')
    apellidos = request.POST.get('apellidos')
    fecha_nacimiento = request.POST.get('fecha_nacimiento')
    foto = request.FILES.get('foto')

    est = Estudiante.objects.create(
        nombre=nombre,
        apellidos=apellidos,
        fecha_nacimiento=fecha_nacimiento,
        foto=foto
    )
    return JsonResponse({'mensaje': 'Estudiante creado'})

def editarEstudiante(request, id):
    if request.method == 'POST':
        est = Estudiante.objects.get(id=id)
        est.nombre = request.POST.get('nombre')
        est.apellidos = request.POST.get('apellidos')
        est.fecha_nacimiento = request.POST.get('fecha_nacimiento')

        foto = request.FILES.get('foto')
        if foto:
            if est.foto:
                est.foto.delete(save=False)
            est.foto = foto

        est.save()
        return JsonResponse({'mensaje': 'Estudiante actualizado'})

def eliminarEstudiante(request, id):
    if request.method == 'POST':
        est = Estudiante.objects.get(id=id)
        if est.foto:
            est.foto.delete(save=False)
        est.delete()
        return JsonResponse({'mensaje': 'Estudiante eliminado'})
