print("9. Crear un programa que genere una matriz de números y la imprima en pantalla. ")

import random

def generar_matriz(filas, columnas, rango_inicio, rango_fin):
    
    
    matriz = [
        [random.randint(rango_inicio, rango_fin) for _ in range(columnas)]
        for _ in range(filas)
    ]
    return matriz

def imprimir_matriz(matriz):
    
    for fila in matriz:
        print(" ".join(map(str, fila)))

filas = 4           
columnas = 5        
rango_inicio = 1    
rango_fin = 100     

matriz = generar_matriz(filas, columnas, rango_inicio, rango_fin)

print("Matriz generada:")
imprimir_matriz(matriz)
