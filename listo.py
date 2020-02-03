
iteraciones=int(input("Número de iteraciones: "))
x=0
y=0

for i in range(0, iteraciones):
    x = ((y**2) -8 -x**2 )/(-10)
    y = ((y**2) -8 -x**2 )/(-10)
    print("X: "+str(x))
    print("Y: "+str(y))