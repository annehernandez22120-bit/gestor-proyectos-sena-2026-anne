from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('acerca-de/', views.acerda_de,name='acerca-de'),
    path('proyectos/',views.mostrar_proyectos, name='proyectos'),
    path('nuevos-registros/', views.nuevos_registros, name='nuevos_registros'),
    path('proyectos/<int:id>/',views.ver_proyecto, name='ver_proyecto'),
    path('proyectos/nuevo/', views.nuevo_proyecto, name='nuevo_proyecto'),
    path('proyectos/<int:id>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('proyectos/<int:id>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/<int:proyecto_id>/tareas/nueva/', views.crear_tarea, name="crear_tarea"),
    path('tareas/<int:id>/avanzar',views.avanzar_estado_tarea, name='avanzar_estado_tarea'),
    path('tareas/<int:id>/avanzar',views.avanzar_rapido, name='avanzar_rapido'),  
    path('tareas/<int:id>/eliminar', views.eliminar_tarea, name='eliminar_tarea'),
]