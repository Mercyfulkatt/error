contacto=["kat","pat","isis"]
numero=[7351487465,7351235894,735418798]

accion = input('action borrar o  agregar usuario: ')
print(contacto)
if (accion=="agregar"):
    contact=input ("agregar un nuevo contacto: ")
    contacto.append(contact)
    num=input("agregar numero: ")
    numero.append(num)
    print(contacto)
    print(numero)
elif(accion=="borrar"):
    contact=input("usuario borrar: ")
    contacto.remove(contact)
    nume=input("telefono a borrar: ")
    print(nume)
    numero.remove(nume)
    print(contacto)
    print(numero)
