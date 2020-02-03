import math

valores = input("Ingresa tus valores: ")

val=list(valores)
acu=[]
iteracion=[]

def form(xa, xb):
    
    xr=(xa+xb)/2
    if(xr == 1.44):
        return "ES el ultimo"
    print("Xa: "+str(xa))
    print("Xb: "+str(xb))
    print("Xr: "+str(xr))
    
    result=xa * xb
    print("Multiplicacon: "+str(result))

    if(result<0):
        aux=xa
        print("Auxiliar: "+str(aux))
        print("Xa: "+str(xa))
        print("Xb: "+str(xb))
        return  form(xr, xb)
    elif(result>0):
        print("Xa: "+str(xa))
        print("Xb: "+str(xb))
        aux=xb
        return form(xa, xr)


    

def buscar(num):
    res=(math.pow(num,3 )-3)
    return res


for i in val:
    num=int(i)
    resultado=buscar(num)
    if(resultado < 0 ):
        acu.append(resultado)
        iteracion.append(i)
        
    elif(resultado < 6):
        acu.append(resultado)
        iteracion.append(i)

x1=int(iteracion[1])
x2=int(iteracion[2])


print(form(x1,x2))


