#Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico. 
#Luego, crea clases derivadas como Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban 
#el método tocar para imprimir mensajes diferentes.

class InstrumentoMusical:
    def tocar(self):
        print("Este instrumento está sonando.")

class Piano(InstrumentoMusical):
    def tocar(self):
        print("El piano está tocando una hermosa melodía.")

class Guitarra(InstrumentoMusical):
    def tocar(self):
        print("La guitarra está tocando acordes vibrantes.")

if __name__ == "__main__":
    instrumento1 = Piano()
    instrumento1.tocar()  

    instrumento2 = Guitarra()
    instrumento2.tocar()  