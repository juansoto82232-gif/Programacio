#Algoritmos de ordenamiento son técnicas utilizadas para organizar elementos en una secuencia específica, 
# generalmente en orden ascendente o descendente. A continuación, 
# se presentan algunos de los algoritmos de ordenamiento más comunes:
#-----Burbuja-----
#algoritmo ejemplo
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
#complejidad temporal: O(n^2) en el peor caso, O(n) en el mejor caso (cuando la lista ya está ordenada).
#complejidad espacial: O(1) (es un algoritmo in-place).porque no requiere espacio adicional significativo.
#estabilidad: Sí, el algoritmo de burbuja es estable porque no cambia el orden relativo de los elementos iguales.
#-----Insercion-----
#algoritmo ejemplo
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
#complejidad temporal: O(n^2) en el peor caso, O(n) en el mejor caso (cuando la lista ya está ordenada).
#complejidad espacial: O(1) (es un algoritmo in-place).
#estabilidad: Sí, el algoritmo de inserción es estable porque no cambia el orden relativo de los elementos iguales.
#-----Merge sort-----
#algoritmo ejemplo
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
#complejidad temporal: O(n log n) en todos los casos.
#complejidad espacial: O(n) debido a la necesidad de espacio adicional para las listas temporales.
#estabilidad: Sí, el algoritmo de merge sort es estable porque no cambia el orden relativo de los elementos iguales.
#-----Heap sort-----
#algoritmo ejemplo
#Primero=arma el heap
#segundo=intercambiar la raiz con el último y 
#luego vuelve a armar el heap con el nuevo primer elemento, repitiendo este proceso hasta que el heap cumpla 
#con la condicion de que los padres sean mayores que sus hijos.
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr
#complejidad temporal: O(n log n) en todos los casos.
#complejidad espacial: O(1) (es un algoritmo in-place).
#estabilidad: No, el algoritmo de heap sort no es estable porque puede cambiar el orden relativo de los elementos iguales.
#-----Counting sort-----
#algoritmo ejemplo
def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range=max_val - min_val + 1
    conteo = [0] * range

    for num in arr:
        conteo[num - min_val] += 1

    for i in range(1, range):
        conteo[num-min_val] += 1

    salida = [0] * len(arr)

    for i in range(len(arr)):    
        arr[i]= salida[1]
#Terminar        

       
#tener en cuenta el rango de los números.
#1=saber el rango.
#2=conteo.
#3=acumular.
#4=empezar a ordenar contanto.
#complejidad temporal: O(n) 
#complejidad espacial: O(k) debido a la necesidad de espacio adicional para el
#Estabilidad: Sí, el algoritmo de counting sort es estable porque no cambia el orden relativo de los elementos iguales.
#-----Radix sort-----
#algoritmo ejemplo
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]
#complejidad temporal: O(d * (n + k)), donde d es el número de dígitos en el número más grande, n es el número de elementos en la entrada y k es el rango de los dígitos (en este caso, 10 para números decimales).
#complejidad espacial: O(n + k) debido a la necesidad de espacio adicional
#Estabilidad: Sí, el algoritmo de radix sort es estable porque no cambia el orden relativo de los elementos iguales.
#-----Quick sort-----
#algoritmo ejemplo
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
#complejidad temporal: O(n log n) en promedio, O(n^2) en el peor caso (cuando la lista ya está ordenada o casi ordenada).
#complejidad espacial: O(log n) en promedio debido a la recursión
#Estabilidad: No, el algoritmo de quick sort no es estable porque puede cambiar el orden relativo de los elementos iguales.     
#-----Bucket sort-----
#algoritmo ejemplo
def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / len(arr)

    buckets = [[] for _ in range(len(arr))]

    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == len(arr):
            index -= 1
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr
#Complejidad temporal: O(n + k), donde n es el número de elementos en la entrada y k es el número de cubetas.
#Complejidad espacial: O(n + k) debido a la necesidad de espacio adicional para las cubetas.
#Estabilidad: Sí, el algoritmo de bucket sort es estable porque no cambia el orden relativo de los elementos iguales.
#-----------------------#
#complejidad temporal,espacial,estabilidad,si es in place o no,inicio,final,medio.
#la estabilidad se refiere a si el algoritmo mantiene el orden relativo de los elementos iguales.
#Burbuja e Insertion




