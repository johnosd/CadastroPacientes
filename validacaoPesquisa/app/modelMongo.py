from django.db import models
from mongoengine import *
connect('comentarios')

class Comentario(Document):
    id_carro = IntField(required=True)
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=False)
