# MiAplicacion/urls.py
from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.landing_page, name='landing_page'),  # Página de aterrizaje
    path('agregar_autor/', views.agregar_autor, name='agregar_autor'),
    path('buscar_autor/', views.buscar_autor, name='buscar_autor'),
    path('agregar_libro/', views.agregar_libro, name='agregar_libro'),  # Nueva sección
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index_libros/', views.index_libros, name='index_libros'),
    path('index_autores/', views.index_autores, name='index_autores'),
    path('agregar_editorial/', views.agregar_editorial, name='agregar_editorial'),
    path('libros/<int:libro_id>/', views.show_libro, name='show_libro'),
    path('libros/edit/<int:libro_id>/', views.edit_libro, name='edit_libro'),
    path('libro/delete/<int:libro_id>/', views.delete_libro, name='delete_libro'),
]
