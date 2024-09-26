#Crea una clase llamada CuentaBancaria con atributos titular y saldo.
#Agrega métodos para depositar y retirar dinero de la cuenta. 



class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} unidades. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad} unidades. Nuevo saldo: {self.saldo}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")

cuenta = CuentaBancaria("Juan Pérez", 5000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(4000)