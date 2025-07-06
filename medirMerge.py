import time
from mergeSort import merge_sort

def busqueda_secuencial(arreglo, valor):
    for i in range(len(arreglo)):
        if arreglo[i] == valor:
            return i
    return -1

# Función para medir Merge Sort
def medir_merge_sort(arreglo):
    arr = arreglo.copy()  # Para no modificar el original
    
    inicio = time.time()
    merge_sort(arr, 0, len(arr)-1)
    tiempo = time.time() - inicio
    
    print(f"Merge Sort ({len(arr)} elementos): {tiempo:.6f} segundos")
    return tiempo

# Función para medir búsqueda
def medir_busqueda(arreglo, valor):
    inicio = time.time()
    resultado = busqueda_secuencial(arreglo, valor)
    tiempo = time.time() - inicio
    
    print(f"Búsqueda ({len(arreglo)} elementos): {tiempo:.6f} segundos → Índice: {resultado}")
    return tiempo