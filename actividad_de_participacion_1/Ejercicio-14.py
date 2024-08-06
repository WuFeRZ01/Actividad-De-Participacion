print("14. Escribir una función que calcule la media aritmética de una lista de números. ")

def calcular_media(lista_numeros):
    
    if not lista_numeros:  
        raise ValueError("La lista está vacía. No se puede calcular la media.")
    
    suma = sum(lista_numeros)  
    cantidad = len(lista_numeros) 
    
    media = suma / cantidad  
    return media


numeros = [10, 20, 30, 40, 50]
print(f"La media aritmética es: {calcular_media(numeros)}")