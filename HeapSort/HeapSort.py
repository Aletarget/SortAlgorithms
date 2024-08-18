def search_Greatest(array, n, i, steps, cycle):
    largest = i  # Inicializar el mayor como la raíz
    left = 2 * i + 1  # hijo izquierdo = 2*i + 1
    right = 2 * i + 2  # hijo derecho = 2*i + 2
    steps += 3
    # Si el hijo izquierdo es mayor que la raíz
    if left < n and array[left] > array[largest]:
        largest = left
        steps += 3

    # Si el hijo derecho es mayor que el más grande hasta ahora
    if right < n and array[right] > array[largest]:
        largest = right
        steps += 3

    # Si el más grande no es la raíz
    if largest != i:
        cycle += 1
        array[i], array[largest] = array[largest], array[i]  # Intercambiar
        steps += 5
        # Aplicar heapify al subárbol afectado
        steps, cycle = search_Greatest(array, n, largest, steps, cycle)
        
    return steps, cycle
        

def heap_sort(array):
    n = len(array)

    steps = 1
    cycle = 0

    # Construir un max-heap
    for i in range(n // 2 - 1, -1, -1):
        steps += 2
        steps, cycle = search_Greatest(array, n, i, steps, cycle)

    # Extraer elementos uno por uno del heap
    steps +=1
    for i in range(n-1, 0, -1):
        steps += 7
        array[i], array[0] = array[0], array[i]  # Mover la raíz actual al final
        steps, cycle = search_Greatest(array, i, 0, steps, cycle)
        
    return array, steps, cycle