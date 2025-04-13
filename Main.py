from model.coche import Coche
from model.vehiculo import Vehiculo
from model.bicicleta import Bicicleta
from model.animal import Perro, Gato
from model.volador import Avion, Pajaro
from model.excepciones_personalizadas import ExcesoVelocidadException
from model.motor import Motor


#### Prueba de los ejercicios de 1 a 3
## Se hace directamente con el constructor con distintos parámetros (Ej3)
## Se muestra la descripción con el método describir (Ej1) solo con los 3 atributos de ese momento

def main():
    print("Crear coches")
    lista_coches = [Coche(50,"Gris urbano","4x4","VW", "Gol", 2003),
                    Coche(60,"Rojo","Híbrido","Mazda", "3", 2019),
                    Coche(70,"Verde lima","Eléctrico","BYD", "Dolphin", 2024),
                    Coche(55,"Azul","Combustible","Chevrolet", "Corsa", 2001)]

    print("Describir coches")
    for car in lista_coches:
        car.describir()



    ### Creamos una bicicleta para probar el método acelerar (Ej5)
    b1 = Bicicleta(20,"verde","road", "M" )
    ### Usamos un coche para probar el método acelerar (Ej5)
    lista_coches[0].acelerar()
    b1.acelerar()

    ### Ej6 Creamos una lista con varios vehículos tanto Coche como Bicicleta
    ### para mostrar como se comportan de manera diferente al acelerar
    ### Aun cuando ambos son de tipo vehículo (clase padre de ambos).
    lista_vehiculos = [Coche(80,"Azul Cielo","Diésel","Toyota", "Prado", 2020),
                    Bicicleta(60,"Rojo","MTB","M"),
                    Bicicleta(70,"Verde lima","road","L"),
                    Coche(55,"Verde","Combustible","Nissan", "Action", 2002)]

    print("Describir Vehículos disitntos tipos")
    for veh in lista_vehiculos:
        veh.acelerar()


    ### Para crear un coche manualmente, descomentar el siguiente bloque de código

    # Coche_marca = input("Ingrese marca:")
    # Coche_modelo = input("Ingrese modelo:")
    # Coche_speed = int(input("Ingrese la velocidad:"))
    # Coche_typocarro = input("Ingrese tipo de carro:")
    # Coche_color = input("Ingrese color de carro:")

    # while True:
    #      try:
    #          Coche_año = input("Ingrese año en formato AAAA: ")
    #          if Coche_año.isdigit() and len(Coche_año) == 4 and int(Coche_año) > 1940:
    #              Coche_año  = int(Coche_año)
    #              break
    #          else:
    #              print("El año ingresado no es válido, puede que el carro sea muy viejo")
    #      except ValueError:
    #         print("Error: el tipo de dato de año no es valido, ingrese un entero de 4 cifras.")

    # nuevo_coche = Coche(Coche_speed, Coche_color, Coche_typocarro, Coche_marca, Coche_modelo, Coche_año)

    #  #información del resultado

    # nuevo_coche.describir()


    ######### Ejercicio 7 Clases abstractas

    #Lista animales
    animales = [Perro(), Gato(), Perro()]

    #Impresión en pantalla utilzando el método abstracto
    for animal in animales:
        print(animal.hacer_sonido())

    ########### Ejercicio 8 Interfaces

    #Uso en las distintas clases
    pajaro = Pajaro()
    print(pajaro.volar())

    avion = Avion()
    print(avion.volar())


    ### Ejercicio 9 
    ### Se inserta el motor personalizado para la prueba
    motor = Motor(4500,"De combustión","BMW") 

    ## Se crea un ejemplo de coche agregando el motor
    nuevo_coche = Coche(55,"Verde","Campero","Jeep", "Wrangler", 2025, motor=motor)

    ### Se prueba el método de descripción que tiene además características del motor
    nuevo_coche.describe_coche_con_motor()

    ### Ejercicio 10

    ### Se genera la excepción personalizada llamada ExcesoVelocidadException
    ### Se crea en su propio archivo de excepciones y se importa
    ### Se usa la misma instancia de nuevo_coche para probar el método
    ### Con dos ejemplos uno que dispara el error y el otro que no.

    try:
        nuevo_coche.incrementarVelocidad(205)
    except ExcesoVelocidadException as e:
        print("Revisa la velocidad: ",e)


    try:
        nuevo_coche.incrementarVelocidad(180)
    except ExcesoVelocidadException as e:
        print("Revisa la velocidad: ",e)




    ##### Para ver un ejemplo del funcionamiento de las clases construida manualmente 
    ##### Descomentar el siguiente bloque de código.

    #Vehiculo
    #Ingresar la velocidad del vehiculo
    # while True:
    #     try:
    #         Vehiculo_speed = int(input("Ingrese la velocidad a la cual acelerará el vehículo: "))
    #         Vehiculo_color = input("Ingrese el color del vehículo: ")
    #         new_Vehiculo = Vehiculo(Vehiculo_speed, Vehiculo_color)
    #         break
            

    #     except ValueError as e:
    #         print(f"Error, valor ingresado a velocidad no es válido: {e}")
    #         print("Intente nuevamente")


    # print(f"Velocidad: {new_Vehiculo.getSpeed()}")

    # # se invoca el metodo acelerar el cual llegara a la velocidad ingresada
    # new_Vehiculo.acelerar()

    # #Vehiculo con sus clases hijas
    # activo = True  #variable que controla si el loop acaba o no

    # while  activo :
    #     type_Vehiculo = input("Ingrese el tipo de vehiculo carro o bicicleta, pero si desea terminar el programa escribe salir: ")

    #     if type_Vehiculo == "salir":
    #         activo = False
    #         break

    #     try:
    #         Vehiculo_speed = int(input("Ingrese la velocidad a la cual acelerará el vehículo: "))

    #     except ValueError as e:
    #         print ("Ingrese una velocidad válida")

    #     if type_Vehiculo == "carro":
    #         type_car = input("Ingrese el tipo de carro:")
    #         Coche_marca = input("Ingrese marca:")
    #         Coche_modelo = input("Ingrese modelo:")
    #         Coche_speed = int(input("Ingrese la velocidad:"))
    #         Coche_typocarro = input("Ingrese tipo de carro:")
    #         Coche_color = input("Ingrese color de carro:")
    #         while True:
    #             try:
    #                 Coche_año = input("Ingrese año en formato AAAA: ")
    #                 if Coche_año.isdigit() and len(Coche_año) == 4 and int(Coche_año) > 1940:
    #                     Coche_año  = int(Coche_año)
    #                     break
    #                 else:
    #                     print("El año ingresado no es válido, puede que el carro sea muy viejo")
    #             except ValueError:
    #                 print("Error: el tipo de dato de año no es valido, ingrese un entero de 4 cifras.")
    #         new_car = Coche(Vehiculo_speed,type_car,Coche_marca,Coche_modelo,Coche_año)
    #         new_car.acelerar()

    #         if Vehiculo_speed > 70:     # si la velocidad es mayor a 70 el carro frena
    #             new_car.brake()
    #         else: 
    #             new_car.honk()          # si no toca la bocina

    #     elif type_Vehiculo == "bicicleta":
    #         type_byke = input("Ingrese el tipo de bicicleta:")
    #         byke_color = input("Ingrese el color de bicicleta:")
    #         byke_talla_marco = input("Ingrese la talla del marco de la bicicleta:")
    #         new_byke = Bicicleta(Vehiculo_speed,byke_color,type_byke,byke_talla_marco)
    #         new_byke.acelerar()

    #         if Vehiculo_speed > 40:     # si la velocidad es mayor a 40 la bicicleta frena
    #             new_byke.brake()
    #         else: 
    #             new_byke.honk()         # si no toca la bocina
            
    #     else:   
    #         print("Tipo de vehiculo no reconocido.")
    #         continue
        
        

if __name__ == "__main__":
    main()