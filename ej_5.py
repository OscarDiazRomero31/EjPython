#Calcula el factorial de un número.

print ("Programa que calcula el factorial")
numero = int(input("Introduzca el número: "))
factorial = 1
i = 1 #Valor inicial.
while (i <= numero): #Bucle While en el que empieza en i y sale de el en el numero que hemos introducido.
    factorial = factorial * i 
    i = i + 1
print ("El factorial de " +str(numero) + " es " +str(factorial))