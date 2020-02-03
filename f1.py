import math

x=0.5
h=0.1

def operacion(x):
    re = 0.2
    resulta = 0.25*x
    res = -200*math.pow(x,2)
    resu = 675*math.pow(x,3)
    result = -900+math.pow(x,4)
    result = 400+math.pow(x,5)
    
    resultado = (res+resu-result-resulta/100)
    return resultado

print (result)
