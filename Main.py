from model.Coche import Coche


print("Crear coche")
Coche_marca = input("Ingrese marca:")
Coche_modelo = input("Ingrese modelo:")

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

nuevo_coche = Coche(Coche_marca, Coche_modelo, Coche_año)

#información del resultado

print(f"Marca: {nuevo_coche.get_marca()} - Modelo: {nuevo_coche.get_modelo()} - Año: {nuevo_coche.get_año()}")

