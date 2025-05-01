from django.shortcuts import render, redirect
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
