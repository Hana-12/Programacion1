from .Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, speed, type_car):
        super().__init__(speed)
        self.type_car = type_car

    def set_type_byke(self, type_car):
        if type_car :
            self.___type_car = type_car

        else:
            raise ValueError ("El tipo de bicicleta no puede estar vacio")
            
    def get_type_car(self):
        return self.type_car
    
    # metodo que acelera progesivamente el vehiculo a la velocidad ingresada
    def accelerate (self):
        for x in range(1,self.get_speed() + 1):
            print(f"El carro anda acelerando a : {x} kM/H")

    # metodo que frena el vehiculo
    def brake (self):
        print("Reduciendo la velocidad del carro")

    # metodo que suena la bocina
    def honk (self):
        print("Beep !!!BEEP!!!")