from django.shortcuts import render , redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Tarea

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def acerda_de(request):
    return render(request,'acerca-de.html')

@login_required
def mostrar_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

@login_required
def nuevos_registros(request):
    Proyecto.objects.create(
        nombre="Aplicación Bancaria", 
        descripcion="Aplicación web para gestionar cuentas bancarias", 
        duracion=1000
    )
    return HttpResponse('registro guardado')

@login_required
def ver_proyecto(request,id):
    proyecto = Proyecto.objects.get(id=id)
    return render(request, 'detalle-proyecto.html', {'proyecto': proyecto})

@login_required
def nuevo_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')
        imagen = request.FILES.get('imagen')
    
        if nombre and descripcion and duracion: 
            proyecto = Proyecto(
                nombre=nombre,
                descripcion=descripcion,
                duracion=duracion,
                imagen=imagen
            )
            proyecto.save()
    
            return redirect('proyectos')

    return render(request, 'nuevo-proyecto.html')

@login_required
def eliminar_proyecto(request, id):
    proyecto = Proyecto.objects.get(id=id)
    proyecto.delete()
    return redirect('proyectos')

@login_required
def editar_proyecto(request,id):   
    proyecto = Proyecto.objects.get(id=id)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        duracion = request.POST.get('duracion')

        if nombre and descripcion and duracion:
            proyecto.nombre = nombre
            proyecto.descripcion = descripcion
            proyecto.duracion = int(duracion)
            proyecto.save()
            return redirect('ver_proyecto', id=proyecto.pk)
    
    return render(request,'editar-proyecto.html', {"proyecto":proyecto})

@login_required
def crear_tarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        titulo = request.POST.get('titulo').strip()
        prioridad = request.POST.get('prioridad')
        estado = request.POST.get('estado')

        if titulo:
            tarea = Tarea(
                titulo=titulo,
                prioridad=prioridad,
                estado=estado,
                proyecto=proyecto)
            tarea.save()

            return redirect('ver_proyecto', id=proyecto_id)
    
    datos = {
        'proyecto' : proyecto,
        'prioridad_choices': Tarea.PRIORIDAD_CHOICES,
        'estado_choices': Tarea.ESTADO_CHOICES
    }

    return render(request,'crear_tarea.html', datos)

#lo siguiente es un decorador, le da indicaciones a lo que esta debajo de el, ya sea metodo u otra cosa

@require_POST
def avanzar_estado_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if tarea.estado == 'PENDIENTE':
        tarea.estado = 'EN_PROGRESO'
        tarea.save()
    elif tarea.estado == 'EN_PROGRESO':
        tarea.estado = 'COMPLETADA'
        tarea.save()
    
    return redirect('ver_proyecto', id=tarea.proyecto.id)

def avanzar_rapido(request,id):
    tarea = get_object_or_404(Tarea, id=id)
    
    if tarea.estado != 'COMPLETADA':
        tarea.estado = 'COMPLETADA'
        tarea.save()
    
    return redirect('ver_proyecto', id=tarea.proyecto.id)

@require_POST
def eliminar_tarea(request,id):
    tarea = get_object_or_404(Tarea,id=id)
    id_proyecto = tarea.proyecto.id
    tarea.delete()
    return redirect('ver_proyecto',id=id_proyecto)