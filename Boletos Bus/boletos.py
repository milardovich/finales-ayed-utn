import os
import pickle
import os.path

class Boleto:
	def __init(self):
		self.nro_tarjeta = 0
		self.dia = 0
		self.mes = 0
		self.hora = 0
		self.nro_colectivo = 0
		self.monto_viaje = 0.0

class Empresa:
	def __init(self):
		self.nombre = ''

def formatearBoleto(boleto):
	boleto.nro_tarjeta = str(boleto.nro_tarjeta).ljust(12, ' ')
	boleto.dia = str(boleto.dia).ljust(2,' ')
	boleto.mes = str(boleto.mes).ljust(2,' ')
	boleto.hora = str(boleto.hora).ljust(2,' ')
	boleto.nro_colectivo = str(boleto.nro_colectivo).ljust(2,' ')
	boleto.monto_viaje = str(boleto.monto_viaje).ljust(4,' ')

def formatearEmpresa(empresa):
	empresa.nombre = str(empresa.nombre).ljust(1, ' ') 

def cargarBoleto(afBoleto, alBoleto):
	b = Boleto()
	b.nro_tarjeta = input("Ingrese nro de tarjeta: ")
	b.dia = input("Ingrese dia: ")
	b.mes = input("Ingrese mes: ")
	b.hora = input("Ingrese hora: ")
	b.nro_colectivo = input("Ingrese nro de colectivo (0 para empresa A, 1 para empresa B y 2 para empresa C): ")
	b.monto_viaje = input("Ingrese monto del viaje: ")
	formatearBoleto(b)
	pickle.dump(b, alBoleto)
	alBoleto.flush()
	mostrarBoleto(b)

def mostrarBoleto(a):
	print(a.nro_tarjeta.strip(), a.dia.strip(), a.mes.strip(), a.hora.strip(), a.nro_colectivo.strip(), a.monto_viaje.strip())

def ordenarBoletos(afBoleto, alBoleto):
    alBoleto.seek (0, 0)
    aux = pickle.load(alBoleto)
    tamReg = alBoleto.tell() 
    t = os.path.getsize(afBoleto)
    cant = int(t / tamReg)  
    for i in range(0, cant-1):
        for j in range (i+1, cant):
            alBoleto.seek (i*tamReg, 0)
            auxi = pickle.load(alBoleto)
            alBoleto.seek (j*tamReg, 0)
            auxj = pickle.load(alBoleto)
            if (auxi.mes > auxj.mes):
                alBoleto.seek (i*tamReg, 0)
                pickle.dump(auxj, alBoleto)
                alBoleto.seek (j*tamReg, 0)
                pickle.dump(auxi,alBoleto)
                alBoleto.flush()
                
def altaBoletos(afBoleto, alBoleto):
    t = os.path.getsize(afBoleto)
    if t==0:
        print ("No hay viajes registrados")
    else:
        print ("Lista de Boletos")
        print ("----------------")
        alBoleto.seek(0, 0)
        while alBoleto.tell()<t:
            vrBoleto = pickle.load(alBoleto)
            mostrarBoleto(vrBoleto)
    print()
    cargarBoleto(afBoleto, alBoleto)
    ordenarBoletos(afBoleto, alBoleto)


'''
Este procedimiento se va a llamar cada vez que se ejecute el programa principal. Es usado para crear el archivo de empresas con contenido por defecto.
'''
def inicializarEmpresas(afEmpresa, alEmpresa):
    empresas = ['A','B','C']
    alEmpresa.seek(0,0)
    for i in range(len(empresas)):
        aux = Empresa()
        aux.nombre = empresas[i]
        formatearEmpresa(aux)
        pickle.dump(aux, alEmpresa)
        alEmpresa.flush()
    

def reporte(afBoleto, alBoleto, mes):
    '''
    Inicializamos un arreglo de 3 x 30 x 2, donde 
    nuestro primer índice (del 0 al 2) es nuestra empresa
    nuestro segundo índice (del 0 al 29) es nuestro día del mes (damos por sentado que todos los meses tienen 30 días)
    Nuestro último índice (del 0 al 1) va a ser para obtener la cantidad de pasajes (primer índice) y la sumatoria obtenida del pago de los mismos
    '''
    dataAux = [[[0 for x in range(3)]for y in range(30)] for z in range(3)]
    
    '''
    Creamos un arreglo de 3 x 2 donde
    El primer índice (del 0 al 2) es nuestra empresa
    El segundo índice (del 0 al 1) va a ser la cantidad de boletos totales vendidos por la empresa (en el caso del 0) y el monto total vendido (en el caso del 1)
    '''
    metricasAux = [[0 for x in range(3)]for y in range(3)]
        
    '''
    Vamos a recorrer todo el archivo desde el comienzo, hasta que encontremos el primer boleto ingresado en el mes del mismo. Cuando lo encontremos, vamos a empezar a guardar los datos dentro de nuestro array auxiliar (dataAux), hasta que lleguemos al próximo mes. Cuando lleguemos al próximo mes vamos a cortar
    '''
    alBoleto.seek(0, 0)
    t = os.path.getsize(afBoleto)
    mesAux = 0
    while alBoleto.tell() < t and mesAux <= mes:
        vrBoleto = pickle.load(alBoleto)
        if(int(vrBoleto.mes) == mes):
            dataAux[int(vrBoleto.nro_colectivo)][int(vrBoleto.dia)][0] += 1
            dataAux[int(vrBoleto.nro_colectivo)][int(vrBoleto.dia)][1] += float(vrBoleto.monto_viaje)

            metricasAux[int(vrBoleto.nro_colectivo)][0] += 1
            metricasAux[int(vrBoleto.nro_colectivo)][1] += float(vrBoleto.monto_viaje)
    
    print("Reporte para el mes ", str(mes))        
    for i in range(3):
        empresa = nombreEmpresa(i)
        print("Empresa: ", empresa, " | viajes: ", str(metricasAux[i][0]), " | total: ",str(metricasAux[i][1])," pesos")
        for j in range(30):
            print("Dia: ", str(j), " viajes: ", str(dataAux[i][j][0]), " total: ", str(dataAux[i][j][1])," pesos")
        print()
  
'''
Función para buscar el nombre de la empresa de acuerdo al número de coche
    0 = Empresa A
    1 = Empresa B
    2 = Empresa C
'''  
def nombreEmpresa(i):
    alEmpresa.seek(0, 0)
    aux = pickle.load(alEmpresa)
    tamReg = alEmpresa.tell() 
    t = os.path.getsize(afEmpresa)
    alEmpresa.seek (i*tamReg, 0)
    vrEmpresa = pickle.load(alEmpresa)
    return vrEmpresa.nombre
              
def menuPrincipal():
    opt = 1
    while opt != 0:
        print("1- Ingresar un nuevo viaje\n2-Obtener reporte\n0-Salir")
        opt = int(input("Ingrese una opcion"))
        if(opt == 1):
            altaBoletos(afBoleto, alBoleto)
        elif(opt == 2):
            mes = int(input("Ingrese el mes para el cuál desea generar el reporte: "))
            while mes < 1 or mes > 12:
                mes = int(input("Ingrese el mes para el cuál desea generar el reporte: "))
            reporte(afBoleto, alBoleto, mes)
        elif opt > 2 or opt < 0:
            print("Ingrese una opción correcta")

'''
Inicialización de las variables de archivos. Vamos a usar el archivo boletos.dat para los boletos, y empresas.dat para las empresas
'''							
afBoleto = "./boletos.dat"  
if not os.path.exists(afBoleto):   
	alBoleto = open (afBoleto, "w+b")   
else:
	alBoleto = open (afBoleto, "r+b")

afEmpresa = "./empresas.dat"
alEmpresa = open (afEmpresa, "w+b")
inicializarEmpresas(afEmpresa, alEmpresa)

menuPrincipal()