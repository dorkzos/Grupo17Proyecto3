from django import forms
from .models import Libro, Resena  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LibroForm(forms.ModelForm):
    CATEGORIAS = [
        ('Ficción', 'Ficción'),
        ('No Ficción', 'No Ficción'),
        ('Ciencia', 'Ciencia'),
        ('Historia', 'Historia'),
        ('Infantil', 'Infantil'),
        ('Educativo', 'Educativo'),
        ('Filosofia', 'Filosofia'),
        ('Novela', 'Novela'),
        ('Poesía', 'Poesía'),
        ('Enciclopedia', 'Enciclopedia'),
        ('Otro', 'Otro'),
    ]
    categoria = forms.ChoiceField(choices=CATEGORIAS, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'categoria', 'precio']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'precio': forms.NumberInput(),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and int(precio) != precio:
            raise forms.ValidationError('El precio debe ser un número entero.')
        return precio


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['comentario', 'calificacion']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe tu reseña aquí...'}),
            'calificacion': forms.Select(choices=[(1, '1 - Muy mala'), (2, '2'), (3, '3'), (4, '4'), (5, '5 - Muy buena')]),
        }
