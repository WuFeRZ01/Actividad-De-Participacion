print("2. Escribir una función que calcule el área de un círculo dado su radio. ")
import math

def calcular_area_circulo(radio):
    
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    
    area = math.pi * (radio ** 2)
    return area

radio = 5
print(f"El área del círculo con radio {radio} es {calcular_area_circulo(radio):.2f}")
