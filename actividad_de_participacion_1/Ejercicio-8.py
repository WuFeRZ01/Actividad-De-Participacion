print("8. Crear una función que invierta el orden de los elementos en una lista dada. ")

def invertir_lista(lista):
    
    return lista[::-1]

lista_original = [1, 2, 3, 4, 5]

lista_invertida = invertir_lista(lista_original)

print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)