def quickSort(array):
    steps = 0
    cycles = 0
    for i in range(len(array)):
        min_idx = i
        steps += 1
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    print(f"QuickSort Pasos: {steps}\n QuickSort Ciclos: {cycles}")
    return array
