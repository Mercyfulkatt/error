a=5
c=7
m=8
xn=4
cont=0

#Decalracion de las constantes


def congruencial(xn, cont):
#creamos la función   
    xn=float(xn)
    #convierte a float
    if(cont == 10):
        #evalua el contador 
        return "Es todo"


    resultado=((5*xn) + 7)
#hace la operacion
    result=float(resultado)
    result = result%8
#saca el modulo 
    x1=result/8
    x1=float(x1)
    print("+-------------------------------------------------+")
    print( "|" +"Xn :"+ str(xn) +" | " +" " + "Xn+1  " +str(result) + " | "  +" "  +"Números aleatorios: "+ str(x1 )+ " |")
    cont=cont+1
    congruencial(result, cont)
    #se usa la recursividad
    #se vuelve a llamar la misma función

print(  congruencial(4,cont))
