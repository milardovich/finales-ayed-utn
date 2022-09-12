import os
import pickle
import os.path

'''
Creo los registros para Colmena y Zona, de acuerdo a lo que explicita el enunciado
'''
class Colmena:
    def __init__(self):
        self.codigo_colmena = 0
        self.nro_zona = 0
        self.fecha_adquisicion = ""
        self.estado = False
        self.porcentajes_produccion = [[0]*10]*4
  
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
            colmena.porcentales_produccion[i][j] = str(colmena.porcentales_produccion[i][j]).ljust(3, ' ')

def formatearZona(zona):
    zona.descripcion = str(zona.descripcion).ljust(30, ' ')

def colmenaExiste(codigoColmena):
	global afColmenas, alColmenas
	alColmenas.seek (0, 0)
	aux = pickle.load(alColmenas)
	tamReg = alColmenas.tell() 
	cantReg = os.path.getsize(afColmenas) // tamReg
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

def adquirirColmena():
    codigoColmena = int(input("Ingrese el código de la colmena a añadir: "))
    while(not colmenaExiste(codigoColmena)):
        codigoColmena = int(input("Ingrese el código de la colmena a añadir: "))
        

def menuPrincipal():
    opt = 1
    while opt != 0:
        print("1- Adquisición de nuevas colmenas\n2- Cosecha\n0-Salir")
        opt = int(input("Ingrese una opción"))
        while opt < 0 or opt > 4:
            opt = int(input("Ingrese una opción correcta"))
            
        if opt == 1:
            adquirirColmena()
            
afColmenas = "./colmenas.dat"  
if not os.path.exists(afColmenas):   
	alColmenas = open (afColmenas, "w+b")   
else:
	alColmenas = open (afColmenas, "r+b")
 
afZonas = "./zonas.dat"  
alZonas = open (afZonas, "w+b")   

            