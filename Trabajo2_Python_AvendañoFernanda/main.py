import json 

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

    if opc==1:
        print("-----------VENTAS-------------------")