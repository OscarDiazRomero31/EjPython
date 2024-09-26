#Crea una clase llamada Estudiante con atributos nombre, edad y curso.
# Crea varios objetos de tipo Estudiante y almacénalos en una lista.
# Luego, itera sobre la lista e imprime la información de cada estudiante.

class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

estudiante1 = Estudiante("Ana", 20, "2ºDAW")
estudiante2 = Estudiante("Luis", 22, "1ºASIR")
estudiante3 = Estudiante("María", 21, "2ºDAW")

lista_estudiantes = [estudiante1, estudiante2, estudiante3]

for estudiante in lista_estudiantes:
    print(f"Nombre: {estudiante.nombre}, Edad: {estudiante.edad}, Curso: {estudiante.curso}")