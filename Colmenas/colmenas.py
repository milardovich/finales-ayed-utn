import os
import pickle
import os.path
import datetime

'''
Creo los registros para Colmena y Zona, de acuerdo a lo que explicita el enunciado
'''


class Colmena:
    def __init__(self):
        self.codigo_colmena = 0
        self.nro_zona = 0
        self.fecha_adquisicion = ""
        self.estado = False
<<<<<<< HEAD
        self.porcentajes_produccion = [[0 for x in range(4)] for y in range(10)] 
  
=======
        self.porcentajes_produccion = [
            [0 for x in range(4)] for y in range(10)]


>>>>>>> 53c2c20 (WIP final colmenas, agregado los close en finales de boletos y cerámica)
class Zona:
    def __init__(self):
        self.descripcion = ""


'''
Creo los procedimientos para formatear cada uno de los registros anteriormente mencionados
'''


def formatearColmena(colmena):
    colmena.codigo_colmena = str(colmena.codigo_colmena).ljust(3, ' ')
    colmena.nro_zona = str(colmena.nro_zona).ljust(3, ' ')
    colmena.fecha_adquisicion = str(colmena.fecha_adquisicion).ljust(10, ' ')
    for i in range(10):
        for j in range(4):
            colmena.porcentajes_produccion[i][j] = str(colmena.porcentajes_produccion[i][j]).ljust(3, ' ')
<<<<<<< HEAD
=======

>>>>>>> 53c2c20 (WIP final colmenas, agregado los close en finales de boletos y cerámica)

def formatearZona(zona):
    zona.descripcion = str(zona.descripcion).ljust(30, ' ')

<<<<<<< HEAD
def inicializarZonas():
    global alZonas, afZonas
    
=======

def inicializarZonas():
    global alZonas, afZonas

>>>>>>> 53c2c20 (WIP final colmenas, agregado los close en finales de boletos y cerámica)
    zonas = [
        'Zona 1',
        'Zona 2',
        'Zona 3',
        'Zona 4',
        'Zona 5',
        'Zona 6'
    ]
<<<<<<< HEAD
    
    alZonas.seek(0)
    
=======

    alZonas.seek(0)

>>>>>>> 53c2c20 (WIP final colmenas, agregado los close en finales de boletos y cerámica)
    for i in range(6):
        auxZona = Zona()
        auxZona.descripcion = zonas[i]
        formatearZona(auxZona)
        pickle.dump(auxZona, alZonas)
        alZonas.flush()

<<<<<<< HEAD
def colmenaExiste(codigoColmena):
	global afColmenas, alColmenas
	alColmenas.seek(0)
	t = os.path.getsize(afColmenas)
 
	if t == 0:
		return False

	aux = pickle.load(alColmenas)
	tamReg = alColmenas.tell() 
	cantReg = t // tamReg

 
	inicio = 0
	fin = cantReg-1
	encontrado = False 					
	while not encontrado and inicio <= fin:
		medio = (inicio + fin) // 2 
		alColmenas.seek(medio*tamReg, 0)
		vrColmena = pickle.load(alColmenas)
		if int(vrColmena.codigo_colmena) == codigoColmena:
			encontrado = True
		else:
			if codigoColmena < int(vrColmena.codigo_colmena):
				fin = medio - 1
			else:
				inicio = medio + 1
		
	if int(vrColmena.codigo_colmena) == codigoColmena:						
		return True					
	else:
		return False
=======
def posicionarseEnColmena(codigoColmena):
    global alColmenas, afColmenas
    
    t = os.path.getsize(alColmenas)
    alColmenas.seek(0, 0)
    while alColmenas.tell()<t and aux.codigo_colmena != codigoColmena:
        pos = alColmenas.tell()
        aux = pickle.load(alColmenas)
    return pos

def colmenaExiste(codigoColmena):
    global afColmenas, alColmenas, vrColmena
    alColmenas.seek(0)
    t = os.path.getsize(afColmenas)

    if t == 0:
        return False

    aux = pickle.load(alColmenas)
    tamReg = alColmenas.tell()
    cantReg = t // tamReg

    inicio = 0
    fin = cantReg-1
    encontrado = False
    while not encontrado and inicio <= fin:
        medio = (inicio + fin) // 2
        alColmenas.seek(medio*tamReg, 0)
        vrColmena = pickle.load(alColmenas)
        if int(vrColmena.codigo_colmena) == codigoColmena:
            encontrado = True
        else:
            if codigoColmena < int(vrColmena.codigo_colmena):
                fin = medio - 1
            else:
                inicio = medio + 1
    if int(vrColmena.codigo_colmena) == codigoColmena:
        return True
    else:
        return False


def zonaExiste(zona):
    global afZonas, alZonas
    alZonas.seek(0)
    aux = pickle.load(alZonas)
    tamReg = alZonas.tell()
    t = os.path.getsize(afZonas)
    cant = int(t / tamReg)
    if zona <= cant:
        return True
    else:
        return False

>>>>>>> 53c2c20 (WIP final colmenas, agregado los close en finales de boletos y cerámica)

def zonaExiste(zona):
    global afZonas, alZonas
    alZonas.seek(0)
    aux = pickle.load(alZonas)
    tamReg = alZonas.tell() 
    t = os.path.getsize(afZonas)
    cant = int(t / tamReg)
    if zona <= cant:
        return True
    else:
        return False

def adquirirColmena():
    global alColmenas, afColmenas
<<<<<<< HEAD
    
    continuar = True
    while continuar:
        auxColmena = Colmena()
        
        auxColmena.codigo_colmena = int(input("Ingrese el código de la colmena a añadir: "))
        while(colmenaExiste(auxColmena.codigo_colmena)):
            auxColmena.codigo_colmena = int(input("Ingrese un código de colmena válido: "))
            
        auxColmena.nro_zona = int(input("Ingrese el código de la zona a añadir: "))
        while(not zonaExiste(auxColmena.nro_zona)):
            auxColmena.nro_zona = int(input("Ingrese un código de zona válido: "))
            
        auxColmena.fecha_adquisicion = datetime.datetime.now().strftime("%x")
        
        auxColmena.estado = True
        
        formatearColmena(auxColmena)
        
        t = os.path.getsize(afColmenas)
        alColmenas.seek(t)
        
        pickle.dump(auxColmena, alColmenas)
        alColmenas.flush()
        
        opt = input("Desea cargar otra colmena? S/N")
        while opt.lower() != "s" and opt.lower() != "n":
        	opt = input("Ingrese una opción válida: S para continuar con otra carga / N para no cargar una nueva colmena")
         
        if (opt.lower() == "n"):
            continuar = False

def cosecha():
    global alColmenas, afColmenas
    
    continuar = True
    while continuar:
        codigoColmena = int(input("Ingrese el código de la colmena a añadir: "))
        while(colmenaExiste(codigoColmena)):
            codigoColmena = int(input("Ingrese un código de colmena válido: "))
            
        opt = input("Desea cosechar otra colmena? S/N")
        while opt.lower() != "s" and opt.lower() != "n":
        	opt = input("Ingrese una opción válida: S para continuar con otra cosecha / N para volver al menu")
         
        if (opt.lower() == "n"):
            continuar = False
=======

    continuar = True
    while continuar:
        auxColmena = Colmena()

        auxColmena.codigo_colmena = int(input("Ingrese el código de la colmena a añadir: "))
        while (colmenaExiste(auxColmena.codigo_colmena)):
            auxColmena.codigo_colmena = int(input("Ingrese un código de colmena válido: "))

        auxColmena.nro_zona = int(input("Ingrese el código de la zona a añadir: "))

        while (not zonaExiste(auxColmena.nro_zona)):
            auxColmena.nro_zona = int(input("Ingrese un código de zona válido: "))

        auxColmena.fecha_adquisicion = datetime.datetime.now().strftime("%x")

        auxColmena.estado = True

        formatearColmena(auxColmena)

        t = os.path.getsize(afColmenas)
        alColmenas.seek(t)

        pickle.dump(auxColmena, alColmenas)
        alColmenas.flush()

        opt = input("Desea cargar otra colmena? S/N")
        while opt.lower() != "s" and opt.lower() != "n":
            opt = input("Ingrese una opción válida: S para continuar con otra carga / N para no cargar una nueva colmena")

        if (opt.lower() == "n"):
            continuar = False


def cosecha():
    global alColmenas, afColmenas, arProduccion, vrColmena

    continuar = True
    while continuar:
        codigoColmena = int(input("Ingrese el código de la colmena a cosechar: "))

        while (not colmenaExiste(codigoColmena) and vrColmena.estado == False):
            codigoColmena = int(input("Ingrese un código de colmena válido: "))

        # Creo una variable auxiliar, para no tener que recorrer de vuelta todo el arreglo al calcular el porcentaje de producción de miel
        cantAuxMiel = 0
        for i in range(4):
            for j in range(10):
                vrColmena[i][j] = int(
                    input("Ingrese el porcentaje de "+arProduccion[i]+" en el cuadro "+str(j)))
                # Controlo que el porcentaje de producción esté entre 0 y 100, caso contrario vuelvo a pedir el valor
                while vrColmena[i][j] < 0 or vrColmena[i][j] > 100:
                    vrColmena[i][j] = int(
                        input("Ingrese el porcentaje de "+arProduccion[i]+" en el cuadro "+str(j)))
                # Si estoy cargando miel, le sumo el porcentaje de producción a la variable cantAuxMiel
                if (i == 0):
                    cantAuxMiel += vrColmena[i][j]

        # Chequeo que el porcentaje total de miel supere o no el 50%, para definir el estado de la colmena
        if cantAuxMiel / 10 > 50:
            vrColmena.estado = False
        else:
            vrColmena.estado = True

        posicionarseEnColmena(vrColmena.codigo_colmena)
        pickle.dump(vrColmena, alColmenas)
        alColmenas.flush()

        opt = input("Desea cosechar otra colmena? S/N")
        while opt.lower() != "s" and opt.lower() != "n":
            opt = input("Ingrese una opción válida: S para continuar con otra cosecha / N para volver al menu")

        if (opt.lower() == "n"):
            continuar = False

>>>>>>> 53c2c20 (WIP final colmenas, agregado los close en finales de boletos y cerámica)

def menuPrincipal():
    opt = 1
    while opt != 0:
        print("1- Adquisición de nuevas colmenas\n2- Cosecha\n0-Salir")
        opt = int(input("Ingrese una opción"))
        while opt < 0 or opt > 4:
            opt = int(input("Ingrese una opción correcta"))

        if opt == 1:
            adquirirColmena()
        elif opt == 2:
            cosecha()
<<<<<<< HEAD
            
afColmenas = "./colmenas.dat"  
if not os.path.exists(afColmenas):   
	alColmenas = open (afColmenas, "w+b")   
else:
	alColmenas = open (afColmenas, "r+b")
 
afZonas = "./zonas.dat"  
alZonas = open (afZonas, "w+b")   

inicializarZonas()
menuPrincipal()            
=======


vrColmena = Colmena()
arProduccion = [
                'Miel', 
                'Propóleo', 
                'Cera', 
                'Polen'
            ]

afColmenas = "./colmenas.dat"
if not os.path.exists(afColmenas):
    alColmenas = open (afColmenas, "w+b")
else:
    alColmenas = open(afColmenas, "r+b")

afZonas = "./zonas.dat"
alZonas = open (afZonas, "w+b")

inicializarZonas()
menuPrincipal()

alZonas.close()
alColmenas.close()
>>>>>>> 53c2c20 (WIP final colmenas, agregado los close en finales de boletos y cerámica)
