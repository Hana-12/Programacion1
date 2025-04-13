from .vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, speed, color, type_byke, talla_marco):
        super().__init__(speed,color)
        self.setType_byke(type_byke)
        self.setTalla_marco(talla_marco)
        self.llanta_suelta = False

    def setType_byke(self, type_byke):
        if type_byke :
            self.__type_byke = type_byke

        else:
            raise ValueError ("El tipo de bicicleta no puede estar vacio")
            
    def getType_byke(self):
        return self.__type_byke
    
    def setTalla_marco(self, talla_marco):
        if talla_marco:
            self.__talla_marco = talla_marco

        else:
            raise ValueError ("La talla del marco no puede estar vacío")
            
    def getTalla_marco(self):
        return self.__talla_marco
    
    

     
    # metodo que acelera lentamente el vehiculo a la velocidad ingresada
    def acelerar(self):
        for x in range(1,self.getSpeed() + 1):
            print(f"Bicicleta acelerando lentamente pedaleando a : {x} kM/H")
        print(f"Velocidad deseada alcanzada: {self.getSpeed()}")
 
    # metodo que pica la bicicleta en una rueda
    def wheelie(self):
        print("La bicicleta se ha parado en una llanta")

    

    # metodo que suena la bocina aplicada a una bici
    def honk(self):
        print("Ring !!!Ringgg!!!")

    def soltarLlanta(self):
        if not self.llanta_suelta:
            print("La bicicleta ahora tiene la llanta suelta")
            self.llanta_suelta = True
        else:
            print("La llanta no se puede soltar porque está suelta ya")

    def fijarLlanta(self):
        if self.llanta_suelta:
            print("La bicicleta ahora tiene la llanta fijada")
            self.llanta_suelta = False
        else:
            print("La llanta no se puede fijar porque está fija ya")



    
