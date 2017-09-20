from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.
from .models import *
from .modelMongo import *

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano', 'valor', 'data_cadastro']


def cadastrar_carro(request, template_name='carro_form.html'):
    form = CarroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('carro_list')
    return render(request, template_name, {'form': form})


def listar_carro(request, template_name="carro_list.html"):
    query = request.GET.get("busca")
    if query:
        carro = Carro.objects.filter(modelo__icontains=query)
    else:
        carro = Carro.objects.all()
    carros = {'lista': carro}
    return render(request, template_name, carros)


def editar_carro(request, pk, template_name='carro_form.html'):
    carro = get_object_or_404(Carro, pk=pk)
    if request.method == "POST":
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm(instance=carro)
    return render(request, template_name, {'form': form})


def remover_carro(request, pk, template_name='carro_delete.html'):
    carro = Carro.objects.get(pk = pk)
    if request.method == "POST":
        carro.delete()
        return redirect('carro_list')
    return render(request, template_name, {'carro': carro})

def cadastrar_comentario(request,  template_name='cadastrar_comentario.html'):
    if request.method == 'POST':
        # save new postdir
        title = request.POST['title']
        content = request.POST['content']
        id_carro = request.POST['CarroList']
        last_update = datetime.now()
        comentario = Comentario(title=title)
        comentario.content = content
        comentario.id_carro = id_carro
        comentario.last_update = last_update
        comentario.save()
        pk = 0
        return redirect('comentario_list', pk)
        # Get all posts from DB
    comentarios = Comentario.objects
    carro = Carro.objects.all()
    return render(request, template_name, {'Posts': comentarios, 'lista':carro})  # context_instance=RequestContext(request))

def listar_comentario(request, pk, template_name='comentario_list.html'):
    # Get all posts from DB
    if int(pk) > 0:
        comentarios = Comentario.objects.filter(id_carro=pk)
        carro = Carro.objects.get(pk=pk)
    else:
        comentarios = Comentario.objects
        carro = Carro.objects
    return render(request,template_name, {'Comentarios': comentarios, 'carro': carro})

def remover_comentario(request, pk, template_name='comentario_delete.html'):
    comentario = Comentario.objects.get(id=pk)
    if request.method == 'POST':
        comentario.delete()
        pk = 0
        return redirect('comentario_list',pk)
    return render(request, template_name, {'comentario': comentario})

def editar_comentario(request, pk, template_name='cadastrar_comentario.html'):
    comentario = Comentario.objects.get(id=pk)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        id_carro = request.POST['CarroList']
        last_update = datetime.now()
        comentario = Comentario(title=title)
        comentario.content = content
        comentario.id_carro = id_carro
        comentario.last_update = last_update
        comentario.save()
        pk = 0
        return redirect('comentario_list', pk)

    comentarios = Comentario.objects
    carro = Carro.objects.all()
    return render(request, template_name, {'comentario': comentario,'lista':carro})
