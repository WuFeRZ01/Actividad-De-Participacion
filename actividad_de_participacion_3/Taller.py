

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



