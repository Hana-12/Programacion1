#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def hacer_sonido(self):
        pass

class Gato(Animal):

    def hacer_sonido(self):
        return 'Miau Miau'

class Perro(Animal):

    def hacer_sonido(self):
        return 'Guau Guau'

#Lista animales
animales = [Perro(), Gato(), Perro()]

#Impresión en pantalla utilzando el método abstracto
for animal in animales:
    print(animal.hacer_sonido())