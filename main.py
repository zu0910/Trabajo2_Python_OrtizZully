import json 
from os import system

with open("./compras.json", encoding="utf-8") as file:
    compras=json.load(file)

with open("./empleados.json", encoding="utf-8") as files:
    empleados=json.load(files)

with open("./medicamentos.json", encoding="utf-8") as files:
    medicamentos=json.load(files)

with open("./pacientes.json", encoding="utf-8") as file:
    pacientes=json.load(file)

with open("./proveedores.json", encoding="utf-8") as files:
    proveedores=json.load(files)

with open("./ventas.json", encoding="utf-8") as files:
    ventas=json.load(files)

booleano=True
while booleano == True:

    print("""
//////////////////////////////////////////////////////////
------------------ WELCOME TO FARMACIA -------------------
          
          1. Ventas.
          2. Compras.
          0. Finalizar

----------------------------------------------------------
""")
    opc= int(input("Por favor ingresa unas de las opciones anteriores: \n"))
    system("clear")
    if opc==1:
        print("---------------- VENTAS -------------------")
        print("-------   Información del paciente   --------")
        NomPaci=input(" Ingrese el nombre del paciente: \n")
        DirePaci=input(" Ingrese la dirección del paciente: \n")

        print("-------------- Información del empleado ---------------")

        for i in empleados:
            print("Nombre: ",i["nombre"], "   Cargo: ",i["cargo"])

        print("-------------------------------------------------------")

        NomEmple=str(input("Escribe el nombre del empleado: \n"))
        CargoEmple=str(input("Escribe el cargo que tiene el empleado: \n"))

        print ("-----------------   Medicamentos     --------------------")

        for i in medicamentos:
            print("_________________________________________________________________________")
            print(" Nombre: ", i["nombre"]," Cantidad: ", i["stock"]," Precio: ", i["precio"])
            print("_________________________________________________________________________")

        print("------------------------------------------------------------------------------")

        NomMedi=str(input("Ingrese el nombre del medicamento: \n"))
        CantMedi=int(input("Ingrese la cantidad de medicamentos que desee llevar: \n"))

        if i["stock"]>=CantMedi:
            i["stock"]=i["stock"]-CantMedi
            Precio=i["precio"]

        ventas.append({"nombre": NomPaci, "direccion": DirePaci})
        empleados.append({"nombre": NomEmple, "cargo": CargoEmple})
        medicamentos.append({"nombre": NomMedi, "stock": CantMedi, "precio": Precio})

        print("Los datos fueron registrados con exito")

    elif opc==2:
        print("------------------  COMPRAS  ----------------------")
        print("-------   Información del proveedor   --------")
        NomPro=input(" Ingrese el nombre del proveedor: \n")
        ConPro=input(" Ingrese el numero de contacto del proveedor: \n")
        DirePro=input("Ingrese la dirección del proveedor: \n")

        print(" --------------------- Medicamentos Comprados -------------------")

        for i in compras:
           print("Nombre del medicamento: ", i["nombreMedicamento"], "\nCantidad comprada: ", i["cantidadComprada"], "\nPrecio de compra: ", i["precioCompra"])
        print("-----------------------------------------------------------------------------------------------------------------------------")
        
        proveedores.append({"nombre":NomPro,"contacto":ConPro,"direccion":DirePro})

    elif opc==0:
        print("Hasta luego XD")
        booleano=False


Compra=json.dumps(compras)
with open("./compras.json","w") as files:
    files.write(Compra)

Empleado=json.dumps(empleados)
with open("./empleados.json","w") as files:
    files.write(Empleado)

Medicamento=json.dumps(medicamentos)
with open("./medicamentos.json","w") as files:
    files.write(Medicamento)

Paciente=json.dumps(pacientes)
with open("./pacientes.json","w") as files:
    files.write(Paciente)

Proveedor=json.dumps(proveedores)
with open("./proveedores.json","w") as files:
    files.write(Proveedor)

Venta=json.dumps(ventas)
with open("./ventas.json","w") as files:
    files.write(Venta)