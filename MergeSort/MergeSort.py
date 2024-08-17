def merge_sort(array):
    if len(array) > 1:
        left_array = array[0:len(array)//2]
        right_array = array[len(array)//2:]
        #Uso de recursividad para la division de los arreglos que ya se tienen.
        merge_sort(left_array)
        
        merge_sort(right_array)

        i = 0 # Contador del array izquierdo
        j = 0 # Contador del array derecho
        k = 0
        while i < len(left_array) and j < len(right_array): #Si alguno deja de ser verdad significa que almenos uno de los arreglos ya se asigno al arreglo original
            """
            Comparar si el primer elemento izquierdo de cada array es mayor o menor, si es menor, se aumenta el contador de ese arreglo izquierdo y sí es mayor se aumenta el
            contador del arreglo derecho, y se volveria a realizar la comparacion aumentando en 1 unidad el valor de K ya que es la posicion del arreglo que se va asignando
            """
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        # En el caso de que el anterior bucle while haya terminado, procedera a comprobar si alguno de los dos arreglos tiene elementos por asignar, en este caso solo se 
        # ejecutara un while, no los dos ya que para que se rompa el anterior ciclo, alguno de los dos arreglos tuvo que ser asignado completamente.
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1