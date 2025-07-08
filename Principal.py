from DAO import DAO
from os import system
import os

#--------------------------------------------------------------------------------------------------

d = DAO()

#--------------------------------------------------------------------------------------------------

def menu():
    system("cls")
    print("--------------------------------")
    print("--- (Gestión De Bibliotecas) ---")
    print("--------------------------------")
    print("      * 1.Registrar")
    print("      * 2.Listar")
    print("      * 3.Buscar")
    print("      * 4.Modificar")
    print("      * 5.Eliminar")
    print("      * 6.Salir")
    op = int(input("      * Digite Una Opcion:"))
    if op==1:
        digitar_datos()
    elif op == 2:
        listar_bibliotecas()
    elif op == 3:
        buscar_bibliotecas()
    elif op == 4:
        actualizar_datos()
    elif op == 5:
        eliminar_bibliotecas()
    else:
        salir()

#--------------------------------------------------------------------------------------------------

def digitar_datos():
    system("cls")
    print("--- (Registrar) ---")
    id = int(input("Digite el _id de la biblioteca: "))
    
    r = d.comprobar_id(id)
    if r == 1:
        system("cls")
        print(f"\n --- El id {id} ya existe ---\n")
        system("pause")
        menu()
    
    system("cls")
    print("--- (Registrar) ---")
    nom = input("Digite el nombre de la biblioteca: ")
    system("cls")
    print("--- (Registrar) ---")
    ciu = input("Digite la ciudad de la biblioteca: ")
    system("cls")
    print("--- (Registrar) ---")
    pai = input("Digite el país de la biblioteca: ")
    system("cls")
    print("--- (Registrar) ---")
    sal = input("¿Dispone de salas de lectura? 1.Sí 2.No: ")
    system("cls")
    print("--- (Registrar) ---")
    wif = input("¿Dispone de conectividad Wifi? 1.Sí 2.No: ")
    
    if sal == 1:
        sal = True
    elif sal == 2:
        sal = False
        
    if wif == 1:
        wif = True
    elif wif == 2:
        wif = False
        
    datos = {
        "_id": id,
        "nombre": nom,
        "ciudad": ciu,
        "ubicacion": {
            "ciudad": ciu,
            "pais": pai   
        },
        "servicios": {
            "lectura_sala": sal,
            "wifi": wif
        }
    }
    
    nuevo = d.registrar(datos)
    print(f"Biblioteca registrada correctamente ({nuevo}).\n\n")
    system("cls")
    menu()
#--------------------------------------------------------------------------------------------------

def listar_bibliotecas():
    system("cls")
    can = d.cantidad_bibliotecas()
    if can == 0:
        system("cls")
        print("--- No hay datos para listar\n\n")
        system("pause")
        menu()
    else:
        bib = d.obtener_todos()
        system("cls")
        print("=== LISTADO BIBLIOTECAS ===")
        for x in bib:
            print(f"ID: {x['_id']}")
            print(f"Nombre: {x['nombre']}")
            print(f"Ciudad: {x['ubicacion']['ciudad']}")
            print(f"País: {x['ubicacion']['pais']}")
            if x['servicios']['lectura_sala'] == True:
                print("Sala: Sí")
            else:
                print("Sala: No")
            if x['servicios']['wifi'] == True:
                print("Wifi: Sí")
            else:
                print("Wifi: No")

#--------------------------------------------------------------------------------------------------

def buscar_bibliotecas():
    system("cls")
    id = int(input("Digite el _id de la biblioteca a buscar: "))
    r = d.comprobar_id(id)
    if r == 0:
       system("cls")
       print(f"La biblioteca {id} no existe\n\n")
       system("pause")
       menu()
    else:
        bib = d.obtener_buscados(id)
        system("cls")
        print("=== LISTADO BIBLIOTECAS ===")
        for x in bib:
            print(f"ID: {x['_id']}")
            print(f"Nombre: {x['nombre']}")
            print(f"Ciudad: {x['ubicacion']['ciudad']}")
            print(f"País: {x['ubicacion']['pais']}")
            if x['servicios']['lectura_sala'] == True:
                print("Sala: Sí")
            else:
                print("Sala: No")
            if x['servicios']['wifi'] == True:
                print("Wifi: Sí")
            else:
                print("Wifi: No")


#--------------------------------------------------------------------------------------------------

def actualizar_datos():
    system("cls")
    id = int(input("Digite el _id de la biblioteca a buscar: "))
    r = d.comprobar_id(id)
    if r == 0:
       system("cls")
       print(f"La biblioteca {id} no existe\n\n")
       system("pause")
       menu()
    else:
        bib = d.obtener_buscados(id)
        system("cls")
        print("=== LISTADO BIBLIOTECAS ===")
        for x in bib:
            print(f"ID: {x['_id']}")
            print(f"Nombre: {x['nombre']}")
            print(f"Ciudad: {x['ubicacion']['ciudad']}")
            print(f"País: {x['ubicacion']['pais']}")
            if x['servicios']['lectura_sala'] == True:
                print("Sala: Sí")
            else:
                print("Sala: No")
            if x['servicios']['wifi'] == True:
                print("Wifi: Sí")
            else:
                print("Wifi: No") 

#--------------------------------------------------------------------------------------------------

def eliminar_bibliotecas():
    pass

#--------------------------------------------------------------------------------------------------

def salir():
    system("cls")
    print("--- ¡ Ok. Usted Saldrá de la Aplicación ! ... ¡ Adios ! ---", end="\n\n")
    system("pause")
    os._exit(1)

#--------------------------------------------------------------------------------------------------

menu()