print("7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.")

def encontrar_maximo_minimo(lista):
    
    if not lista:
        raise ValueError("La lista está vacía")
    
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo


entrada = input("Ingrese números separados por espacios: ")


try:
    numeros = list(map(float, entrada.split()))
    maximo, minimo = encontrar_maximo_minimo(numeros)
    print(f"El número más grande en la lista es: {maximo}")
    print(f"El número más pequeño en la lista es: {minimo}")
except ValueError as e:
    print(f"Error: {e}")