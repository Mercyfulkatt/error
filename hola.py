contacto=["kat","pat"]
numero=[7351487465,7351235894]

accion = input('action borrar o  agregar usuario: ')
print(contacto)
if (accion=="agregar"):
    contact=input ("agregar un nuevo contacto")
    contacto.append(contact)
    num=input("agregar numero")
    numero.append(num)
    print(contacto)
elif(accion=="borrar"):
    contact=input("usuario borrar")
    contacto.remove(contact)
    print(numero)

    