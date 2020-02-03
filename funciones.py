import math

x=5
h=0.1
f=0
fcentros=0

def delantera(x,h):
    f=math.log(x+h)
    fp=math.log(x)
    res=(f-fp)/h
    print(res)

def centros(x,h):
    fcentros=math.log(x+h)
    fcen=math.log(x-h)
    resultado=(fcentros-fcen)/(h*2)
    print(resultado)

def atras(x,h):
    resul=math.log(x)
    f1=math.log(x-h)
    resulta=(resul-f1)/h
    print(resulta)

delantera(x,h)
centros(x,h)
atras(x,h)