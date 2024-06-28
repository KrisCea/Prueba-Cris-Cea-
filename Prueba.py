#recuerda hacer contador

#Uso de colecciones
# Uso de archivos de texto
# Uso de librerías estándar de Python

"""nombre, 
dirección y 
número de teléfono,
detalles de su pedido, incluyendo el 
tipo y la 
cantidad de plantas o flores solicitadas"""

""" El sistema deberá mostrar una lista de todos los pedidos realizados, incluyendo los detalles del cliente y los productos
solicitados"""

import csv

agregar_cliente=True
agregar_producto=True
precio_final=0
precio=0
datos_boleta=[]
pedido=[]
data=[]

def mensaje_error():
    print("ERROR\nintente nuevamente\n")

def menu_productos():
    print(
"""
    Productos:

n°  Producto:       Valor unitario:
1.  Abono.          $24
2.  Tierra.         $28.6 
3.  Lirio.          $27.5 
4.  Rosas rojas.    $39.5 
5.  Margaritas.     $110

0.  Salir

""")

print(
"""   Vivero GreenGarden
       plantas y flores

""")
while agregar_cliente:
    datos_boleta.clear()
    pedido.clear()
    agregar_producto=True

    print("Ingrese datos del cliente.")

    nombre=input("Nombre: ")
    while not nombre.isalpha():
        mensaje_error()
        nombre=input("Nombre: ")
    
    direccion=input("Direccion: ")

    telefono=input("Telefono: ")
    while not telefono.isdigit() or len(telefono)!=9:
        if len(telefono)!=9:
            print("DEBE TENER 9 DIGITOS\n")
        else:
            mensaje_error()
        telefono=input("Telefono: ")
    
#PEDIDO
    while agregar_producto:
        precio_final=0
        menu_productos()

        opcion=input("Ingrese numero de opcion: ")
        while not opcion.isdigit() or int(opcion)<0 or int(opcion)>5:
            mensaje_error()
            opcion=input("Ingrese numero de opcion: ")
        

        if int(opcion)==1:
            producto="Abono"
            precio= 24
        elif int(opcion)==2:
            producto="Tierra"
            precio= 28.6
        elif int(opcion)==3:
            producto="Lirio"
            precio= 27.5
        elif int(opcion)==4:
            producto="Rosas rojas"
            precio= 39.5 
        elif int(opcion)==5:
            producto="Margarita"
            precio= 110
        elif int(opcion)==0:
            break

        cantidad=input("Cantidad: ")
        while not cantidad.isdigit() or float(cantidad)<0:
            mensaje_error()
            cantidad=input("Cantidad: ")

        
        
        

        valor_compra=float(precio)*float(cantidad)
        precio_final+=float(valor_compra)

        pedido.append([f"Producto: {producto}",f"Cantidad: {cantidad}",f"Precio: ${valor_compra}"])

        agrega=input("1 para agregar producto: ")
        if agrega!="1":
            agregar_producto=False

    if int(opcion)==0:
            break
    
    print(f"****Boleta****")
    for i in pedido:
        for j in i:
            print(j, end=", ")

        print("")
    print(f"Precio final:",precio_final)
        
    agrega=input("1 para agregar cliente: ")
    if agrega!="1":
        agregar_cliente=False

        datos_boleta=[nombre,direccion,telefono,pedido]
        data.append(datos_boleta)

print("Saliendo...")

with open("Reporte_GreenGarden.csv","w") as archivoCSV:
    editarCSV=csv.writer(archivoCSV)

    editarCSV.writerow(["Nombre","Direccion","Telefono","Pedido"])
    editarCSV.writerows(data)
