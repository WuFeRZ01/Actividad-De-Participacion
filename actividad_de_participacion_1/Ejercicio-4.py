print("4. Escribir un programa que determine si un número dado es par o impar. ")


def es_par_o_impar(numero):
    
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

try:
    numero = int(input("Ingrese un número entero: "))
    resultado = es_par_o_impar(numero)
    print(f"El número {numero} es {resultado}.")
except ValueError:
    print("Por favor, ingrese un número entero válido.")
