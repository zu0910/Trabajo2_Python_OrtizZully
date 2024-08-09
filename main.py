import json 
from os import system # Limpiar pantalla

with open("./compras.json", encoding="utf-8") as file:
    compras=json.load(file)# Abrir el json de compras

with open("./empleados.json", encoding="utf-8") as files:
    empleados=json.load(files)# Abrir el json de empleados

with open("./medicamentos.json", encoding="utf-8") as files:
    medicamentos=json.load(files)# Abrir el json de medicamentos

with open("./pacientes.json", encoding="utf-8") as file:
    pacientes=json.load(file)# Abrir el json de pacientes

with open("./proveedores.json", encoding="utf-8") as files:
    proveedores=json.load(files)# Abrir el json de proveedores

with open("./ventas.json", encoding="utf-8") as files:
    Ventas=json.load(files)# Abrir el json de ventas

#boleano es verdadero
booleano=True
while booleano == True:#Mientras el boleano sea verdadero se hara
# Mostrara el menu principal
    print("""
//////////////////////////////////////////////////////////
------------------ WELCOME TO FARMACIA -------------------
          
          1. Ventas.
          2. Compras.
          0. Finalizar

----------------------------------------------------------
""")
    #el usuario tendra que digitar unas de las opciones que aparecen en el menu
    opc= int(input("Por favor ingresa unas de las opciones anteriores: \n"))
    system("clear")
    #Si la opcion elegida es uno se hara
    if opc==1:
        print("---------------- VENTAS -------------------")
        print("-------   Información del paciente   --------")
        #En la variable creada se guardara la informacion que digite el usuario
        NomPaci=input(" Ingrese el nombre del paciente: \n")
        DirePaci=input("Ingrese la direccion del paciente: \n")
        TelePaci=input(" Ingrese el telefono del paciente: \n")
        #Se mostrara la informacion del empleado 
        print("-------------- Información del empleado ---------------")
        #se crea un for para que entre al json empleados e imprima el nombre, y cago, i es el bucle que cuenta todos los nombres y cargos que se encuentra en el json
        for i in empleados:
            print("Nombre: ",i["nombre"], "   Cargo: ",i["cargo"])

        print("-------------------------------------------------------")
        #Apartir de la informacion mostrada tendra que copiar exactamente igual el nombre y cargo del empleado
        NomEmple=str(input("Escribe el nombre del empleado: \n"))
        CargoEmple=str(input("Escribe el cargo que tiene el empleado: \n"))
        system("clear")

        print ("-----------------   Medicamentos     --------------------")
        #igual que el procedimiento del anterior se le mostrara la informacion guardada del json medicamento
        for i in medicamentos:
            print("_________________________________________________________________________")
            print(" Nombre: ", i["nombre"]," Cantidad: ", i["stock"]," Precio: ", i["precio"])
            print("_________________________________________________________________________")

        print("------------------------------------------------------------------------------")
        # El usuario tendra que digitar el nombre del medicamento y la cantidad que desee llevar
        NomMedi=str(input("Ingrese el nombre del medicamento: \n"))
        CantMedi=int(input("Ingrese la cantidad de medicamentos que desee llevar: \n"))
        system("clear")#Se limpiara la pantalla de la consola 
        #crea un bucle para el json de medicamento
        for i in medicamentos:
            #si la cantidad de medicamentos es mayor o igual a la cantidad que ingreso el usuario y lo que hara es restar 
            if i["stock"]>=CantMedi:
                i["stock"]=i["stock"]-CantMedi
                Precio=i["precio"]
        #se guardara los siguientes casos en el json ventas y pecientes
        Ventas.append({"nombre": NomPaci, "direccion": DirePaci})
        pacientes.append({"nombre": NomPaci, "direccion": DirePaci, "telefono": TelePaci})
        
        print("Los datos fueron registrados con exito")
        system("clear")
        #Si la opcion elegida es dos se hara 
    elif opc==2:
        print("------------------  COMPRAS  ----------------------")
        print("-------   Información del proveedor   --------")
        #se cra una variable donde guarde la informacion que el usuario digite 
        NomPro=input(" Ingrese el nombre del proveedor: \n")
        ConPro=input(" Ingrese el  contacto del proveedor: \n")
        DirePro=input("Ingrese la dirección del proveedor: \n")

        for i in medicamentos:
            print("_________________________________________________________________________")
            print(" Nombre: ", i["nombre"]," Cantidad: ", i["stock"]," Precio: ", i["precio"])
            print("_________________________________________________________________________")

        print("------------------------------------------------------------------------------")
        
        print("--------- Compra del medicamento -------------------------")
        NomMedicamento=input("Ingrese el nombre de medicamento: \n")
        CantCompra=int(input("Ingrese la cantidad que desees comprar: \n"))
        PreCom=int(input("Ingrese el precio del medicamento: \n"))
        #un bucle para que la cantidad de medicamento sube lo cantidad que el usuario desea comprar
        for i in medicamentos:
            if NomMedicamento== i["nombre"]:
                i["stock"]+=CantCompra
        #esta informacion se guardara a los json proveedores y compras
        proveedores.append({"nombre":NomPro,"contacto":ConPro,"direccion":DirePro})
        compras.append({"proveedor": {"nombre":NomPro, "contacto":ConPro}, "medicamentosComprados":{"nombreMedicamento":NomMedicamento, "cantidadComprada":CantCompra, "precioCompra":PreCom}})
    #si la opcion elegida es 0 se finalizara el programa 
    elif opc==0:
        print("Hasta luego XD")
        booleano=False

#Guardar informacion al json de compra
Compra=json.dumps(compras)
with open("./compras.json","w") as files:
    files.write(Compra)
#Guardar informacion al json de empleado
Empleado=json.dumps(empleados)
with open("./empleados.json","w") as files:
    files.write(Empleado)
#Guardar informacion al json de medicamento
Medicamento=json.dumps(medicamentos)
with open("./medicamentos.json","w") as files:
    files.write(Medicamento)
#Guardar informacion al json de paciente
Paciente=json.dumps(pacientes)
with open("./pacientes.json","w") as files:
    files.write(Paciente)
#Guardar informacion al json de proveedor
Proveedor=json.dumps(proveedores)
with open("./proveedores.json","w") as files:
    files.write(Proveedor)
#Guardar informacion al json de venta
Venta=json.dumps(Ventas)
with open("./ventas.json","w") as files:
    files.write(Venta)

#Desarrollado por Zully Fernanda Ortiz Avendaño