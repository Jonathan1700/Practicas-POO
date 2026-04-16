from abc import ABC, abstractclassmethod

class vehiculo(ABC):
    @abstractclassmethod
    def ir (self):
        pass

    def detener(self):
        pass

class coche(vehiculo):
    def ir (self):
        print ("conduces el auto ")
    
    def detener(self):
        print ("el carro se esta deteniendo")

class motocicleta (vehiculo):
    def ir (self):
        print("andas en moto")
    def detener(self):
        print ("la moto se esta deteniendo")


coche = coche()
motocicleta = motocicleta ()



coche.detener()
motocicleta.detener()

# el metodo abstracto es para impedir que se creen objetos de una clase

