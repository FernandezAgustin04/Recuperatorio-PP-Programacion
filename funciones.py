import re
import random
import json
from datetime import date
from menu import *
from prueba import lista_personajes

flag_ingreso_uno = False

"""
PUNTO 1
"""
def parser_csv(path:str)->list:
    coleccion = []
    with open(path,"r",encoding="utf-8") as archivo:
        for personaje in archivo:
            personaje = personaje.strip() 
            lectura = re.split(r",|\n|\|\$%", personaje)
            key = {}
            key["id"] = int(lectura[0])
            key["nombre"] = lectura[1]
            key["raza"] = lectura[2]
            key["poder_de_pelea"] = int(lectura[3]) 
            key["poder_de_ataque"] = int(lectura[4])
            key["habilidades"] = lectura[5:] 
            coleccion.append(key)
        # print(coleccion) solo para ver que está bien dividido
        return coleccion
    
"""
PUNTO 2
"""
def separar_razas(lista):
    personajes_separados = []
    for personaje in lista:
        if re.search(r"e-H|n-H", personaje["raza"]):
            raza_separada = re.split(r"-", personaje["raza"])
            personaje["raza"] = raza_separada
        personajes_separados.append(personaje)
    return personajes_separados

def listar_raza_cantidad(lista):
    personajes_separados = separar_razas(lista)
    recuento_razas = {}
    for personaje in personajes_separados:
        if isinstance(personaje["raza"], list):
            for raza in personaje["raza"]:
                if raza in recuento_razas:
                    recuento_razas[raza] += 1
                else:
                    recuento_razas[raza] = 1
        else:
            raza = personaje["raza"]
            if raza in recuento_razas:
                recuento_razas[raza] += 1
            else:
                recuento_razas[raza] = 1
    for raza, cantidad in recuento_razas.items():
        print(f'{raza}: {cantidad}')

"""
PUNTO 3
"""   
def listar_personajes_por_raza(lista_personajes):
    razas = {}
    for personaje in lista_personajes:
        raza = personaje["raza"]
        nombre = personaje["nombre"]
        poder_ataque = personaje["poder_de_pelea"]
        if raza in razas:
            razas[raza].append((nombre, poder_ataque))
        else:
            razas[raza] = [(nombre, poder_ataque)]
    
    for raza, personajes in razas.items():
        print(raza)
        for nombre, poder_ataque in personajes:
            print(f"Nombre: {nombre}, Poder de ataque: {poder_ataque}")
        print()

"""
PUNTO 4
"""  
def listar_personajes_por_habilidad(lista, habilidad):
    personajes_habilidad = []
    for personaje in lista:
        habilidades = personaje["habilidades"]
        if habilidad in habilidades:
            personajes_habilidad.append(personaje)

    if personajes_habilidad:
        print(f"Personajes con la habilidad '{habilidad}':")
        for personaje in personajes_habilidad:
            nombre = personaje["nombre"]
            raza = personaje["raza"]
            poder_pelea = personaje["poder_de_pelea"]
            poder_ataque = personaje["poder_de_ataque"]
            promedio_poder = (poder_pelea + poder_ataque) / 2
            print(f"Nombre: {nombre}, Raza: {raza}, Promedio de poder: {promedio_poder}")
    else:
        print(f"No hay personajes con la habilidad '{habilidad}'.")

"""
PUNTO 5
"""
def guardar_registro_batalla(ganador, perdedor):
    fecha_actual = date.today().strftime("%d-%m-%y")
    entrada_registro = f"Fecha: {fecha_actual} | Ganador: {ganador} | Perdedor: {perdedor}\n"
    with open("registros_batalla.txt", "a") as archivo:
        archivo.write(entrada_registro)

def jugar_batalla():
    eleccion_jugador = int(input("Selecciona un número del 1 al 35 para elegir tu personaje: "))
    personaje_jugador = lista_personajes[eleccion_jugador - 1]

    eleccion_maquina = random.randint(1, 35)
    personaje_maquina = lista_personajes[eleccion_maquina - 1]

    print(f"Tu personaje: {personaje_jugador['nombre']}")
    print(f"Personaje de la máquina: {personaje_maquina['nombre']}")

    if personaje_jugador['poder_de_pelea'] > personaje_maquina['poder_de_pelea']:
        print("¡Has ganado la batalla!")
        guardar_registro_batalla(personaje_jugador['nombre'], personaje_maquina['nombre'])
    elif personaje_jugador['poder_de_pelea'] < personaje_maquina['poder_de_pelea']:
        print("¡Has perdido la batalla!")
        guardar_registro_batalla(personaje_maquina['nombre'], personaje_jugador['nombre'])
    else:
        print("Empate")

"""
PUNTO 6
"""
def guardar_personajes_por_raza_y_habilidad_json(lista, raza, habilidad):
    personajes_filtrados = []
    for personaje in lista:
        if personaje['raza'] == raza or habilidad in personaje['habilidades']:
            habilidades_restantes = [habilidad for habilidad in personaje['habilidades'] if habilidad != habilidad]
       
            personaje_filtrado = {
                'nombre': personaje['nombre'],
                'poder_de_ataque': personaje['poder_de_ataque'],
                'habilidades_restantes': personaje["habilidades"]
            }
            
            personajes_filtrados.append(personaje_filtrado)
            print(f"{personaje['nombre']} - {personaje['poder_de_ataque']} - {personaje['habilidades']}")
    
    if personajes_filtrados:
        nombre_archivo = f"{raza.replace(' ', '_')}_{habilidad.replace(' ', '_')}.json"
        
        with open(nombre_archivo, 'w') as archivo:
            json.dump(personajes_filtrados, archivo, indent=4)
        
        print(f"Se ha generado el archivo {nombre_archivo} correctamente.")
    else:
        print(f"No se encontraron personajes que coincidan con la raza '{raza}' o la habilidad '{habilidad}'.")

        # Obtener todas las habilidades restantes
        habilidades_restantes = []
        for personaje in lista:
            habilidades_restantes += habilidades_restantes[personaje['habilidades']]

        # Mostrar las habilidades restantes en el archivo JSON
        personajes_filtrados.append({
            'habilidades_restantes': list(habilidades_restantes)
        })

        with open(nombre_archivo, 'w') as archivo:
            json.dump(personajes_filtrados, archivo, indent=4)

        print(f"Se ha generado el archivo {nombre_archivo} correctamente.")
    return nombre_archivo
    
"""
PUNTO 7
"""
def leer_personajes_desde_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        datos_guardados = json.load(archivo)

    print("Listado de personajes:")
    for personaje in datos_guardados:
        print(f"Nombre: {personaje['nombre']}")
        print(f"Poder de ataque: {personaje['poder_de_ataque']}")
        print(f"Habilidades: {', '.join(personaje['habilidades_restantes'])}")
        print("---")

"""
PUNTO 8
"""
def salir_del_programa():
    if flag_ingreso_uno == False:
        print("[ERROR], debe ingresar el 1 antes")
    print("Gracias por utilizar el programa")
    print("Hasta luego")

"""
Requerimiento extra
Agregar una opción que permita otorgarle un 50% más de poder de pelea y un 70% más de poder de ataque a los Saiyan, 
y agregaran a sus habilidades la “transformación nivel dios”.
Guardar en un archivo CSV los personajes que hayan recibido esta actualización.
"""

def dragon_ball_mejorar_Saiyan(lista:list):
    if type(lista) == list:
        for personaje in lista:
            raza_saiyan = False
            for caracteristica in personaje["raza"]:
                if caracteristica == "saiyan":
                    raza_saiyan = True
            if raza_saiyan == True:
                agregar_lista_mejoras_personajes(personaje)
                subir_personajes_csv(personaje)
        print("se mejoraron los saiyan")
    else:
        print("No se ingreso una lista valida")

def subir_personajes_csv(personaje:dict):
    if type (personaje) == dict:
        with open("Saiyan_mejorados.csv", "a") as archivo:
            for caracteristica in personaje:
                archivo.write(f' {personaje[caracteristica]},')
            archivo.write(f'\n')
    else:
        return 1

def agregar_lista_mejoras_personajes(personaje:dict):
    if type (personaje) == dict:
        porcentaje_agregado = calcular_suma_porcentaje(personaje["poder_pelea"], 50)
        personaje["poder_pelea"] = porcentaje_agregado
        porcentaje_agregado = calcular_suma_porcentaje(personaje["poder_ataque"], 70)
        personaje["poder_ataque"] = porcentaje_agregado
        personaje["habilidades"].append("transformacion nivel dios")
    else:
        return 1

def calcular_suma_porcentaje(sacar_porcentaje:int, porcentaje:int):
    if type (sacar_porcentaje) == int and type (porcentaje) == int:
        porcentaje_calculado = sacar_porcentaje * porcentaje / 100
        porcentaje_calculado += sacar_porcentaje
        return porcentaje_calculado
    else:
        return 1


"""
EJERCICIO RECUPERATORIO
"""

#A
def ordenar_personajes_por_atributo(lista_personajes):
    atributo = input("Ingrese el atributo por el cual desea ordenar los personajes: ")
    while atributo not in lista_personajes[0]:
        print("Atributo inválido. Por favor, ingrese un atributo válido.")
        atributo = input("Ingrese el atributo por el cual desea ordenar los personajes: ")
    orden = input("Ingrese el orden de clasificación TRUE(ASCENDENTE) o FALSE(DESCENDENTE): ").upper()
    
    n = len(lista_personajes)
    if orden == "DESCENDENTE":
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if lista_personajes[j][atributo] < lista_personajes[j + 1][atributo]:
                    lista_personajes[j], lista_personajes[j + 1] = lista_personajes[j + 1], lista_personajes[j]
    else:
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if lista_personajes[j][atributo] > lista_personajes[j + 1][atributo]:
                    lista_personajes[j], lista_personajes[j + 1] = lista_personajes[j + 1], lista_personajes[j]
    
    return lista_personajes

#B
def generar_codigo_personaje(personaje):
    nombre = personaje['nombre']
    poder_ataque = personaje['poder_de_ataque']
    poder_defensa = personaje['poder_de_pelea']
    codigo = ""

    if poder_ataque > poder_defensa:
        codigo += "A"
    elif poder_defensa > poder_ataque:
        codigo += "D"
    else:
        codigo += "AD"

    codigo += "-" + str(max(poder_ataque, poder_defensa))
    codigo += "-" + str(personaje['id']).zfill(9)

    return codigo

def agregar_codigos_personajes(lista_personajes):
    for personaje in lista_personajes:
        codigo = generar_codigo_personaje(personaje)
        personaje['codigo'] = codigo

    return lista_personajes