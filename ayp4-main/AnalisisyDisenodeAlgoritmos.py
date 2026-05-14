#Solucion algortimica
#Sean P un problmea algoritmico y A un algoritmo. Se dice que A resuelve(o es una solucion) P
#si y solo si A calcula una respuesta correcta para cada una de las instancias de P. Es decir, 
#A resuelve P si y solo si A resuelve cada instancia de P.
#Ejemplo: El algoritmo de ordenamiento por burbuja resuelve el problema de orden
#Ordenamiento, ya que para cada instancia de ordenamiento, 
#El algoritmo de ordenamiento por burbuja calcula una respuesta correcta.
#-----------------Estudio-----------------#
#Analisis asintótico Y todo lo que tenga 
#Estudiar como crece un codigo cualquiera
#----------------fin----------------#
#Algortimos
def elegir(arr):
    if arr is not None:
        return arr[0]
    return None
def elegir(arr,elem):#tiene un creciemiento lineal
    for i in range (len(arr)):
        if arr[i]==elem:
            return True
    return False
#-------------------
def tiene_duplicados(lista):
    n = len(lista)
    for i in range (n):
        for j in range (i+1,n):
            if lista[i] == lista[j]:
                return True
    return False
#hacer un algortimo que me diga cual es el elemento que mas se repite en la lista
#hacerlo que la i se compare con la lista y al hallar el elemento repetido salga
lista=[3,5,2,1,3]
def elemento_mas_repetido(lista):
    for i in range():
       for j in range():   
#pendiente de terminar                   
#metodo del profe 
def elemento_mas_repetido(lista):
    max_elemento=lista[0]
    max_conteo=0
    for i in range (len(lista)):
        conteo=0
        for j in range (len(lista)):
            if lista[i]== lista[j]:
                conteo +=1
        if conteo > max_conteo:
            max_conteo=conteo
            max_elemento=lista[i]
    return max_elemento,max_conteo
#por diccionario
def elemento_mas_repetido(lista):
    frecuencias={}     
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] +=1
        else:
            frecuencias[elemento]=0
    max_elemento=0
    max_conteo=0
    for elemento, conteo in frecuencias:
        if conteo > max_conteo:
            max_conteo=conteo
            max_elemento=elemento
    return max_elemento,max_conteo
#hacer un codigo que al sumarlos den 0 con listas 
def elemento_mas_repetido(lista):
    n=len(lista)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if lista[i] + lista[j] + lista[k]==0:
                    return True
    return False
#hacer la solucion mas eficiente
def elemento_mas_repetido(lista):
    lista.sort()
    n=len(lista)
    for i in range(n-2):
        left=i+1
        right=n-1
        while left < right:
            suma=lista[i]+lista[left]+lista[right]
            if suma==0:
                return True
            elif suma < 0:
                left +=1
            else:
                right -=1
    return False


        