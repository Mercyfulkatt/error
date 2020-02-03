#Agenda
#Ivan Alejandro Hernandez Estrada

import modulo
modulo.menu()

opcion = input ("> ")

print("Has seleccionado la opcion: ",opcion)

if opcion == "1":
    modulo.agregar()
    modulo.menu()
elif opcion == "2":
    print("dime cuantos registros quieres")
    registros = input("> ")
    registrosnumero = int(registros)
    modulo.mostrar( (registrosnumero + 1))
    modulo.menu()
elif opcion == "x":
    print("Adios")
else:
    modulo.mierror()
    modulo.menu()

