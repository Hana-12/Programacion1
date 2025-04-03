#Este módulo define la clase Coche para representar vehículos. 
#Incluye funcionalidades para describir el coche y gestionar sus atributos.

class Coche:

    # Represnetar un coche con marca, modelo y año

    def __init__(self, marca, modelo, año): #atributos privados __
        self.__marca = marca   
        self.__modelo = modelo
        self.set_año(año)


    def description(self): #Metodo descripción 

        print(f"Marca: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__año}")

    #metodos getter

    def get_marca(self):  #Traigame la marca

        return self.__marca
    
    def get_modelo(self): # Traigame el modelo

        return self.__modelo
    
    def get_año(self): # traigame el año

        return self.__año
    
    #metodos setter

    def set_marca(self, nueva_marca): # modificar la marca

        self.__marca = nueva_marca

    def set_modelo(self, nuevo_modelo): #modificar el modelo

        self.__modelo = nuevo_modelo

    def set_año(self, nuevo_año): #modificar el año
        if isinstance(nuevo_año, int) and len(str(nuevo_año)) == 4:
            self.__año = nuevo_año
        else: 
            raise ValueError("Error: el año del coche debe ser un numero de 4 digitos mayor a cero.")
    
    

