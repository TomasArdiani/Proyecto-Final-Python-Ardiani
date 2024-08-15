from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    def is_superuser():
        return self.role == 'admin'


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, default=1)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=1)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField(default='2024-07-28')
    genero = models.CharField(max_length=100)
    numero_paginas = models.IntegerField()
    idioma = models.CharField(max_length=50)
    imagen_portada = models.URLField(blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.titulo    

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # Role choices
    ADMIN = 'admin'
    EDITOR = 'editor'
    VIEWER = 'viewer'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (EDITOR, 'Editor'),
        (VIEWER, 'Viewer'),
    ]

    # New role field
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=VIEWER)

    def __str__(self):
        return self.name
