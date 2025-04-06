from .Vehicle import Vehicle

class Bicycle (Vehicle):
    def __init__(self, speed, type_byke):
        super().__init__(speed)
        self.type_byke = type_byke

    def set_type_byke(self, type_byke):
        if type_byke :
            self.___type_byke = type_byke

        else:
            raise ValueError ("El tipo de bicicleta no puede estar vacio")
            
    def get_type_byke(self):
        return self.type_byke
    
    # metodo que acelera progesivamente el vehiculo a la velocidad ingresada
    def accelerate (self):
        for x in range(1,self.get_speed() + 1):
            print(f"Bicicleta pedaleando a : {x} kM/H")

    # metodo que frena el vehiculo
    def brake (self):
        print("Reduciendo la velocidad de la bicicleta")

    # metodo que suena la bocina
    def honk (self):
        print("Ring !!!Ringgg!!!")
    
