from DAO import DAO
from os import system
import os

#--------------------------------------------------------------------------------------------------

def validar_int(ini, fin, txt, err):
    while True:
        try:
            op = int(input(txt))
            if ini <= op <= fin:
                return op
            else:
                print(err)
                system("pause")
                system("cls")
        except ValueError:
            print(f"Error de tipo: Por favor, ingrese un entero entre {ini} y {fin}.")
            system("pause")
            system("cls")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            system("pause")
            system("cls")

#--------------------------------------------------------------------------------------------------

d = DAO()

#--------------------------------------------------------------------------------------------------

def menu():
    system("cls")
    txt = """ 
--------------------------------
=== Gestión de Centros Teletón ===
--------------------------------
1.Registrar centro Teletón
2.Listar centros Teletón
3.Buscar centro Teletón
4.Modificar datos centro Teletón
5.Eliminar centro Teletón
6.Salir\n
Por favor, digite una opción: 
"""

    op = validar_int(1, 6, txt, "Fuera de rango: Por favor, ingrese una opción válida.\n")

    if op==1:
        registrar_centro()
    elif op == 2:
        listar_centros()
    elif op == 3:
        buscar_centro()
    elif op == 4:
        actualizar_centro()
    elif op == 5:
        eliminar_centros()
    else:
        salir()
#--------------------------------------------------------------------------------------------------

def registrar_centro():
    system("cls")
    print("=== Registrar ===")
    id = int(input("Digite el _id del centro: "))
    
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

def listar_centros():
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

def buscar_centro():
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

def actualizar_centro():
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

def eliminar_centros():
    pass

#--------------------------------------------------------------------------------------------------

def salir():
    system("cls")
    print("--- Saliendo del programa... ¡Muchas gracias por su preferencia! ---", end="\n\n")
    system("pause")
    os._exit(1)

#--------------------------------------------------------------------------------------------------

menu()