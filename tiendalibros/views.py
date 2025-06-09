from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def inicio(request):
    if request.user.is_authenticated:
        # Usuario logueado
        return render(request, 'inicio_logueado.html', {
            'usuario': request.user
        })
    else:
        # Usuario no logueado, formulario de login
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

def usuario_logout(request):
    logout(request)
    return redirect('inicio')
