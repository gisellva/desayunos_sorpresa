from django.shortcuts import render, redirect, get_object_or_404
from .forms import DesayunoForm
from .models import Desayuno

def crear_desayuno(request):
    if request.method == 'POST':
        form = DesayunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_desayunos')
    else:
        form = DesayunoForm()
    return render(request, 'desayunos/crear_desayuno.html', {'form': form})

def listar_desayunos(request):
    desayunos = Desayuno.objects.all()
    return render(request, 'desayunos/listar_desayunos.html', {'desayunos': desayunos})

def eliminar_desayuno(request, desayuno_id):
    desayuno = get_object_or_404(Desayuno, id=desayuno_id)
    desayuno.delete()
    return redirect('listar_desayunos')

def editar_desayuno(request, desayuno_id):
    desayuno = get_object_or_404(Desayuno, id=desayuno_id)

    if request.method == 'POST':
        form = DesayunoForm(request.POST, instance=desayuno)
        if form.is_valid():
            form.save()
            return redirect('listar_desayunos')
    else:
        form = DesayunoForm(instance=desayuno)

    return render(request, 'desayunos/editar_desayuno.html', {'form': form, 'desayuno': desayuno})