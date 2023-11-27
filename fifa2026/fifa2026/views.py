from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from fifa.forms import CustomUserCreationForm

def index(request):
    return render(request, 'index.html', {
        # context
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('admin:index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{
        # context
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('index')
        # context

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Usuario registrado exitosamente')
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

