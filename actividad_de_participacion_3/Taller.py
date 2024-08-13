print("1.Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.")

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def __str__(self):
        return f"Vehículo con velocidad máxima de {self.velocidad_maxima} km/h y {self.kilometraje} km de kilometraje."

    def actualizar_kilometraje(self, nuevo_kilometraje):
        if nuevo_kilometraje >= self.kilometraje:
            self.kilometraje = nuevo_kilometraje
        else:
            print("El kilometraje no puede ser menor que el actual.")

    def acelerar(self, incremento):
        print(f"El vehículo está acelerando. Velocidad actual incrementada en {incremento} km/h.")


mi_vehiculo = Vehiculo(251, 15512)
print(mi_vehiculo)

mi_vehiculo.actualizar_kilometraje(17002)
print(mi_vehiculo)

mi_vehiculo.acelerar(75)


print("Cree una clase Punto que represente un punto en el plano cartesiano.")


import math

class Punto:
    def __init__(self, x=0, y=0):
        
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def trasladar(self, dx, dy):
        
        self.x += dx
        self.y += dy

    def distancia_a(self, otro_punto):
        
        return math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)


punto1 = Punto(3, 4)
punto2 = Punto(6, 8)


print("Punto 1:", punto1)  
print("Punto 2:", punto2)  


punto1.trasladar(2, -1)
print("Punto 1 trasladado:", punto1)  


distancia = punto1.distancia_a(punto2)
print(f"Distancia entre Punto 1 y Punto 2: {distancia:.2f}")  

print("A la clase del punto anterior, defínale los siguientes métodos")

import math

class Punto:
    def __init__(self, x=0, y=0):
        
        self.x = x
        self.y = y

    def __str__(self):
        
        return f'({self.x}, {self.y})'

    def mostrar(self):
        
        print(f'Punto: ({self.x}, {self.y})')

    def mover(self, nuevo_x, nuevo_y):
        
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro):
        
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt(dx**2 + dy**2)

p1 = Punto(1, 2)
p2 = Punto(4, 6)

p1.mostrar()
p2.mostrar()

p1.mover(3, 4)
print("Después de mover p1:")
p1.mostrar()

distancia = p1.calcular_distancia(p2)
print(f'Distancia entre p1 y p2: {distancia}')


print("4.Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas.") 
print("Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.")

class Rectangulo:
    def __init__(self, punto1, punto2):
        
        self.x1, self.y1 = punto1
        self.x2, self.y2 = punto2

    def calcular_perimetro(self):
        
        ancho = abs(self.x2 - self.x1)
        alto = abs(self.y2 - self.y1)
        return 2 * (ancho + alto)

    def calcular_area(self):
        
        ancho = abs(self.x2 - self.x1)
        alto = abs(self.y2 - self.y1)
        return ancho * alto

    def es_cuadrado(self):
        
        ancho = abs(self.x2 - self.x1)
        alto = abs(self.y2 - self.y1)
        return ancho == alto

rect = Rectangulo((1, 2), (4, 6))

print(f"Perímetro: {rect.calcular_perimetro()}")
print(f"Área: {rect.calcular_area()}")
print(f"Es cuadrado: {rect.es_cuadrado()}")

print("5.Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no")


import math

class Circulo:
    def __init__(self, centro, radio):
        
        self.x_centro, self.y_centro = centro
        self.radio = radio

    def calcular_area(self):
        
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        
        return 2 * math.pi * self.radio

    def punto_pertenece(self, punto):
        
        x, y = punto
        distancia_centro = math.sqrt((x - self.x_centro) ** 2 + (y - self.y_centro) ** 2)
        return distancia_centro <= self.radio

circulo = Circulo((0, 0), 5)

print(f"Área: {circulo.calcular_area():.2f}")
print(f"Perímetro: {circulo.calcular_perimetro():.2f}")

punto = (3, 4)
print(f"El punto {punto} pertenece al círculo: {circulo.punto_pertenece(punto)}")

punto_exterior = (6, 6)
print(f"El punto {punto_exterior} pertenece al círculo: {circulo.punto_pertenece(punto_exterior)}")

print("6.Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta")

class Carta:
    
    PINTA_TREBOLES = "Tréboles"
    PINTA_DIAMANTES = "Diamantes"
    PINTA_CORAZONES = "Corazones"
    PINTA_PICAS = "Picas"
    
    def __init__(self, valor, pinta):
        
        self.valor = valor
        self.pinta = pinta

    def __str__(self):
        
        return f"{self.valor} de {self.pinta}"

carta1 = Carta('A', Carta.PINTA_TREBOLES)
carta2 = Carta('10', Carta.PINTA_DIAMANTES)

print(carta1)  
print(carta2)  

print("7.Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros")

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def __str__(self):
        
        propietarios_str = ', '.join(self.propietarios)
        return (f"Número de cuenta: {self.numero_cuenta}\n"
                f"Propietarios: {propietarios_str}\n"
                f"Balance: {self.balance:.2f}")
    


    def depositar(self, cantidad):
        
        if cantidad <= 0:
            return "La cantidad a depositar debe ser mayor que cero."
        
        self.balance += cantidad
        return f"Depósito exitoso. El nuevo balance es: {self.balance:.2f}"

    def __str__(self):
        
        propietarios_str = ', '.join(self.propietarios)
        return (f"Número de cuenta: {self.numero_cuenta}\n"
                f"Propietarios: {propietarios_str}\n"
                f"Balance: {self.balance:.2f}")


cuenta = CuentaBancaria('58033833430', ['Samuel Zapata', 'Maia N'], 14.000)

print(cuenta)
print(cuenta.depositar(500.00))  # Depósito exitoso
print(cuenta.depositar(-100.00)) # Error en el depósito

print(cuenta)  


cuenta = CuentaBancaria('58033833430', ['Samuel Zapata', 'Maia N'], 14.000)

print(cuenta)


print("8.Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta")


print(" El punto 8 está contenido en el punto 7 ^^")

print("9.")

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def retirar(self, cantidad):
        
        if cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
            return False
        elif cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
            return False
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}. Saldo restante: {self.saldo}.")
            return True

    def consultar_saldo(self):
        
        print(f"Saldo actual: {self.saldo}")


cuenta = CuentaBancaria("Samuel Zapata", 14000)
cuenta.consultar_saldo()  
cuenta.retirar(150)       
cuenta.consultar_saldo()  
cuenta.retirar(900)       


print("10.")


class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    def retirar(self, cantidad):        
        if cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
            return False
        elif cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
            return False
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}. Saldo restante: {self.saldo}.")
            return True
    def aplicar_cuota_manejo(self):
        porcentaje = 0.02
        cuota = self.saldo * porcentaje
        self.saldo -= cuota
        print(f"Se ha aplicado una cuota de manejo del {porcentaje * 100}%. Monto de la cuota: {cuota}. Saldo restante: {self.saldo}.")
    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

cuenta = CuentaBancaria("Samuel Zapata", 14000)
cuenta.consultar_saldo()  
cuenta.aplicar_cuota_manejo()  
cuenta.consultar_saldo()  

print("11.")

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
            return False
        elif cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
            return False
        else:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad}. Saldo restante: {self.saldo}.")
            return True
    def aplicar_cuota_manejo(self):
        porcentaje = 0.02
        cuota = self.saldo * porcentaje
        self.saldo -= cuota
        print(f"Se ha aplicado una cuota de manejo del {porcentaje * 100}%. Monto de la cuota: {cuota}. Saldo restante: {self.saldo}.")
    def consultar_saldo(self):
        print(f"Saldo actual: {self.saldo}")
    def mostrar_detalles(self):
        print(f"Detalles de la cuenta bancaria:")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo}")
cuenta = CuentaBancaria("Samuel Zapata", 14000)
cuenta.mostrar_detalles()




















































































































