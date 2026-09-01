from django.db import models

class Proyecto(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    nombre = models.CharField(max_length=100) #Campo de texto (varchar)
    descripcion = models.TextField() #texto largo
    duracion = models.IntegerField() #entero
    imagen = models.ImageField(upload_to = 'img/', default = 'img/logo.png')

class Tarea(models.Model):
    '''
    modelo que representa la tarea de un proyecto
    '''

    PRIORIDAD_CHOICES = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    ]
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En progreso'),
        ('COMPLETADA', 'Completada'),
    ]
    
    # relacion 1 a muchos: un proyecto tiene muchas tareas
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete = models.CASCADE,
        related_name='tareas',
    )
    titulo = models.CharField(max_length=50)
    prioridad = models.CharField(
        max_length=5,
        choices= PRIORIDAD_CHOICES,
        default='MEDIA')
    estado = models.CharField(
        max_length=11,
        choices= ESTADO_CHOICES,
        default='PENDIENTE'
    )