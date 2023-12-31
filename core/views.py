from django.shortcuts import render, redirect, get_object_or_404
from .models import CreateUserForm,FormAuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Se deben crear funciones para que daran la inteligencia al programa 


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": CreateUserForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {"form": CreateUserForm, "error": "Usuario ya existe."})

        return render(request, 'signup.html', {"form": CreateUserForm, "error": "Las contraseñas no coinciden."})

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": FormAuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": FormAuthenticationForm, "error": "Usuario o contraseña son incorrectos."})

        login(request, user)
        return redirect('home')

@login_required
def signout(request):
    logout(request)
    return redirect('home')