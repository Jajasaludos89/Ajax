from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),  # Ruta raíz para evitar el error 404
    path('estudiantes/', views.inicio),
    path('listadoEstudiantes/', views.listadoEstudiantes),
    path('nuevoEstudiante/', views.nuevoEstudiante),
    path('editarEstudiante/<int:id>/', views.editarEstudiante),
    path('eliminarEstudiante/<int:id>/', views.eliminarEstudiante),
]
