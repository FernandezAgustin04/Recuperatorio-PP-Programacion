from funciones import *

flag_ingreso_uno = False

def menu():

    print("\
        1 Traer datos \n\
        2 Listar cantidad por raza \n\
        3 Listar razas \n\
        4 Listar por habilidad \n\
        5 Jugar batalla\n\
        6 Guardar Json\n\
        7 Leer Json\n\
        8 Salir del programa\n\
        9 Requerimiento extra\n\
        10 Ordenar personaje por atributo\n\
        11 Generar codigo de personaje\n\
        ")

    selector = input ("Seleccione opcion: ")
    selector = str(selector)

    return selector


respuesta = True
while (respuesta == True):
    opcion = menu()

    match opcion:
        case "1":
            print("Eligió 'Traer datos'")
            lista = parser_csv("DBZ.csv")
            flag_ingreso_uno = True
        case "2":
            if flag_ingreso_uno == True:
                print("Eligio 'Listar cantidad por raza'")
                listar_raza_cantidad(lista)
            else:
                salir_del_programa()
                break
        case "3":
            if flag_ingreso_uno == True:           
                print("Eligio 'Listar personajes por raza'")
                listar_personajes_por_raza(lista)
            else:
                salir_del_programa()
                break
        case "4":
            if flag_ingreso_uno == True:
                print("Eligio 'Listar personajes por habilidad'")
                habilidad = input("Ingrese habilidad  ")
                listar_personajes_por_habilidad(lista, habilidad)
            else:
                salir_del_programa()
                break
        case "5":
            if flag_ingreso_uno == True:
                print("Eligio 'Jugar batalla'")
                jugar_batalla()
            else:
                salir_del_programa()
                break
        case "6":
            if flag_ingreso_uno == True:
                print("Eligio 'Guardar Json'")        
                # El usuario ingresa la raza y la habilidad
                raza_ingresada = input("Ingrese la raza: ")
                habilidad_ingresada = input("Ingrese la habilidad: ")
                # Guardar los personajes que cumplen los criterios en un archivo JSON
                guardar_personajes_por_raza_y_habilidad_json(lista, raza_ingresada, habilidad_ingresada)
            else:
                salir_del_programa()
                break
            flag_punto_seis = True
        case "7":
            if flag_punto_seis == True:
                print("Eligio 'Leer Json'")
                nombre_archivo = guardar_personajes_por_raza_y_habilidad_json(lista, raza_ingresada, habilidad_ingresada)
                leer_personajes_desde_json(nombre_archivo)
            else:
                salir_del_programa()
                break
        case "8":
            salir_del_programa()
            break
        case "9":
            if flag_ingreso_uno == True:
                print("Eligio 'requerimiento extra'")
                dragon_ball_mejorar_Saiyan(lista)
                pass
            else:
                salir_del_programa()
                break
        case "10":
            if flag_ingreso_uno == True:
                print("Eligio ejercicio A del recuperatorio")
            else:
                salir_del_programa()
                break
        case "11":
            if flag_ingreso_uno == True:
                print("Eligio ejercicio B del recuperatorio")
            else:
                salir_del_programa()
                break
                
            
