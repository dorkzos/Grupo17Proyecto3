from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'inicio_logueado.html', {
            'usuario': request.user
        })
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('inicio')
        else:
            form = AuthenticationForm()
        return render(request, 'inicio.html', {'form': form})

def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registrarse.html', {'form': form})

def usuario_logout(request):
    logout(request)
    return redirect('inicio')
