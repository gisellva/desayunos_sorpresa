from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_desayuno, name='crear_desayuno'),
    path('listar/', views.listar_desayunos, name='listar_desayunos'),
]
