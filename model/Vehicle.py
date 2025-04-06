class Vehicle:

    def __init__(self,speed):
        self.set_speed(speed) 

    def get_speed(self):
        return self.__speed
    
    def set_speed(self,speed):
        if speed > 0 :
            self.__speed = speed
        else:
            raise ValueError ("No se puede velocidad menos de 0 ya que retrocederia")
    
    # metodo que acelera progesivamente el vehiculo a la velocidad ingresada
    def accelerate (self):
        for x in range(1,self.__speed + 1):
            print(f"El vehiculo anda acelerando a : {x} kM/H")

    # metodo que frena el vehiculo
    def brake ():
        print("Reduciendo la velocidad del vehiculo")

    # metodo que suena la bocina
    def honk ():
        print("Beep !!!BEEP!!!")

          
            
  