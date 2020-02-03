def bienvenidos():
    print("Bienvenidos a Agenda Telefónica")
    print("Seleccione una opcion: ")
    print("1 - Añadir un registro a la agenda")
    print("2 - Listar el contenido de la agenda")
    print("3 - Salir")
    
def escribir():
    print("Has elegido añadir un registro a la agenda ")
    agenda = open("agendatelefonica.csv",'a')
    nombre = input("Introduce el nombre de contacto: ")
    telefono = input("Introduce su telefono ")
    posicion = input("Introduce la posicion en la lista")
    print("Se ha guardado en la agenda el contacto: ", nombre,"con el numero")
    agenda.write(posicion)
    agenda.write(",")
    agenda.write(nombre)
    agenda.write(",")
    agenda.write(telefono)
    agenda.write(",")
    agenda.write("\n")
    agenda.close()
    
def listar(fin):
    print("Has elegido listar el contenido de la agenda")
    agenda = open("agendatelefonica.csv")
    numero = 0
    for i in range(1,fin):
        lectura = agenda.readline()
        print(lectura.replace(",","\t\t"))
        numero = numero + 1
    print("Ya he terminado de leer el archivo")
    agenda.close()
    
def mierror():
    print("La opcion que has seleccionado no es valida")
    
def buscador(nombrebuscado):
    print("Aqui buscare las coincidencias")
    agenda = open("agendatelefonica.csv")
    for i in range(1,30):
        lectura = agenda.readline()
        partido = lectura.split(',')
        if nombrebuscado == partido[1]:
           print(partido[2])
    agenda.close()
        
