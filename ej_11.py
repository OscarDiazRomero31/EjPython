#Crea una clase llamada Persona con atributos nombre y edad. 
#Luego, crea un objeto de tipo Persona e imprime sus atributos.

class Persona:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre  
        self.edad = edad 
        self.correo = correo     

persona1 = Persona("Oscar", 21, "oscar@gmail.com")

print("Nombre:", persona1.nombre)
print("Edad:", persona1.edad)
print("Coreo:", persona1.correo)