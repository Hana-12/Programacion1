class Vehiculo:

    def __init__(self,speed, color):
        self.setSpeed(speed) 
        self.setColor(color) 




    def getSpeed(self):
        return self.__speed
    
    def setSpeed(self,speed):
        if speed > 0 :
            self.__speed = speed
        else:
            raise ValueError ("No se puede velocidad menos de 0 ya que no tiene habilitada la reversa")

    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color
        


    # método que acelera progesivamente el vehículo a la velocidad ingresada
    def acelerar(self):
        print(f"El vehículo llegará a {self.getSpeed()}")
        for x in range(1,self.getSpeed() + 1):
            print(f"El vehículo anda acelerando a : {x} kM/H")

    # método que frena el vehículo
    def brake(self):
        print("Reduciendo la velocidad del vehículo, frenandooo!")

    # método que suena la bocina o similar
    def honk (self):
        print("Beep !!!BEEP!!!")

          
            
  