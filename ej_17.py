#Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, y un método area que calcule el área
#de la figura. Luego, crea clases derivadas como Rectangulo y Triangulo que hereden de FiguraGeometrica y 
#sobrescriban el método area para calcular el área específica de cada figura.

class FiguraGeometrica:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def area(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases derivadas")

class Rectangulo(FiguraGeometrica):
    def area(self):
        return self.ancho * self.altura

class Triangulo(FiguraGeometrica):
    def area(self):
        return (self.ancho * self.altura) / 2

rectangulo = Rectangulo(5, 10)
print(f"Área del rectángulo: {rectangulo.area()}")

triangulo = Triangulo(5, 10)
print(f"Área del triángulo: {triangulo.area()}")