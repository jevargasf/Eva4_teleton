from DAO import DAO
from os import system
import os

#--------------------------------------------------------------------------------------------------

def validar_int(ini, fin, txt):
    while True:
        try:
            op = int(input(txt))
            if ini <= op <= fin:
                return op
            else:
                raise ValueError
        except ValueError:
            print(f"Error de tipo: Por favor, ingrese un entero entre {ini} y {fin}.")
            system("pause")
            system("cls")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            system("pause")
            system("cls")

def validar_str(txt, err):
    while True:
        try:
            string = input(txt)
            if len(string) == 0:
                print(f"Error: {err}. Si quiere omitir el ingreso de este dato, digite 0 (cero).")
            elif string == '0':
                return 'N/A'
            else:
                return string
        except Exception as e:
            print(f"Error no controlado: {e}")

def validar_correo(txt):
    while True:
        try:
            string = input(txt)
            if len(string) == 0:
                print(f"Error: El correo no puede quedar vacío. Si quiere omitir el ingreso de este dato, digite 0 (cero).")
            elif '@' not in string:
                print(f"Error: Por favor, ingrese una dirección de correo válida.")
            elif string == '0':
                return 'N/A'
            else:
                return string
        except Exception as e:
            print(f"Error no controlado: {e}")

def validar_telefono(txt):
    while True:
        try:
            string = input(txt)
            if len(string) == 0:
                print(f"Error: El teléfono no puede quedar vacío. Si quiere omitir el ingreso de este dato, digite 0 (cero).")
            elif len(string.strip()) is not 9:
                print(f"Error: Por favor, ingrese un número de teléfono válido. El número telefónico debe tener 9 dígitos.")
            elif string == '0':
                return 'N/A'
            else:
                return string
        except Exception as e:
            print(f"Error no controlado: {e}")
#--------------------------------------------------------------------------------------------------

d = DAO()

#--------------------------------------------------------------------------------------------------

def menu():
    system("cls")
    txt = """ 
--------------------------------
=== Gestión de Institutos Teletón ===
--------------------------------
1.Registrar nuevo
2.Listar institutos
3.Buscar datos instituto
4.Modificar datos instituto
5.Eliminar instituto
6.Salir\n
Por favor, digite una opción: 
"""

    op = validar_int(1, 6, txt)

    if op==1:
        registrar_instituto()
    elif op == 2:
        listar_institutos()
    elif op == 3:
        buscar_instituto()
    elif op == 4:
        actualizar_instituto()
    elif op == 5:
        eliminar_instituto()
    else:
        salir()
#--------------------------------------------------------------------------------------------------

def registrar_instituto():
    system("cls")
    print("=== Registrar ===")
    txt = """
Digite el _id del nuevo registro: 
"""
    id = validar_int(1, 999999, txt)
    
    r = d.comprobar_id(id)
    if r == 1:
        system("cls")
        print(f"\n --- El id {id} ya existe. Por favor, intente nuevamente. ---\n")
        system("pause")
        menu()
    
    system("cls")
    print("=== Registrar ===")
    nom_txt = """
Digite el nombre del instituto: 
"""
    nom = validar_str(nom_txt, "El nombre del instituto no puede quedar vacío")

    system("cls")
    print("=== Registrar ===")
    zon_txt = """
Digite la zona donde se ubica el instituto:
1. Norte
2. Centro
3. Sur
"""
    zon = validar_int(1, 3, zon_txt)

    system("cls")
    print("=== Registrar ===")
    ciu_txt = """
Digite la ciudad donde se ubica el instituto: 
"""
    ciu = validar_str(ciu_txt, "La ciudad no puede quedar vacía")

    system("cls")
    print("=== Registrar ===")
    dir_txt = """
Digite la dirección donde se ubica el instituto: 
"""
    dir = validar_str(dir_txt, "La dirección no puede quedar vacía")

    system("cls")
    print("=== Registrar ===")
    cor_txt = """
Ingrese correo de contacto del instituto: 
"""
    cor = validar_correo(cor_txt)

    system("cls")
    print("=== Registrar ===")
    tel_txt = """
Ingrese teléfono de contacto del instituto. No ingrese código de país. Ej: 94393492: 
"""
    tel = validar_telefono(tel_txt)
    
    datos = {
        "_id": id,
        "nombre": nom,
        "ubicacion": {
            "zona": zon,
            "ciudad": ciu,
            "dirección": dir   
        },
        "contacto": {
            "correo": cor,
            "teléfono": tel
        }
    }
    print(datos)
    #nuevo = d.registrar(datos)
    print(f"Instituto registrado correctamente [recuperar respuesta].\n\n")
    system("pause")
    menu()
#--------------------------------------------------------------------------------------------------

def listar_institutos():
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

def buscar_instituto():
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

def actualizar_instituto():
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

def eliminar_instituto():
    pass

#--------------------------------------------------------------------------------------------------

def salir():
    system("cls")
    print("--- Saliendo del programa... ¡Muchas gracias por su preferencia! ---", end="\n\n")
    system("pause")
    os._exit(1)

#--------------------------------------------------------------------------------------------------

menu()