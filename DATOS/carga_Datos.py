import json
import os
def load_random_numbers(filename):
    # Definir la ruta relativa a la carpeta 'DATOS'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    route = os.path.join(script_dir,filename) #Guardar la ruta de la carpeta en la que se encuentra el generador-Datos.p
    # Leer los datos del archivo .json
    with open(route, 'r') as file:
        data = json.load(file)
    return data