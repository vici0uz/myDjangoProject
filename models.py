from django.db import models
from django import forms


class Autor(models.Model):
    presentacion = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    cabecera = models.ImageField(upload_to='tmp')

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=60)
    estado_provincia = models.CharField(max_length=30)
    pais = models.CharField(max_length=50)
    web = models.URLField()


class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor, on_delete=models.PROTECT)
    fechaPublicacion = models.DateField()
    num_paginas = models.IntegerField()

    class Admin:
        pass
