import math

semilla=int(input("Ingresa la semilla: "))
iteraciones=int(input("Ingresa el numero de iteracones: "))
#ingresa el usuario sus datos
contador=1
#contador igualado a cero

while contador < iteraciones:
    #contador es menor que las iteraciones 
    semillaCuadrada=math.pow(semilla, 2)
    #elevamos la variable semilla al cuadrado 
    NsemillaCuadrada=str(semillaCuadrada)
    #lo convierte a string 
    numeros=NsemillaCuadrada[4:8]
    #extraemos los cuatro elementos
    semilla=int(numeros)
    #convertimos a un entero
    print("R"+str(contador)+": "+str(semilla))
    #imprime Ry el valor de las variables 
    resultado=semilla/10000
    #se divide entre 10000
    print(resultado)
    #imprime el resultado
    contador=contador+1
    #se incremenata el contador 
