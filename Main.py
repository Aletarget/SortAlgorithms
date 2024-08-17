import time
from DATOS import carga_Datos
from HeapSort import HeapSort
from QuickSort import QuickSort
from MergeSort import MergeSort

datos100 = "100datos.json"
datos1000 = "1000datos.json"
datos10000 = "10000datos.json"

array = carga_Datos.load_random_numbers(datos100)

#LLAMADO AL MERGE-SORT

inicio = time.perf_counter_ns() #Conteo en nanosegundos para comenzar a contar el tiempo de duracion del algoritmo
MergeSort.merge_sort(array)
fin = time.perf_counter_ns()
tiempoFinal = (fin - inicio)/pow(10,6) #Conversion de nanosegundos a milisegundos
print("Tiempo total para ordenar los datos mediante el metodo Merge Sort: ", tiempoFinal , "ms\n")
print(array)

