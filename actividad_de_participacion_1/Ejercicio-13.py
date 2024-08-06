print("13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y division")


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

print(f"Suma: {numero1} + {numero2} = {suma}")
print(f"Resta: {numero1} - {numero2} = {resta}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion}")
print(f"División: {numero1} / {numero2} = {division}")
