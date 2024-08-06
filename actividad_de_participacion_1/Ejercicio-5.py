print("5. Crear una función que convierta grados Fahrenheit a grados Celsius. ")

def fahrenheit_a_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius


try:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius:.2f} grados Celsius.")
except ValueError:
    print("Por favor, ingrese un valor numérico válido.")