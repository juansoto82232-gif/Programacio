"""
═══════════════════════════════════════════════════════════════════════════════
        TALLER: ANÁLISIS DE ALGORITMOS
        Algoritmos y Programación 4
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES GENERALES:
------------------------
- Entregar archivo .py con todas las secciones resueltas
- El código debe ejecutar sin errores

DISTRIBUCIÓN:
- Sección A: Análisis teórico (1.0)         
- Sección B: Investigación (0.5)             
- Sección C: Resolver y optimizar (2.0)      
- Sección D: Proponer y justificar (1.5)     

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN A: ANÁLISIS TEÓRICO (1.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO A.1 (0.4): Clasificar complejidad

Para cada función, escribe:
  - La complejidad Big-O
  - UNA línea explicando por qué

Escribe tus respuestas como comentarios debajo de cada función.
"""


def alpha(lista):
    total = 0
    for x in lista:
        total += x
    promedio = total / len(lista)
    return promedio

# Complejidad: O(n)
# Porque: El bucle recorre cada elemento de la lista una vez (O(n)), y las operaciones dentro del bucle son O(1).


def beta(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                return True
    return False

# Complejidad: O(n²)
# Porque: El bucle anidado recorre cada par de elementos de la lista (O(n) * O(n) = O(n²)), 
# y las operaciones dentro de los bucles son O(1).


def gamma(n):
    if n <= 1:
        return 1
    return gamma(n // 2) + 1

# Complejidad: O(log n)
# Porque: La función se llama recursivamente log_2(n) veces, y cada llamada realiza una operación constante.


def delta(lista):
    resultado = set()
    for x in lista:
        resultado.add(x)
    return resultado

# Complejidad: O(n)
# Porque: El bucle recorre cada elemento de la lista una vez (O(n)), 
# y la operación de agregar a un set es O(1) en promedio, por lo que la complejidad total es O(n).


def epsilon(lista):
    for x in lista:
        if x in lista:
            pass

# Complejidad: O(n²)
# Porque: El bucle for recorre cada elemento de la lista (O(n)), 
# y dentro del bucle se realiza una operación de búsqueda (x in lista) que también es O(n), 
# lo que resulta en O(n * n) = O(n²).
# PISTA: ¿cuánto cuesta `x in lista`?


def zeta(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 3

# Complejidad: O(log n)
# Porque: El bucle while se ejecuta log_3(n) veces, ya que j se multiplica por 3 en cada iteración.


def eta(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = eta(lista[:medio])
    der = eta(lista[medio:])
    return izq + der

# Complejidad: O(n log n)
# Porque: El algoritmo divide la lista en dos mitades log n veces (debido a la recursión), 
# y cada nivel de recursión procesa toda la lista (O(n)) al combinar los resultados.
# PISTA: ¿cuánto cuesta lista[:medio]?


def theta(n):
    i = 1
    while i * i <= n:
        i += 1
    return i

# Complejidad: O(√n)
# Porque: El bucle se ejecuta hasta que i * i > n, lo que significa que i es aproximadamente √n.


"""
PUNTO A.2 (0.3): Ordenar de menor a mayor complejidad

Ordena las siguientes complejidades de la MÁS RÁPIDA a la MÁS LENTA:

O(n!), O(1), O(n log n), O(2^n), O(n²), O(log n), O(n), O(n³), O(√n)

Tu respuesta (de más rápida a más lenta):
1. O(1) '''Tiempo constante'''
2. O(log n)'''Tiempo logaritmico'''
3. O(√n)'''Tiempo raíz cuadrada'''
4. O(n)'''Tiempo lineal'''
5. O(n log n)'''Tiempo linealítmico'''
6. O(n²)'''Tiempo cuadrático'''
7. O(n³)'''Tiempo cúbico'''
8. O(2^n)'''Tiempo exponencial'''
9. O(n!)'''Tiempo factorial el más lento, crece muchísimo incluso para valores pequeños de n'''
"""


"""
PUNTO A.3 (0.3): Verdadero o Falso

Escribe V o F y justifica brevemente las falsas.

1. F O(2n) es más lento que O(n)
   Justificación: Su complejidad es igual sabiendo que en big-O se ignoran las constantes, entonces O(2n) = O(n).

2. V Un algoritmo O(n²) siempre es más lento que uno O(n log n)
   Justificación: En el n log n combina lineal y logaritmico que es mas eficiente que el cuadratico.

3. F Si un algoritmo tiene un for de n y dentro un for de 5,
       su complejidad es O(n²)
   Justificación: No seria la complejidad O(n²) vendria siendo O(n)

4. F `x in set` tiene la misma complejidad que `x in list`
   Justificación: `x in set` tiene complejidad O(1) en promedio, mientras que `x in list` tiene complejidad O(n).

5. F Un algoritmo recursivo que se llama a sí mismo 2 veces
       siempre es O(2^n)
   Justificación: No necesariamente, depende de cómo se divida el problema. 
   Por ejemplo, el algoritmo de búsqueda binaria se llama a sí mismo una vez y tiene complejidad O(log n), 
   mientras que el algoritmo de Fibonacci se llama a sí mismo dos veces y tiene complejidad O(2^n).

6. F O(n) + O(n²) = O(n³)
   Justificación: No es igual por temas del algebra
    y en la teoria del big-O se deja el polinomio de mayor exponenete osea O(n) + O(n²) = O(n²)

7. V La complejidad espacial de un algoritmo in-place es O(1)
   Justificación: El algortimo in_place realiza su tarea utilizando una cantidad constante.

8. V Memorización mejora la complejidad temporal pero empeora la espacial
   Justificación: La memorización almacena resultados previamente calculados, 
   lo que reduce el tiempo de ejecución en llamadas repetidas, pero requiere 
   espacio adicional para almacenar estos resultados.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN B: INVESTIGACIÓN (0.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO B.1 (0.25): Complejidad de operaciones de Python

Investiga y completa la tabla con la complejidad de cada operación.
Agrega una justificación de por qué es la complejidad.
Puedes consultar: https://wiki.python.org/moin/TimeComplexity

┌──────────────────────────────┬──────────────┬──────────────┐
│ Operación                    │ Lista []     │ Set/Dict {}  │
├──────────────────────────────┼──────────────┼──────────────┤
│ Acceder por índice [i]       │ O(1)         │ N/A          │
│ Buscar elemento (x in ...)   │ O(n)         │ O(1)         │
│ Agregar al final (.append)   │ O(1)         │ O(1) (.add)  │
│ Insertar al inicio           │ O(n)         │ N/A          │
│ Eliminar por valor (.remove) │ O(n)         │ O(1)         │
│ Obtener longitud (len)       │ O(1)         │ O(1)         │
│ Ordenar (.sort / sorted)     │ O(n log n)   │ N/A          │
│ Copiar (.copy / [:])         │ O(n)         │ O(n)         │
└──────────────────────────────┴──────────────┴──────────────┘
"""


"""
PUNTO B.2 (0.25): Caso real

Investiga y responde:

1. ¿Qué algoritmo de ordenamiento usa Python internamente (sorted/list.sort)?
   Respuesta: Timsort:Para ordenar listas cuando usas la función sorted() o el método .sort(). 
   Este algoritmo es eficiente, estable y está optimizado 
   para aprovechar el orden parcial que suelen tener los datos en la práctica.

2. ¿Cuál es su complejidad en el mejor, peor y caso promedio?
   Mejor: O(n)
   Peor: O(n!)
   Promedio: O(n log n)

3. ¿Por qué Python eligió ese algoritmo y no Quick Sort?
   Respuesta:Por estabilidad,optimización para datos parcialmente ordenados,rendimiento consistente,peor caso garantizado.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN C: RESOLVER Y OPTIMIZAR (2.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
En cada problema:
1. Analiza la versión LENTA y escribe su complejidad
2. Implementa la versión RÁPIDA
3. Escribe la complejidad de tu versión
4. Ejecuta las pruebas para verificar que funciona
"""


# ─── PROBLEMA C.1 (0.4): Elementos únicos ────────────────────────────────────

def unicos_lento(lista):
    """
    Retorna lista sin duplicados manteniendo el orden.
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado


def unicos_rapido(lista):
    """
    Misma funcionalidad pero más eficiente.
    USA un set auxiliar para búsqueda O(1).

    TODO: Implementar
    COMPLEJIDAD: O(n) porque se recorre la lista una vez (O(n)) 
    y las operaciones de búsqueda y adición al set son O(1) en promedio,
    """
    resultado = []
    vistos = set()
    for x in lista:
        if x not in vistos:
            vistos.add(x)
            resultado.append(x)
    return resultado
pass


# ─── PROBLEMA C.2 (0.4): Frecuencia del más común ────────────────────────────

def mas_comun_lento(lista):
    """
    Retorna el elemento que más se repite y cuántas veces.
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    max_elem = None
    max_count = 0
    for x in lista:
        count = 0
        for y in lista:
            if y == x:
                count += 1
        if count > max_count:
            max_count = count
            max_elem = x
    return max_elem, max_count


def mas_comun_rapido(lista):
    """
    Misma funcionalidad usando diccionario contador.

    TODO: Implementar
    COMPLEJIDAD: O(n) porque se recorre la lista una vez para contar y 
    luego se recorre el diccionario de conteos,
    """
    conteos = {}
    for x in lista:
        conteos[x] = conteos.get(x, 0) + 1

    max_elem = None
    max_count = 0
    for elem, count in conteos.items():
        if count > max_count:
            max_count = count
            max_elem = elem

    return max_elem, max_count
pass


# ─── PROBLEMA C.3 (0.4): Pares que suman K ───────────────────────────────────

def pares_suma_lento(lista, k):
    """
    Retorna todos los pares (i, j) donde lista[i] + lista[j] == k.
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))
    return pares


def pares_suma_rapido(lista, k):
    """
    Misma funcionalidad usando set para buscar complementos.

    Estrategia:
    - Para cada x, el complemento es k - x
    - Si el complemento ya está en un set de "vistos", es un par

    TODO: Implementar
    COMPLEJIDAD: O(n) porque se recorre la lista una vez, 
    y las operaciones de búsqueda y adición al set son O(1) en promedio,
    """
    pares = []
    vistos = set()
    for x in lista:
        complemento = k - x
        if complemento in vistos:
            pares.append((complemento, x))
        vistos.add(x)
    return pares
pass


# ─── PROBLEMA C.4 (0.4): Anagramas ───────────────────────────────────────────

def son_anagramas_lento(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas (mismas letras, diferente orden).
    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)


def son_anagramas_rapido(palabra1, palabra2):
    """
    Misma funcionalidad sin ordenar.

    Estrategia: contar frecuencia de cada letra con diccionario.

    TODO: Implementar
    COMPLEJIDAD: O(n) porque se recorre cada palabra una vez para contar las letras,
    y luego se comparan los conteos, lo que también es O(n).
    """
    if len(palabra1) != len(palabra2):
        return False
    conteo1 = {}
    conteo2 = {}
    for c in palabra1:
        conteo1[c] = conteo1.get(c, 0) + 1
    for c in palabra2:
        conteo2[c] = conteo2.get(c, 0) + 1
    return conteo1 == conteo2
pass


# ─── PROBLEMA C.5 (0.4): Subarray de suma máxima ─────────────────────────────

def max_subarray_lento(lista):
    """
    Encuentra la suma máxima de un subarray contiguo.
    Ejemplo: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4, -1, 2, 1])

    COMPLEJIDAD: O(?)  ← analiza y escribe
    """
    n = len(lista)
    max_suma = lista[0]
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += lista[k]
            max_suma = max(max_suma, suma)
    return max_suma


def max_subarray_rapido(lista):
    """
    Algoritmo de Kadane: un solo recorrido.

    Idea: mantener la suma actual. Si se vuelve negativa, reiniciar.
    - suma_actual = max(x, suma_actual + x)
    - max_suma = max(max_suma, suma_actual)

    TODO: Implementar
    COMPLEJIDAD: O(n) porque se recorre la lista una vez.
    """
    max_actual = max_global = lista[0]
    for x in lista[1:]:
        max_actual = max(x, max_actual + x)
        max_global = max(max_global, max_actual)
    return max_global
pass


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN D: PROPONER Y JUSTIFICAR (1.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO D.1 (0.5): Diseñar un algoritmo

PROBLEMA: Sistema de autocompletado
Un buscador tiene una lista de 1 millón de palabras. Cuando el usuario
escribe las primeras letras, debe mostrar las 5 palabras que empiezan
con ese prefijo.

Ejemplo:
  palabras = ["python", "programar", "programa", "prueba", "pizza", ...]
  autocompletar("pro") → ["programar", "programa"]

Propón DOS soluciones con diferente complejidad:

SOLUCIÓN 1 (fuerza bruta):
  Descripción: Recorrer toda la lista de palabras y verificar si cada una comienza con el prefijo.
  Complejidad: O(n) porque se recorre toda la lista de palabras una vez, 
  y las operaciones de comparación de prefijo son O(1) en promedio.
  Código:
  
"""


def autocompletar_v1(palabras, prefijo):
    """
    Versión fuerza bruta.
    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    resultado = []
    p = len(prefijo)
    for palabra in palabras:
        # Verificar manualmente si la palabra comienza con el prefijo
        if len(palabra) >= p:
            coincide = True
            for i in range(p):
                if palabra[i] != prefijo[i]:
                    coincide = False
                    break
            if coincide:
                resultado.append(palabra)
                if len(resultado) == 5:
                    break
    return resultado
pass


"""
SOLUCIÓN 2 (optimizada):
  Descripción: Si las palabras están ordenadas, 
  se puede usar búsqueda binaria para encontrar el punto de inicio de las palabras que comienzan con el prefijo, 
  y luego tomar las siguientes 5 palabras.
  Complejidad: O(log n) porque se puede usar búsqueda binaria para encontrar 
  el punto de inicio de las palabras que comienzan con el prefijo,
  ¿Qué estructura de datos usarías? Una lista ordenada de palabras.
  Código:
"""


def autocompletar_v2(palabras_ordenadas, prefijo):
    """
    Versión optimizada.
    PISTA: Si las palabras están ordenadas, puedes usar búsqueda binaria
    para encontrar dónde empiezan las que tienen el prefijo.

    TODO: Implementar
    COMPLEJIDAD: O(log n)
    """
    def busqueda_binaria_primera_ocurrencia(lista, prefijo):
        izquierda = 0
        derecha = len(lista) - 1
        resultado = len(lista)  # posición más allá del final si no se encuentra
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            palabra = lista[medio]
            # Comparamos solo hasta la longitud del prefijo para decidir
            if palabra[:len(prefijo)] >= prefijo:
                resultado = medio
                derecha = medio - 1
            else:
                izquierda = medio + 1
        return resultado

    pos = busqueda_binaria_primera_ocurrencia(palabras_ordenadas, prefijo)
    resultado = []
    n = len(palabras_ordenadas)
    p = len(prefijo)

    for i in range(pos, n):
        palabra = palabras_ordenadas[i]
        if palabra[:p] == prefijo:
            resultado.append(palabra)
            if len(resultado) == 5:
                break
        else:
            break
    return resultado
pass


"""
PUNTO D.2 (0.5): Analizar un sistema real

ESCENARIO: Red social con 10 millones de usuarios.
Cada usuario tiene una lista de amigos (promedio 200 amigos).

Analiza la complejidad de estas operaciones y propón la mejor
estructura de datos para cada una:


1. Verificar si dos usuarios son amigos
   - Con lista de amigos: O(n),(n=200),Hay que recorrer la lista hasta encontrar al usuario
   - Con set de amigos: O(1),Búsqueda directa por hash
   - ¿Cuál elegirías? Set, porque las consultas son muchísimo más rápidas.

2. Encontrar amigos en común entre dos usuarios
   - Con listas: O(n²),Comparar cada elemento de una lista con la otra
   - Con sets: O(n),Intersección de conjuntos
   - ¿Cuál elegirías? Set, porque reduce drásticamente el tiempo.

3. Sugerir "personas que quizás conozcas" (amigos de amigos que no son tus amigos)
   - Describe tu algoritmo: Para un usuario U, recorrer sus amigos (≈ 200)
    Para cada amigo A, recorrer sus amigos (≈ 200)
    Agregar candidatos si:
    No es U
    No ya es amigo de U
    (Opcional) Contar cuántas veces aparece cada candidato (ranking)
   - Complejidad estimada: O(k²),
   - ¿Es viable para 10M de usuarios? ,No si lo haces en tiempo real para todos,Si Se calcula solo cuando el usuario entra
    Se usa cache
    O se hace offline (batch processing)

4. Si cada usuario tiene en promedio 200 amigos y hay 10M de usuarios:
   - ¿Cuánta memoria ocupa almacenar TODAS las relaciones de amistad?,10M usuarios
    200 amigos promedio
    Total de relaciones:
    10M×200=2,000M=2×10^9 conexiones
    Cada relación se guarda dos veces (A→B y B→A)
   - Con lista: ___ bytes aproximadamente
   Cada ID ≈ 4 bytes (int)
    Total:
    2×10^9 ×4≈8 GB
    Respuesta: ≈ 8 GB
   - Con set: ___ bytes aproximadamente
    Overhead de hash (punteros, buckets, etc.)
    Aproximadamente 2–3x más memoria
    ≈16–24 GB
    Respuesta: ≈ 20 GB (aprox)
"""


"""
PUNTO D.3 (0.5): Reflexión y comparación

Escribe un párrafo (mínimo 5 líneas) respondiendo:

¿Por qué es importante analizar la complejidad de un algoritmo
ANTES de implementarlo? Da un ejemplo concreto de un caso donde
elegir el algoritmo incorrecto podría causar problemas reales
(tiempo de espera, costos de servidor, mala experiencia de usuario, etc.)

Tu respuesta:
Analizar la complejidad de un algoritmo antes de implementarlo es fundamental para garantizar que el programa sea eficiente
 y escalable, especialmente cuando se trabaja con grandes volúmenes de datos. 
 Conocer la complejidad permite anticipar el tiempo y los recursos que el algoritmo consumirá, 
 evitando sorpresas desagradables como tiempos de espera excesivos o sobrecarga en los servidores. 
 Por ejemplo, en un sistema de búsqueda en línea con millones de usuarios, 
 elegir un algoritmo de búsqueda con complejidad cuadrática (O(n²)) en lugar de uno logarítmico (O(log n)) 
 puede provocar retrasos significativos, afectando la experiencia del usuario y aumentando los costos operativos 
 por la necesidad de más infraestructura. Además, un análisis previo ayuda a seleccionar la solución más adecuada 
 para el problema, optimizando el rendimiento y la satisfacción del usuario final. En resumen, 
 a evaluación de la complejidad es clave para diseñar software eficiente, confiable y rentable.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                         CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

def medir(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    return resultado, time.time() - inicio


if __name__ == "__main__":
    print("=" * 70)
    print("     TALLER: ANÁLISIS DE ALGORITMOS - PRUEBAS SECCIÓN C")
    print("=" * 70)

    # ── C.1: Únicos ──────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.1: ELEMENTOS ÚNICOS")
    print("─" * 70)

    for n in [1000, 5000, 10000]:
        lista = [random.randint(1, n // 2) for _ in range(n)]

        r1, t1 = medir(unicos_lento, lista)
        r2, t2 = medir(unicos_rapido, lista) if unicos_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓ correcto" if r1 == r2 else f"  ✗ DIFERENTE")
        else:
            print("  (sin implementar)")

    # ── C.2: Más común ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.2: ELEMENTO MÁS COMÚN")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 20) for _ in range(n)]

        r1, t1 = medir(mas_comun_lento, lista)
        r2, t2 = medir(mas_comun_rapido, lista) if mas_comun_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓" if r1 == r2 else f"  resultado: {r1} vs {r2}")
        else:
            print("  (sin implementar)")

    # ── C.3: Pares que suman K ───────────────────────────────────
    print("\n" + "─" * 70)
    print("C.3: PARES QUE SUMAN K")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 100) for _ in range(n)]
        k = 50

        r1, t1 = medir(pares_suma_lento, lista, k)
        r2, t2 = medir(pares_suma_rapido, lista, k) if pares_suma_rapido(lista, k) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  pares encontrados: {len(r1)} vs {len(r2)}")
        else:
            print("  (sin implementar)")

    # ── C.4: Anagramas ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.4: ANAGRAMAS")
    print("─" * 70)

    casos_anagramas = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("python", "typhon", True),
        ("abc", "abcd", False),
    ]

    for p1, p2, esperado in casos_anagramas:
        r_lento = son_anagramas_lento(p1, p2)
        r_rapido = son_anagramas_rapido(p1, p2) if son_anagramas_rapido(p1, p2) is not None else "N/A"
        marca = "✓" if r_rapido == esperado else "✗"
        print(f"  {marca} '{p1}' vs '{p2}': lento={r_lento}, rápido={r_rapido}, esperado={esperado}")

    # ── C.5: Subarray máximo ─────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.5: SUBARRAY DE SUMA MÁXIMA")
    print("─" * 70)

    casos_subarray = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [5, -9, 6, -2, 3],
    ]

    for lista in casos_subarray:
        r_lento = max_subarray_lento(lista)
        r_rapido = max_subarray_rapido(lista)
        marca = "✓" if r_rapido == r_lento else "✗"
        print(f"  {marca} {lista} → lento={r_lento}, rápido={r_rapido}")

    for n in [500, 2000, 5000]:
        lista = [random.randint(-50, 50) for _ in range(n)]
        r1, t1 = medir(max_subarray_lento, lista)
        r2, t2 = medir(max_subarray_rapido, lista) if max_subarray_rapido(lista) is not None else (None, 0)
        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s")

    # ── D.1: Autocompletar ───────────────────────────────────────
    print("\n" + "─" * 70)
    print("D.1: AUTOCOMPLETAR")
    print("─" * 70)

    palabras = [f"palabra_{random.randint(1000, 9999)}" for _ in range(50000)]
    palabras.extend(["python", "programar", "programa", "prueba", "pizza",
                      "proyecto", "profesor", "promedio", "proceso", "producir"])
    random.shuffle(palabras)
    palabras_ord = sorted(palabras)

    for prefijo in ["pro", "pyt", "piz", "xyz"]:
        r1, t1 = medir(autocompletar_v1, palabras, prefijo) if autocompletar_v1(palabras, prefijo) is not None else (None, 0)
        r2, t2 = medir(autocompletar_v2, palabras_ord, prefijo) if autocompletar_v2(palabras_ord, prefijo) is not None else (None, 0)

        print(f"  Prefijo '{prefijo}': v1={t1:.4f}s  v2={t2:.4f}s", end="")
        if r1:
            print(f"  → {len(r1)} resultados")
        else:
            print("  (sin implementar)")