def heapify(array, n, i):
    largest = i  # Inicializar el mayor como la raíz
    left = 2 * i + 1  # hijo izquierdo = 2*i + 1
    right = 2 * i + 2  # hijo derecho = 2*i + 2

    # Si el hijo izquierdo es mayor que la raíz
    if left < n and array[left] > array[largest]:
        largest = left

    # Si el hijo derecho es mayor que el más grande hasta ahora
    if right < n and array[right] > array[largest]:
        largest = right

    # Si el más grande no es la raíz
    if largest != i:
        array[i], array[largest] = array[largest], array[i]  # Intercambiar

        # Aplicar heapify al subárbol afectado
        heapify(array, n, largest)

def heap_sort(array):
    n = len(array)

    # Construir un max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extraer elementos uno por uno del heap
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Mover la raíz actual al final
        heapify(array, i, 0)

    return array