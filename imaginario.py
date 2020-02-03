base = complex(input("Ingresa tu numero imaginario"))
potencia= int(input("Ingresa la potencia"))

lista1=[1,5,9,13,17,21,25,29,33]
lista2=[2,6,10,14,18,22,26,30,34]
lista3=[3,7,11,15,19,23,27,31,35]
lista4=[0,4,8,12,16,20,24,28,32,36,-4,-8,-12,-16,-20,-24,-28,-32,-36,-40]
lista6=[-1,-4,-8,-12,-16,-20,-24,-28,-32,-36]
lista7=[-2,-6,-10,-14,-18,-22,-26,-30,-34,-38]
lista8=[-3,-7,-11,-15,-19,-23,-27,-31,-35,-39]

#declaramos unas listas en las que se declaran los valores

if(potencia in lista1):
    print("Resultado es: j")
elif(potencia in lista2 ):
    print("Resultado es: -1")
elif(potencia in lista3):
    print("Resultado es: -j")
elif(potencia in lista4):
    print("Resultado es: 1")
elif(potencia in lista6):
    print("Resultado es: -i")
elif(potencia in lista7):
    print("Resultado es: -1")
elif(potencia in lista8):
    print("Resultado es: i")
elif(potencia in lista4):
    print("Resultado es: 1")
#comparamos que los valores coincidan y en base a eso imprimimos el resultado