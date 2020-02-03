import numpy
import sys

matriz1=input("Ingresa tu primer matriz: ")
matriz2=input("Ingresa tu segunda matriz")

matriz1=list(matriz1)
matriz2=list(matriz2)
aux=[]
i=1
j=1

for i in range(len(matriz1)):
    a=float( matriz1[i] )
    b=float( matriz2[i] )
    res= a+b
    print(res)

for j in range(len(matriz1)):
    a=float( matriz1[j] )
    b=float( matriz2[j] )
    res= a - b
    print("Resta: " +str(res))

r1 = int(input("Numero de renglones de la matriz 1 "))
c1  = int(input("Numero de columnas  de la matriz 1  "))
r2 = int(input("Numero de renglones de la matriz 2 "))
c2 = int(input("Numero de columnas de la matriz 2 "))


if( c1 != r2 ):
        print("no se pude hacer la multiplicacion")
        sys.exit()
        #detiene el programa

matriz_1=numpy.zeros((r1, c1))
matriz_2=numpy.zeros((r2, c2))
matrizResul=numpy.zeros((r1,c2))

print("Introduce los elementos de la matriz 1 ")

for n in range(0,r1):
        for m in range(0,c1):
                matriz_1[n,m]=input("Elemento a ["+str(n+1)+str(m+1)+"]")

for n in range(0,r2):
        for m in range(0,c2):
                matriz_2[n,m]=input("Elemento a ["+str(n+1)+str(m+1)+"]")

#operaciones de multiplicacion con las matrices

for x in range(0, r1):
        for k in range(0, c2):
                for l in range(0, r2 ):
                        matrizResul[k,l]+=matriz_1[x,l]*matriz_2[l,k]

print(matrizResul)



