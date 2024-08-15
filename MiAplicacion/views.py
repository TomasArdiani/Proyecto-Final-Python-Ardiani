from django.shortcuts import render, redirect, get_object_or_404
from .forms import AutorForm, LibroForm, PeliculaForm, BuscarAutorForm, UserRegisterForm, UserLoginForm, EditorialForm
from .models import Autor, Libro, Pelicula, Editorial
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied


def is_super_user(user):
    user = get_user_model()
    if user.is_authenticated and False:
        return True
    else:
        raise PermissionDenied()

def base(request):
    return render(request, 'base.html')

def landing_page(request):
    return render(request, 'landing.html')

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')  # Redirige a la página de aterrizaje después de guardar
    else:
        form = AutorForm()
    return render(request, 'agregar_autor.html', {'form': form})

def buscar_autor(request):
    form = BuscarAutorForm(request.GET or None)
    autores = []

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')
        if nombre:
            autores = Autor.objects.filter(nombre__icontains=nombre)
    
    return render(request, 'buscar_autor.html', {'form': form, 'autores': autores})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')  # Redirige a la página de aterrizaje después de guardar
    else:
        form = LibroForm()
    return render(request, 'libro_form.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after registering
            return redirect('landing_page')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                auth_login(request, user)
                # Display a message with the user's name
                message = f"Hi, {user.username}!"
                return render(request, 'landing.html', {'message': message})
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def index_libros(request):
    libros = Libro.objects.all()
    return render(request, 'index_libros.html', { 'libros': libros })

def index_autores(request):
    autores = Autor.objects.all()
    return render(request, 'index_autores.html', { 'autores': autores })

def agregar_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('some-view-name')  # Redirect to a new URL
            return render(request, 'landing.html', {'message': "editorial creada con exito"})
    else:
        form = EditorialForm()
    return render(request, 'agregar_editorial.html', {'form': form})

def show_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'show_libro.html', {'libro': libro})

@user_passes_test(is_super_user)
def edit_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('show_libro', libro_id=libro.id)  # Adjust the redirect to your book detail view
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libro_form.html', {'form': form, 'libro': libro})

@user_passes_test(is_super_user)
def delete_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    libro.delete()
    return redirect('index_libros')