import json
import os
from DATOS import carga_Datos
from HeapSort import HeapSort
from QuickSort import QuickSort
from MergeSort import MergeSort

#cargar el archivo con los numeros de prueba
test_Data = "test_Data.json"
array = carga_Datos.load_random_numbers(test_Data)

#Definir una ruta absoluta específica para guardar los archivo JSON con los resultados
result = "repo/SortAlgorithms/Results"

# Verificar si el directorio existe y si no créarlo si es necesario
directorio = os.path.dirname(result)
if not os.path.exists(result):
    os.makedirs(result)

#LLAMADO AL MERGE-SORT
mtest_100 = MergeSort.merge_sort(array["cien"].copy())
print(f"Dataset 100\nNumero de pasos MergeSort: {mtest_100[1]}\n Numero de ciclos MergeSort: {mtest_100[2]}\n")
mtest_1000 = MergeSort.merge_sort(array["mil"].copy())
print(f"Dataset 1000\nNumero de pasos MergeSort: {mtest_1000[1]}\n Numero de ciclos MergeSort: {mtest_1000[2]}\n")
mtest_10000 = MergeSort.merge_sort(array["diezmil"].copy())
print(f"Dataset 10000\nNumero de pasos MergeSort: {mtest_10000[1]}\n Numero de ciclos Mergesort: {mtest_10000[2]}\n")

#almacenar en un diccionario los arrays una vez organizados
Merge_drganized_data = {
    "n_cien": mtest_100,
    "n_mil": mtest_1000,
    "n_diezmil": mtest_10000
}

#almacenar el diccionario anterior en un json
with open(os.path.join(result, f"Merge_organized_data.json"), "w") as mfile:
    json.dump(Merge_drganized_data, mfile)


#Llamado QuickSort
qtest_100 = QuickSort.quickSort(array["cien"].copy(),0,len(array["cien"].copy())-1)
print(f"Dataset 100\nNumero de pasos QuickSort: {qtest_100[2]}\n Numero de ciclos QuickSort: {qtest_100[1]}\n")
qtest_1000 = QuickSort.quickSort(array["mil"].copy(),0,len(array["mil"].copy())-1)
print(f"Dataset 1000\nNumero de pasos QuickSort: {qtest_1000[2]}\n Numero de ciclos QuickSort: {qtest_1000[1]}\n")
qtest_10000 = QuickSort.quickSort(array["diezmil"].copy(),0,len(array["diezmil"].copy())-1)
print(f"Dataset 10000\nNumero de pasos QuickSort: {qtest_10000[2]}\n Numero de ciclos QuickSort: {qtest_10000[1]}\n")

#almacenar en un diccionario los arrays una vez organizados
quick_organized_Data = {
    "n_cien": qtest_100,
    "n_mil": qtest_1000,
    "n_diezmil": qtest_10000
}

#almacenar el diccionario anterior en un json
with open(os.path.join(result, f"QuickSort_organized_data.json"), "w") as qfile:
    json.dump(quick_organized_Data, qfile)

#Llamado HeapSort
htest_100 = HeapSort.heap_sort(array["cien"].copy())
print(f"Dataset 100\nNumero de pasos HeapSort: {htest_100[1]}\n Numero de ciclos HeapSort: {htest_100[2]}\n")
htest_1000 = HeapSort.heap_sort(array["mil"].copy())
print(f"Dataset 1000\nNumero de pasos HeapSort: {htest_1000[1]}\n Numero de ciclos HeapSort: {htest_1000[2]}\n")
htest_10000 = HeapSort.heap_sort(array["diezmil"].copy())
print(f"Dataset 10000\nNumero de pasos HeapSort: {htest_10000[1]}\n Numero de ciclos HeapSort: {htest_10000[2]}\n")

#almacenar en un diccionario los arrays una vez organizados
heap_organized_Data = {
    "n_cien": htest_100,
    "n_mil": htest_1000,
    "n_diezmil": htest_10000
}

#almacenar el diccionario anterior en un json
with open(os.path.join(result, f"HeapSort_organized_data.json"), "w") as hfile:
    json.dump(heap_organized_Data, hfile)
