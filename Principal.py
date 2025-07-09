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
    id_txt = """
Digite el _id del nuevo registro: 
"""
    id = validar_int(1, 999999, id_txt)
    
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
    if zon == 1:
        zon = 'Norte'
    elif zon == 2:
        zon = 'Centro'
    elif zon == 3:
        zon = 'Sur'

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
        "general": {"nombre": nom},
        "recursos_humanos": {
            "contacto": {
                "correo": cor,
                "telefono": tel
            }
        },
        "descripcion":{
            "ubicacion":{
                "detalle": {
                    "zona": zon,
                    "ciudad": ciu,
                    "direccion": dir   
                }
            }
        }
    }
    nuevo = d.registrar(datos)
    print(f"Instituto registrado correctamente: {nuevo}.\n\n")
    system("pause")
    menu()
#--------------------------------------------------------------------------------------------------

def listar_institutos():
    system("cls")
    can = d.cantidad_institutos()
    if can == 0:
        system("cls")
        print("--- No hay datos para listar\n\n")
        system("pause")
        menu()
    else:
        institutos = d.obtener_todos()
        system("cls")
        print("=== LISTADO INSTITUTOS ===")
        for x in institutos:
            print(f"ID: {x['_id']}")
            print(f"Nombre: {x['general']['nombre']}")
            print(f"Correo: {x['recursos_humanos']['contacto']['correo']}")
            print(f"Teléfono: +569 {x['recursos_humanos']['contacto']['telefono']}")
            print(f"Zona: {x['descripcion']['ubicacion']['detalle']['zona']}")
            print(f"Ciudad: {x['descripcion']['ubicacion']['detalle']['ciudad']}")
            print(f"Dirección: {x['descripcion']['ubicacion']['detalle']['direccion']}")
        system("pause")
        menu()

#--------------------------------------------------------------------------------------------------

def buscar_instituto():
    system("cls")
    id_txt = """
Digite el _id del instituto a buscar: 
"""
    id = validar_int(1, 999999, id_txt)
    r = d.comprobar_id(id)
    if r == 0:
       system("cls")
       print(f"El _id del instituto {id} no existe.\n\n")
       system("pause")
       menu()
    else:
        institutos = d.obtener_buscados(id)
        system("cls")
        print("=== LISTADO INSTITUTOS ===")
        for x in institutos:
            print(f"ID: {x['_id']}")
            print(f"Nombre: {x['general']['nombre']}")
            print(f"Correo: {x['recursos_humanos']['contacto']['correo']}")
            print(f"Teléfono: +569 {x['recursos_humanos']['contacto']['telefono']}")
            print(f"Zona: {x['descripcion']['ubicacion']['detalle']['zona']}")
            print(f"Ciudad: {x['descripcion']['ubicacion']['detalle']['ciudad']}")
            print(f"Dirección: {x['descripcion']['ubicacion']['detalle']['direccion']}")
        system("pause")
        menu()

#--------------------------------------------------------------------------------------------------

def actualizar_instituto():
    system("cls")
    id_txt = """
Digite el _id del instituto a actualizar: 
"""
    id = validar_int(1, 999999, id_txt)
    r = d.comprobar_id(id)
    if r == 0:
       system("cls")
       print(f"El _id del instituto {id} no existe.")
       system("pause")
       menu()
    else:
        institutos = d.obtener_buscados(id)
        system("cls")
        print("=== LISTADO INSTITUTOS ===")
        for x in institutos:
            print(f"ID: {x['_id']}")
            print(f"Nombre: {x['general']['nombre']}")
            print(f"Correo: {x['recursos_humanos']['contacto']['correo']}")
            print(f"Teléfono: +569 {x['recursos_humanos']['contacto']['telefono']}")
            print(f"Zona: {x['descripcion']['ubicacion']['detalle']['zona']}")
            print(f"Ciudad: {x['descripcion']['ubicacion']['detalle']['ciudad']}")
            print(f"Dirección: {x['descripcion']['ubicacion']['detalle']['direccion']}")
        
            system("cls")

        # CICLO WHILE QUE OFREZCA UN MENÚ PARA ACUTALIZAR.
        # SE MANTIENE EN EL CICLO OFRECIENCO ACTUALIZAR HASTA QUE DICE QUE NO
        # IF ELIF PARA ELEGIR 1 OPCIÓN DEL MENÚ
        # CUANDO SALE DEL CICLO, SE ENVÍAN LOS DATOS AL DAO
    
            print("=== Actualizar ===")
            nom_txt = """
        Digite el nuevo nombre del instituto: 
        """
            nom = validar_str(nom_txt, "El nombre del instituto no puede quedar vacío")

            system("cls")
            print("=== Actualizar ===")
            zon_txt = """
        Digite la nueva zona donde se ubica el instituto:
        1. Norte
        2. Centro
        3. Sur
        """
            zon = validar_int(1, 3, zon_txt)
            if zon == 1:
                zon = 'Norte'
            elif zon == 2:
                zon = 'Centro'
            elif zon == 3:
                zon = 'Sur'

            system("cls")
            print("=== Actualizar ===")
            ciu_txt = """
        Digite la nueva ciudad donde se ubica el instituto: 
        """
            ciu = validar_str(ciu_txt, "La ciudad no puede quedar vacía")

            system("cls")
            print("=== Actualizar ===")
            dir_txt = """
        Digite la nueva dirección donde se ubica el instituto: 
        """
            dir = validar_str(dir_txt, "La dirección no puede quedar vacía")

            system("cls")
            print("=== Actualizar ===")
            cor_txt = """
        Ingrese nuevo correo de contacto del instituto: 
        """
            cor = validar_correo(cor_txt)

            system("cls")
            print("=== Actualizar ===")
            tel_txt = """
        Ingrese nuevo teléfono de contacto del instituto. No ingrese código de país. Ej: 94393492: 
        """
            tel = validar_telefono(tel_txt)
            
            datos_nuevos = {
                "_id": id,
                "general": {"nombre": nom},
                "recursos_humanos": {
                    "contacto": {
                        "correo": cor,
                        "telefono": tel
                    }
                },
                "descripcion":{
                    "ubicacion":{
                        "detalle": {
                            "zona": zon,
                            "ciudad": ciu,
                            "direccion": dir   
                        }
                    }
                }
            }

        res = d.actualizar_instituto(id, datos_nuevos)
        print(f"Datos actualizados correctamente. Id actualizada: {res}.", end="\n\n")
        system("pause")
        menu()

#--------------------------------------------------------------------------------------------------

def eliminar_instituto():
    system("cls")
    id_txt = """
Digite el _id del instituto a eliminar: 
"""
    id = validar_int(1, 999999, id_txt)
    r = d.comprobar_id(id)
    if r == 0:
       system("cls")
       print(f"El _id del instituto {id} no existe. Imposible eliminar. Por favor, intente nuevamente.\n\n")
       system("pause")
       menu()
    else:
        system("cls")
        res = d.eliminar_instituto(id)
        print(f"Registro eliminado correctamente. Id eliminado: {res}.", end="\n\n")
        system("pause")
        menu()


#--------------------------------------------------------------------------------------------------

def salir():
    system("cls")
    print("--- Saliendo del programa... ¡Muchas gracias por su preferencia! ---", end="\n\n")
    system("pause")
    os._exit(1)

#--------------------------------------------------------------------------------------------------

menu()