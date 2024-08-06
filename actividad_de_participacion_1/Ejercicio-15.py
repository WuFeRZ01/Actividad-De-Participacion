print("15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.")

def es_palindromo(cadena):
    
    cadena = cadena.lower().replace(" ", "")  
    return cadena == cadena[::-1]  

texto = input("Ingrese una cadena de texto: ")

if es_palindromo(texto):
    print(f'"{texto}" es un palíndromo.')
else:
    print(f'"{texto}" no es un palíndromo.')