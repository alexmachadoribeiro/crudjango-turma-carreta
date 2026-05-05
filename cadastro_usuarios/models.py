from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    genero = models.CharField(max_length=10, blank=True)