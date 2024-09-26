#Crea una clase llamada Coche con atributos marca y modelo.
#Crea un método que imprima la información del coche en un formato legible. 

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprimir_info(self):
        print(f"Coche - Marca: {self.marca}, Modelo: {self.modelo}")

coche = Coche("BMW", "M3 Competition")
coche.imprimir_info()