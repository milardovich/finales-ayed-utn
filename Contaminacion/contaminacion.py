import os
import pickle
import datetime
from random import randint

medicionesDiarias = [[0 for x in range(2)] for y in range(15)]

class Medicion:
    def __init__(self):
        self.fecha = ""
        self.nro_zona = 0
        self.snap = 0.0

def formatearMedicion(medicion):
    medicion.fecha = str(medicion.fecha).ljust(20, ' ')
    medicion.nro_zona = str(medicion.nro_zona).ljust(2, ' ')
    medicion.snap = str(medicion.snap).ljust(4, ' ')

def inicializarMediciones():
    global alMediciones
    alMediciones.seek(0)
    for i in range(100):
        aux = Medicion()
        aux.nro_zona = randint(0, 14)
        aux.snap = randint(0, 350)
        formatearMedicion(aux)
        pickle.dump(aux, alMediciones)
        alMediciones.flush()

def calidadAire(snap):
    if (snap <= 50):
        return 'Buena'
    elif (snap <= 100):
        return 'Moderada'
    elif (snap <= 150):
        return 'Dañina para grupos sensibles'
    elif (snap <= 200):
        return 'Dañina para la salud'
    elif (snap <= 300):
        return 'Muy dañina para la salud'
    else:
        return 'Peligrosa'

def informeDiario():
    global afMediciones, alMediciones, medicionesDiarias

    t = os.path.getsize(afMediciones)
    alMediciones.seek(0)

    while alMediciones.tell() < t:
        aux = pickle.load(alMediciones)
        zona = int(aux.nro_zona)
        snap = float(aux.snap)

        medicionesDiarias[zona][0] += snap
        medicionesDiarias[zona][1] += 1

    zonaSnapMas = -1
    zonaSnapMenos = 999999

    zonaMas = 0
    zonaMenos = 0

    for i in range(15):
        print("Zona "+str(i))
        snapZona = medicionesDiarias[i][0]/medicionesDiarias[i][1]
        print(calidadAire(snapZona))

        if(zonaSnapMas < snapZona):
            zonaSnapMas = snapZona
            zonaMas = i
        
        if(zonaSnapMenos > snapZona):
            zonaSnapMenos = snapZona
            zonaMenos = i        

    print("Zona con mayor polución: "+str(zonaMas))
    print("Zona con menor polución: "+str(zonaMenos))

def generarMaestro():
    global afMaestro, alMaestro, afMediciones, alMediciones

    tmaestro = os.path.getsize(afMaestro)
    alMaestro.seek(tmaestro)

    t = os.path.getsize(afMediciones)
    alMediciones.seek(0)
    while alMediciones.tell() < t:
        aux = pickle.load(alMediciones)
        pickle.dump(aux, alMaestro)
    
    print("Mediciones insertadas al archivo maestro")

def limpiarTarjeta():
    os.remove(afMediciones)
    print("Tarjeta Limpiada")

def menu():
    opt = 1
    while opt != 0:
        print("Seleccione una opcion: \n1- Informe Diario\n2- Generar Maestro\n3- Limpiar Tarjeta\n0- Salir")
        opt = int(input(" "))
        while opt < 0 or opt > 3:
            opt = int(input("Ingrese una opción correcta: "))
        
        if opt == 1:
            informeDiario()
        elif opt == 2:
            generarMaestro()
        elif opt == 3:
            limpiarTarjeta()

afMediciones = "./mediciones.dat"
alMediciones = open (afMediciones, "w+b")

afMaestro = "./maestro.dat"
if not os.path.exists(afMaestro):
    alMaestro = open (afMaestro, "w+b")
else:
    alMaestro = open(afMaestro, "r+b")

inicializarMediciones()
menu()

alMediciones.close()
alMaestro.close()