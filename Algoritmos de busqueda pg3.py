import random
import timeit

# Representación de usuario con una clase
class Usuario:
    def __init__(self, user_id, nombre, edad):
        self.id = user_id
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"Usuario({self.id}, {self.nombre}, {self.edad})"

# Generar 100,000 usuarios automáticamente
nombres = ["Julio", "Alejandro", "Joan", "Manuel", "Maynor", "Emilio", "Estefania", "Mishell"]
usuarios = [Usuario(i, random.choice(nombres), random.randint(18, 80)) for i in range(100000)]

# Algoritmo de Búsqueda lineal
def lineal_search(usuarios, user_id):
    for usuario in usuarios:
        if usuario.id == user_id:
            return usuario
    return None

# Algoritmo de Búsqueda binaria (se requiere lista ordenada)
def binary_search(usuarios, user_id):
    izquierda, derecha = 0, len(usuarios) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if usuarios[medio].id == user_id:
            return usuarios[medio]
        elif usuarios[medio].id < user_id:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return None

# Ordenar usuarios por ID para búsqueda binaria
usuarios.sort(key=lambda x: x.id)

# Permitir al usuario ingresar un ID para buscar
target_id = int(input("Ingrese el ID a buscar: "))

# Medir tiempos
lineal_time = timeit.timeit(lambda: lineal_search(usuarios, target_id), number=1)
binary_time = timeit.timeit(lambda: binary_search(usuarios, target_id), number=1)

usuario_encontrado_lineal = lineal_search(usuarios, target_id)
usuario_encontrado_binaria = binary_search(usuarios, target_id)

print(f"Tiempo de búsqueda lineal: {lineal_time:.6f} segundos")
print(f"Tiempo de búsqueda binaria: {binary_time:.6f} segundos")

if usuario_encontrado_lineal:
    print(f"Usuario encontrado: {usuario_encontrado_lineal}")
else:
    print("Usuario no encontrado.")
