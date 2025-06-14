from app.models import Libro
from datetime import date

libros = [
    {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "categoria": "Novela", "precio": 120, "fecha_publicacion": date(1967, 5, 30)},
    {"titulo": "1984", "autor": "George Orwell", "categoria": "Ficción", "precio": 90, "fecha_publicacion": date(1949, 6, 8)},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "categoria": "Infantil", "precio": 70, "fecha_publicacion": date(1943, 4, 6)},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "categoria": "Novela", "precio": 150, "fecha_publicacion": date(1605, 1, 16)},
    {"titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "categoria": "Ficción", "precio": 85, "fecha_publicacion": date(1953, 10, 19)},
    {"titulo": "Crónica de una muerte anunciada", "autor": "Gabriel García Márquez", "categoria": "Novela", "precio": 95, "fecha_publicacion": date(1981, 3, 1)},
    {"titulo": "Orgullo y prejuicio", "autor": "Jane Austen", "categoria": "Novela", "precio": 110, "fecha_publicacion": date(1813, 1, 28)},
    {"titulo": "El Hobbit", "autor": "J.R.R. Tolkien", "categoria": "Ficción", "precio": 130, "fecha_publicacion": date(1937, 9, 21)},
    {"titulo": "La Odisea", "autor": "Homero", "categoria": "Historia", "precio": 100, "fecha_publicacion": date(800, 1, 1)},
    {"titulo": "Moby Dick", "autor": "Herman Melville", "categoria": "Novela", "precio": 105, "fecha_publicacion": date(1851, 10, 18)},
    {"titulo": "Rayuela", "autor": "Julio Cortázar", "categoria": "Novela", "precio": 125, "fecha_publicacion": date(1963, 6, 28)},
    {"titulo": "El Aleph", "autor": "Jorge Luis Borges", "categoria": "Filosofia", "precio": 80, "fecha_publicacion": date(1949, 1, 1)},
    {"titulo": "Ensayo sobre la ceguera", "autor": "José Saramago", "categoria": "Novela", "precio": 115, "fecha_publicacion": date(1995, 1, 1)},
    {"titulo": "Pedro Páramo", "autor": "Juan Rulfo", "categoria": "Novela", "precio": 90, "fecha_publicacion": date(1955, 3, 19)},
    {"titulo": "El amor en los tiempos del cólera", "autor": "Gabriel García Márquez", "categoria": "Novela", "precio": 120, "fecha_publicacion": date(1985, 9, 5)},
    {"titulo": "La sombra del viento", "autor": "Carlos Ruiz Zafón", "categoria": "Novela", "precio": 130, "fecha_publicacion": date(2001, 4, 12)},
    {"titulo": "Los detectives salvajes", "autor": "Roberto Bolaño", "categoria": "Novela", "precio": 140, "fecha_publicacion": date(1998, 1, 1)},
    {"titulo": "El túnel", "autor": "Ernesto Sabato", "categoria": "Novela", "precio": 100, "fecha_publicacion": date(1948, 1, 1)},
    {"titulo": "La casa de los espíritus", "autor": "Isabel Allende", "categoria": "Novela", "precio": 120, "fecha_publicacion": date(1982, 1, 1)},
    {"titulo": "Cuentos de la selva", "autor": "Horacio Quiroga", "categoria": "Infantil", "precio": 75, "fecha_publicacion": date(1918, 1, 1)},
]

for libro in libros:
    Libro.objects.get_or_create(**libro)
print("Libros agregados correctamente.")
