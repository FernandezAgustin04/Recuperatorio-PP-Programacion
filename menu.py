from funciones import *

flag_tres = False

def menu():

    print("\
        1 Traer datos \n\
        2 Listar cantidad por raza \n\
        3 Listar razas \n\
        4 Listar por habilidad \n\
        5 Jugar batalla\n\
        6 Guardar Json\n\
        7 Leer Json\n\
        8 Requerimiento extra\n\
        9 Ordenar personaje por atributo\n\
        10 Generar codigo de personaje\n\
        11 Agregar codigo\n\
        12 Salir del programa\
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
            lista_personajes = parser_csv("DBZ.csv")
            flag_ingreso_uno = True
        case "2":
            if flag_ingreso_uno == True:
                if flag_tres == True:
                    print("Eligio 'Listar cantidad por raza'")
                    listar_raza_cantidad(lista_personajes)
                else:
                    print("Error, primero ingrese el 3")
            else:
                salir_del_programa()
                break
        case "3":
            if flag_ingreso_uno == True:
                flag_tres = True           
                print("Eligio 'Listar personajes por raza'")
                listar_personajes_por_raza(lista_personajes)
            else:
                salir_del_programa()
                break
        case "4":
            if flag_ingreso_uno == True:
                print("Eligio 'Listar personajes por habilidad'")
                habilidad = input("Ingrese habilidad  ")
                listar_personajes_por_habilidad(lista_personajes, habilidad)
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
                guardar_personajes_por_raza_y_habilidad_json(lista_personajes, raza_ingresada, habilidad_ingresada)
            else:
                salir_del_programa()
                break
            flag_punto_seis = True
        case "7":
            if flag_punto_seis == True:
                print("Eligio 'Leer Json'")
                nombre_archivo = guardar_personajes_por_raza_y_habilidad_json(lista_personajes, raza_ingresada, habilidad_ingresada)
                leer_personajes_desde_json(nombre_archivo)
            else:
                salir_del_programa()
                break
        case "8":
            if flag_ingreso_uno == True:
                print("Eligio 'requerimiento extra'")
                dragon_ball_mejorar_Saiyan(lista_personajes)
                print(lista_personajes)
            else:
                salir_del_programa()
                break
        case "9":
            if flag_ingreso_uno == True:
                print("Eligio ejercicio A del recuperatorio")
                print(ordenar_personajes_por_atributo(lista_personajes))
        case "10":
            if flag_ingreso_uno == True:
                print("Codigos generados con exito")
            else:
                salir_del_programa()
                break
        case "11":
            personajes_con_codigos = agregar_codigos_personajes(lista_personajes)
            for personaje in personajes_con_codigos:
                print(personaje)
        case "12":
            salir_del_programa()
            break
                        

                
            

