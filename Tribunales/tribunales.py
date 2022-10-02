import os
import pickle
from random import randint

class Juicio:
    def __init__(self):
        self.nro_juicio = 0
        self.id = 0
        self.juzgado = 0
        self.ano = 0
        self.caratula = ""
        self.nro_cliente = 0
        self.cliente = ""
        self.estado = True

class Actuacion:
    def __init__(self):
        self.id = 0
        self.descripcion = ""
        self.cant_hs = 0.0
        self.gastos = 0.0

def formatearJuicio(juicio):
    juicio.nro_juicio = str(juicio.nro_juicio).ljust(7, ' ')
    juicio.id = str(juicio.id).ljust(7, ' ')
    juicio.juzgado = str(juicio.juzgado).ljust(7, ' ')
    juicio.ano = str(juicio.ano).ljust(4, ' ')
    juicio.caratula = juicio.caratula.ljust(64, ' ')
    juicio.cliente = juicio.cliente.ljust(32, ' ')

def formatearActuacion(actuacion):
    actuacion.id = str(actuacion.id).ljust(7, ' ')
    actuacion.descripcion = str(actuacion.descripcion).ljust(64, ' ')
    actuacion.cant_hs = str(actuacion.cant_hs).ljust(6, ' ')
    actuacion.gastos = str(actuacion.gastos).ljust(6, ' ')
    