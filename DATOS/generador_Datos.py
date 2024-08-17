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

# Generar los archivos con diferentes cantidades de números aleatorios
generate_random_numbers(100, '100datos.json')
generate_random_numbers(1000, '1000datos.json')
generate_random_numbers(10000, '10000datos.json')