from model.Coche import Coche
from model.Vehicle import Vehicle
from model.Bicycle import Bicycle


print("Crear coche")
Coche_marca = input("Ingrese marca:")
Coche_modelo = input("Ingrese modelo:")
Coche_speed = int(input("Ingrese la velocidad:"))
Coche_typocarro = input("Ingrese tipo de carro:")

while True:
     try:
         Coche_año = input("Ingrese año:")
         if Coche_año.isdigit() and len(Coche_año) == 4:
             Coche_año  = int(Coche_año)
             break
         else:
             print("El año ingresado no es valido")
     except ValueError:
         print("Error: el tipo de dato de año no es valido.")

nuevo_coche = Coche(Coche_speed,Coche_typocarro,Coche_marca, Coche_modelo, Coche_año)

 #información del resultado

print(f"Marca: {nuevo_coche.get_marca()} - Modelo: {nuevo_coche.get_modelo()} - Año: {nuevo_coche.get_año()}")


 #Vehiculo
 #Ingresar la velocidad del vehiculo
try:
    Vehicle_speed = int(input("Ingrese la velocidad a la cual acelerará el vehículo: "))
    new_vehicle = Vehicle(Vehicle_speed)
    print(f"Speed: {new_vehicle.get_speed()}")

# se invoca el metodo accelerate el cual llegara a la velocidad ingresada
    new_vehicle.accelerate()

except ValueError as e:
    print(f"Error: {e}")

#Vehiculo con sus clases hijas
activo = True  #variable que controla si el loop acaba o no

while  activo :
    type_vehicle = input("Ingrese el tipo de vehiculo carro o bicicleta, pero si desea terminar el programa escribe salir: ")

    if type_vehicle == "salir":
        activo = False
        break

    try:
        Vehicle_speed = int(input("Ingrese la velocidad a la cual acelerará el vehículo: "))

    except ValueError as e:
        print ("Ingrese una velocidad valida")

    if type_vehicle == "carro":
        type_car = input("Ingrese el tipo de carro:")
        new_car = Coche (Vehicle_speed,type_car,Coche_marca,Coche_modelo,Coche_año)
        new_car.accelerate()

        if Vehicle_speed > 70:     # si la velocidad es mayor a 70 el carro frena
            new_car.brake()
        else: 
            new_car.honk()          # si no toca la bocina

    elif type_vehicle == "bicicleta":
        type_byke = input("Ingrese el tipo de bicicleta:")
        new_byke = Bicycle (Vehicle_speed,type_byke)
        new_byke.accelerate()

        if Vehicle_speed > 40:     # si la velocidad es mayor a 40 la bicicleta
            new_byke.brake()
        else: 
            new_byke.honk()         # si no toca la bocina
        
    else:   
        print("Tipo de vehiculo no recnocido.")
        continue
    
        

