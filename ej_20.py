#Crea una clase base llamada Empleado con atributos nombre y salario, y un método calcular_salario_anual 
#que calcule el salario anual del empleado. Luego, crea clases derivadas como Gerente y Programador que 
#hereden de Empleado y añadan atributos y métodos específicos de cada tipo de empleado.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario_anual(self):
        return self.salario * 12

class Gerente(Empleado):
    def __init__(self, nombre, salario, bonificacion):
        super().__init__(nombre, salario)
        self.bonificacion = bonificacion

    def calcular_salario_anual(self):
        return (self.salario + self.bonificacion) * 12

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguajes):
        super().__init__(nombre, salario)
        self.lenguajes = lenguajes  # Lista de lenguajes de programación que conoce

    def mostrar_lenguajes(self):
        return f"{self.nombre} conoce los siguientes lenguajes: {', '.join(self.lenguajes)}"

empleado1 = Empleado("Juan", 3000)
gerente1 = Gerente("Ana", 5000, 1000)
programador1 = Programador("Luis", 4000, ["Python", "Java", "C++"])

print(f"Salario anual de {empleado1.nombre}: {empleado1.calcular_salario_anual()}")
print(f"Salario anual de {gerente1.nombre}: {gerente1.calcular_salario_anual()}")
print(f"Salario anual de {programador1.nombre}: {programador1.calcular_salario_anual()}")
print(programador1.mostrar_lenguajes())
