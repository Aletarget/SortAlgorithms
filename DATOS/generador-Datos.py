import random
import json
import os

def generate_random_numbers(count, filename):
    # Generar una lista de números aleatorios
    random_numbers = [random.randint(1, count) for _ in range(count)]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    route = os.path.join(script_dir,filename) #Guardar la ruta de la carpeta en la que se encuentra el generador-Datos.py
    # Guardar la lista en un archivo .json
    with open(route, 'w') as file:
        json.dump(random_numbers, file, indent=4)
    print(f"{filename} generado con {count} números aleatorios.")

# Generar los archivos con diferentes cantidades de números aleatorios
generate_random_numbers(100, 'random_numbers_100.json')
generate_random_numbers(1000, 'random_numbers_1000.json')
generate_random_numbers(10000, 'random_numbers_10000.json')