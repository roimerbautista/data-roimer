print ("Estructuras Repititivas")

#For 
for i in range(1, 11):
    print(f"Numero: {i}")


"---------------------------------------------"
for letra in "Python":
    print(f"Letra: {letra}")


#######################################################
#While

contador = 1
while contador <= 3:
    print(f"intento: {contador}")
    contador += 1


#Do While

while True:
    numero = int(input("Ingrese un numero > 0 : "))
    if numero > 0:
        print(f"El numero ingresado es: {numero}")
        break
    else:
        print("El numero ingresado no es mayor a 0, intente nuevamente")