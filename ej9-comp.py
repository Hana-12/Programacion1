from model.Motor import Motor
from model.Coche import Coche as Cocheant

class ExcesoVelocidadException(Exception):
    pass


class Coche(Cocheant):
    motor = Motor(2000,"De combustión","Mercedes Benz")
    velocidad = 0

    def describe_coche(self):
        print(f"El coche es de marca {self.__marca}")
        print(f"El coche es modelo {self.__modelo}")
        print(f"El coche es de tipo {self.__type_car}")
        print("El motor tiene los siguientes detalles:")
        print("Potencia:",self.motor.potencia)
        print("Tipo:",self.motor.tipo)
        print("Marca:",self.motor.marca)

    def incrementarVelocidad(self, velocidad: int):
        self.velocidad = velocidad
        if self.velocidad > 200:
            raise ExcesoVelocidadException(f"{self.velocidad}km/h está por fuera de los límites permitidos")
        else:
            print(f"La nueva velocidad es de {self.velocidad} km/h, disfrute")
    


nuevo_coche = Coche(20,"Campero","Jeep","Wrangler",2025)

nuevo_coche.describe_coche()

nuevo_coche.incrementarVelocidad(180)
