Proyecto Django de Biblioteca
Este proyecto es una aplicación Django para gestionar una biblioteca, incluyendo autores, libros y películas basadas en libros.

Requisitos
Python 3.12 o superior
Django 5.0.7 o superior

Estructura del Proyecto
1. Inicio del Proyecto
El proyecto se inicia con la página de aterrizaje (landing page) que ofrece opciones para gestionar autores, libros y películas.
2. Agregar Autor
Permite añadir nuevos autores a la base de datos.
La información requerida incluye el nombre del autor.
3. Buscar Autor
Permite buscar autores en la base de datos por nombre.
Muestra una lista de autores que coinciden con la búsqueda.
4. Agregar Libro
Permite añadir nuevos libros a la base de datos.
Se puede ingresar información como título, autor, editorial, y fecha de publicación.
5. Agregar Película Basada en Libro
Permite añadir películas basadas en libros.
Se puede ingresar información como título de la película, libro relacionado, director, y año de lanzamiento.
Instalación y Configuración
Clonar el Repositorio

Clona el repositorio desde la URL proporcionada.
Instalar Dependencias

Asegúrate de tener Python y Django instalados.
Ejecuta el comando para instalar las dependencias requeridas.
Configurar la Base de Datos

Ajusta los parámetros de configuración de la base de datos si es necesario.
Realiza las migraciones iniciales para crear las tablas en la base de datos.
Iniciar el Servidor de Desarrollo

Ejecuta el comando para iniciar el servidor de desarrollo de Django.
Acceder a la Aplicación

Abre un navegador web y accede a la URL del servidor local para interactuar con la aplicación.
Uso
Página de Aterrizaje: Accede a las opciones para agregar autores, buscar autores, agregar libros y agregar películas.
Agregar Autor: Completa el formulario para añadir un nuevo autor.
Buscar Autor: Utiliza el formulario de búsqueda para encontrar autores por nombre.
Agregar Libro: Rellena el formulario con los detalles del libro para agregarlo a la base de datos.
Agregar Película: Completa el formulario con la información de la película basada en un libro.



para crear usuarios admin desde el shell:

>>> from django.contrib.auth.models import User
>>> user=User.objects.create_user('foo', password='bar')
>>> user.role = 'admin'
>>> user.save()