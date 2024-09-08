# Definimos las dimensiones de la matriz 3D
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Suponemos dos semanas para este ejemplo

# Inicializamos la matriz 3D con datos de temperaturas aleatorios
import random

temperaturas = [[[random.randint(10, 30) for _ in range(len(dias))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Imprimir la matriz de temperaturas para verificar los datos generados
for ciudad_index, ciudad in enumerate(ciudades):
    print(f"Temperaturas para {ciudad}:")
    for semana_index in range(semanas):
        print(f"  Semana {semana_index + 1}: {temperaturas[ciudad_index][semana_index]}")
    print()

# Calcular el promedio de temperaturas para cada ciudad por semana
for ciudad_index, ciudad in enumerate(ciudades):
    print(f"Promedios de temperaturas semanales para {ciudad}:")
    for semana_index in range(semanas):
        suma_temperaturas = sum(temperaturas[ciudad_index][semana_index])
        promedio_temperatura = suma_temperaturas / len(dias)
        print(f"  Semana {semana_index + 1}: {promedio_temperatura:.2f}°C")
    print()

