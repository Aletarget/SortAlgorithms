def partition(array, low, high):
    pivot = array[high]  # Elegir el último elemento como pivote
    i = low - 1  # Índice del elemento más pequeño
    
    for j in range(low, high):
        # Si el elemento actual es menor o igual que el pivote
        if array[j] <= pivot:
            i += 1  # Incrementar el índice del elemento más pequeño
            array[i], array[j] = array[j], array[i]  # Intercambiar
            
    # Colocar el pivote en la posición correcta
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1  # Retornar la posición del pivote

def quickSort(array, low, high):
    if low < high:
        # Particionar el array y obtener el índice del pivote
        pi = partition(array, low, high)
        
        # Ordenar los elementos por separado antes y después de la partición
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    
    return array

