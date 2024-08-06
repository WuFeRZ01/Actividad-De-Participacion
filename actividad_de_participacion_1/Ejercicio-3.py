print("3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla. ")

import random

def generar_lista_aleatoria(cantidad, rango_inicio, rango_fin):
    
    lista = [random.randint(rango_inicio, rango_fin) for _ in range(cantidad)]
    return lista


cantidad_de_numeros = 16  
rango_inicio = 1          
rango_fin = 101        


numeros_aleatorios = generar_lista_aleatoria(cantidad_de_numeros, rango_inicio, rango_fin)


print("Lista de números aleatorios:")
print(numeros_aleatorios)

