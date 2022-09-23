import os
import pickle
import os.path
import datetime
from random import randint

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
    for i in range(15):
        aux = Medicion()
        aux.nro_zona = i
        aux.snap = randint(0, 500)
        pickle.dump(aux, alMediciones)
        
def informeDiario():
    global alMediciones, afMediciones
    alMediciones.seek(0)        
        
afMediciones = "./mediciones.dat"
alMediciones = open (afMediciones, "w+b")

afMaestro = "./maestro.dat"
if not os.path.exists(afMaestro):
    alMaestro = open (afMaestro, "w+b")
else:
    alMaestro = open(afMaestro, "r+b")

inicializarMediciones()

alMediciones.close()
alMaestro.close()