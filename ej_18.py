#Crea una clase base llamada Vehiculo con atributos marca y modelo, y un método informacion que imprima la 
#información del vehículo. Luego, crea clases derivadas como Coche y Bicicleta que hereden de Vehiculo y 
#añadan atributos y métodos específicos de cada tipo de vehículo.

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def informacion(self):
        super().informacion()
        print(f"Número de puertas: {self.puertas}")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def informacion(self):
        super().informacion()
        print(f"Tipo de bicicleta: {self.tipo}")

coche = Coche("Toyota", "Corolla", 4)
coche.informacion()

bicicleta = Bicicleta("Giant", "Escape 3", "Urbana")
bicicleta.informacion()
