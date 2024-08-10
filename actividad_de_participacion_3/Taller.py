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















































































































