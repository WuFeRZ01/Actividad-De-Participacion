print("10. Escribir una función que calcule el factorial de un número dado. ")


def factorial(n):
    
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


print(factorial(5))  
