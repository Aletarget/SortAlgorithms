
def partition(array, low, high, cycle, steps):
    pivot = array[high]  # Elegir el último elemento como pivote
    i = low - 1  # Índice del elemento más pequeño
    
    for j in range(low, high):
        cycle += 1
        # Si el elemento actual es menor o igual que el pivote
        if array[j] <= pivot:
            i += 1  # Incrementar el índice del elemento más pequeño
            array[i], array[j] = array[j], array[i]  # Intercambiar
            steps +=5   
            
    # Colocar el pivote en la posición correcta
    array[i + 1], array[high] = array[high], array[i + 1]
    steps += 5

    return i + 1, cycle, steps  # Retornar la posición del pivote

def quickSort(array, low, high, cycle = 0, steps = 0):

    if low < high:
        cycle += 1
        # Particionar el array y obtener el índice del pivote
        pi, cycle, steps = partition(array, low, high, cycle, steps)
        
        # Ordenar los elementos por separado antes y después de la partición
        array, cycle, steps = quickSort(array, low, pi - 1, cycle, steps)
        array, cycle, steps = quickSort(array, pi + 1, high, cycle, steps)
        steps += 3
    
    return array, cycle, steps

