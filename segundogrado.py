import math
a=int(input("agregar a"))
b=int(input("agregar b"))
c=int(input("agregar c"))

x1=((-b)+math.sqrt((b*b)-(4*a*c)))/(2*a)
x2=((-b)-math.sqrt((b*b)-(4*a*c)))/(2*a)

print("x1: " + str(x1))
print("x2: " + str(x2))