from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^cadastrar_carro/', cadastrar_carro, name='cadastrar_carro'),
    url(r'^listar_carro/', listar_carro, name='carro_list'),
    url(r'^editar_carro/(?P<pk>[0-9]+)/', editar_carro, name='editar_carro'),
    url(r'^remover_carro/(?P<pk>[0-9]+)/', remover_carro, name='remover_carro'),
    url(r'^cadastrar_comentario/', cadastrar_comentario, name='comentarios'),
]
