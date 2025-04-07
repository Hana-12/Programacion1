from abc import ABC, abstractmethod

# Definición de la interfaz
class Volador(ABC):

    @abstractmethod
    def volar(self):
        pass

# Implementación de la interfaz en las clases pajaro y avión
class Pajaro(Volador):

    def volar(self):
        return "El Pájaro mueve sus alas y vuela"

class Avion(Volador):

    def volar(self):
        return "El Avión enciende sus motores y despega"

#Uso en las distintas clases
pajaro = Pajaro()
print(pajaro.volar())

avion = Avion()
print(avion.volar())