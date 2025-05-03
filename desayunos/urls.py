from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_desayuno, name='crear_desayuno'),
    path('eliminar/<int:desayuno_id>/', views.eliminar_desayuno, name='eliminar_desayuno'),
    path('listar/', views.listar_desayunos, name='listar_desayunos'),
    path('editar/<int:desayuno_id>/', views.editar_desayuno, name='editar_desayuno'),
]
