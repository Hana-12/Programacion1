#Este módulo define la clase Coche para representar vehículos. 
#Incluye funcionalidades para describir el coche y gestionar sus atributos.
from model.motor import Motor
from .vehiculo import Vehiculo
from .excepciones_personalizadas import ExcesoVelocidadException

## Ej4 Acá se incorpora el concepto de heredar de la Clase padre Vehiculo

class Coche(Vehiculo):
    motor = Motor(2000,"De combustión","Mercedes Benz") ## Es el motor por defecto
    ## Eventualmente podrían solicitarse al usuario los detalles del motor
    ## pero es solo para ejemplificar el ejercicio 9
    # Ej1 marca modelo y año
    # Ej2 setters y getters de marca y modelo
    # Ej3 constructores para inicializarlos

    
    # Representar un coche con marca, modelo y año
    ## Se deja el motor como opcional para no interferir con los ejercicios anteriores
    def __init__(self, speed, color, type_car, marca, modelo, año, motor=Motor(2000,"De combustión","Mercedes Benz")): #atributos privados __
        super().__init__(speed, color)
        self.__marca = marca   
        self.__modelo = modelo
        self.__type_car = type_car
        self.setAño(año)
        self.motor = motor
        
    def describir(self): #Metodo describir

        print(f"El coche tiene las siguientes características:\nMarca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}")

    #metodos getter

    def getMarca(self):  #Traigame la marca

        return self.__marca
    
    def getModelo(self): # Traigame el modelo

        return self.__modelo
    
    def getAño(self): # traigame el año

        return self.__año
    
    def getType_car(self):
        return self.type_car #Traer el tipo de carro 
      
    #metodos setter

    def setMarca(self, nueva_marca): # modificar la marca

        self.__marca = nueva_marca

    def setModelo(self, nuevo_modelo): #modificar el modelo

        self.__modelo = nuevo_modelo

    def setAño(self, nuevo_año): #modificar el año
        if isinstance(nuevo_año, int) and len(str(nuevo_año)) == 4:
            self.__año = nuevo_año
        else: 
            raise ValueError("Error: el año del coche debe ser un numero de 4 digitos mayor a cero.")
    
    def setType_car(self, type_car): # Modificar el tipo de carro
        if type_car :
            self.__type_car = type_car

        else:
            raise ValueError ("El tipo de carro no puede estar vacio")
            
    # metodo que acelera directamente a la velocidad ingresada
    # Ej5 distintos métodos de acelerar para coche y bicicleta
    def acelerar(self):
        print(f"El carro anda acelerando casi instantáneamente a: {self.getSpeed()} kM/H")

    # metodo que frena el vehiculo
    def brake(self):
        print("Reduciendo la velocidad del carro")

    # metodo que suena la bocina
    def honk(self):
        print("Beep !!!BEEP!!!")

    ## Ejercicio 9
    def describe_coche_con_motor(self):
        print(f"El coche es de marca {self.__marca}")
        print(f"El coche es modelo {self.__modelo}")
        print(f"El coche es de tipo {self.__type_car}")
        print("El motor tiene los siguientes detalles:")
        print("Potencia:",self.motor.potencia)
        print("Tipo:",self.motor.tipo)
        print("Marca:",self.motor.marca)

    ### Ejercicio 10
    def incrementarVelocidad(self, velocidad: int):
        self.velocidad = velocidad
        if self.velocidad > 200:
            raise ExcesoVelocidadException(f"{self.velocidad}km/h está por fuera de los límites permitidos")
        else:
            print(f"La nueva velocidad es de {self.velocidad} km/h, disfrute")