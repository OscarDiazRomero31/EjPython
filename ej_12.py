#Crea una clase llamada Rectangulo con atributos ancho y altura.
#Agrega un método para calcular el área del rectángulo y otro para calcular su perímetro.

class TrianguloRectangulo():
    def __init__(self, base, altura ):
        self.base=base
        self.altura=altura
    
    def area (self):
        return self.base * self.altura
    
    def perimetro (self):
        return 2 * (self.base + self.altura)

rectangulo = TrianguloRectangulo(5,3)

print("Área del rectángulo:", rectangulo.area())
print("Perímetro del rectángulo:", rectangulo.perimetro())