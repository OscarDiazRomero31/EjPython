#Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico.
#Luego, crea dos clases derivadas, Perro y Gato, que hereden de Animal y sobrescriban
#el método hablar para imprimir mensajes diferentes. 

class Animal:
    def sonido(self):
        print("Este animal hace un sonido.")

class Perro(Animal):
    def sonido(self):
        print("¡Guau! ¡Guau!")

class Gato(Animal):
    def sonido(self):
        print("¡Miau! ¡Miau!")

if __name__ == "__main__":
    mi_perro = Perro()
    mi_gato = Gato()

    mi_perro.sonido()  
    mi_gato.sonido()   