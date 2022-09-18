import os
import pickle
import os.path

'''
Creo los registros para Pieza, Material y Pedido, de acuerdo a lo que explicita el enunciado
'''
class Pieza:
    def __init__(self):
        self.nombre_pieza = ""
        self.materiales = [0]*15
        self.stock_disponible = 0
        self.stock_pendiente = 0
  
class Material:
	def __init__(self):
		self.descripcion = ""
		self.precio = 0.0
  
class Pedido:
    def __init__(self):
        self.nombre = ""
        self.nro_pieza = 0
        self.cant_piezas = 0
        self.monto = 0.0
        
'''
Creo los procedimientos para formatear cada uno de los registros anteriormente mencionados
'''
def formatearPieza(pieza):
    pieza.nombre_pieza = str(pieza.nombre_pieza).ljust(32, ' ')
    for i in range(15):
        pieza.materiales[i] = str(pieza.materiales[i]).ljust(2,' ')
    pieza.stock_disponible = str(pieza.stock_disponible).ljust(2, ' ')
    pieza.stock_pendiente = str(pieza.stock_pendiente).ljust(2, ' ')

def formatearMaterial(material):
    material.descripcion = str(material.descripcion).ljust(16, ' ')
    material.precio = str(material.precio).ljust(6, ' ')

def formatearPedido(pedido):
    pedido.nombre = str(pedido.nombre).ljust(8, ' ')
    pedido.nro_pieza = str(pedido.nro_pieza).ljust(2, ' ')
    pedido.cant_piezas = str(pedido.cant_piezas).ljust(2, ' ')
    pedido.monto = str(pedido.monto).ljust(6, ' ')
'''
Si bien esto no estaba en el enunciado, creo este método para poder tener información en el archivo de materiales.
Lo único que hace este método ese iterar el arreglo y cargar los valores del mismo en el archivo materiales.dat
'''
def inicializarMateriales():
    global alMateriales, afMateriales
    
    materiales = [
        ['Arcilla Blanca', '100'],
        ['Arcilla Roja', '150'],
        ['Esmalte', '200'],
        ['Agua', '250'],
        ['Plomo', '300'],
        ['Estaño', '350'],
        ['Sal', '400'],
        ['Mármol', '450'],
        ['Sílice', '500'],
        ['Feldespato', '550'],
        ['Óxido de Hierro', '600'],
        ['Yeso', '650'],
        ['Caolín', '700'],
        ['Aluminio', '750'],
        ['Berilio', '800']
    ]
    
    alMateriales.seek(0)
    
    for i in range(15):
        auxMat = Material()
        auxMat.descripcion = materiales[i][0]
        auxMat.precio = materiales[i][1]
        formatearMaterial(auxMat)
        pickle.dump(auxMat, alMateriales)
        alMateriales.flush()
        
'''
Procedimiento para cargar una nueva pieza. Lo que hago es posicionarme utilizando el método seek al final del archivo. Para saber cuál es el final del archivo utilizo el método os.path.getsize()
'''        
def cargarPieza():
    global afPiezas, alPiezas
    t = os.path.getsize(afPiezas)
    alPiezas.seek(t, 0)
    pieza = Pieza()
    pieza.nombre_pieza = input("Ingrese el nombre de la pieza: ")
    material = int(input("Ingrese el material para el cual quiera ingresar la cantidad. Ingrese 0 para continuar: "))
    while material > 0:
        if material < 15:
            cantidad = int(input("Ingrese la cantidad: "))
            pieza.materiales[material-1] = cantidad
        else:
            print("Ingrese un código válido")
        
        material = int(input("Ingrese el material para el cual quiera ingresar la cantidad. Ingrese 0 para continuar: "))
        
    pieza.stock_disponible = input("Ingrese el stock disponible: ")
    pickle.dump(pieza, alPiezas)
    alPiezas.flush()

'''
Procedimiento del tipo "helper", lo que hace es posicionarse a en la "fila" de nuestro archivo donde se encuentra el número de pieza que le pasamos como argumento (nroPieza).

Recordemos que, si el número de pieza es autoincremental que comienza en 1, la pieza con el primer número de pieza (1) va a estar en la posición 0. Luego, la pieza con el segundo número de pieza (2) va a estar en la posición 0 + el tamaño en bytes que ocupe una pieza. 

La pieza en la posición n va a estar en la posición de la pieza n-1 + el tamaño que ocupe una pieza (al usar el procedimiento formatear, todas las piezas ocupan el mismo tamaño en bytes).
'''
def posicionarseEnPieza(nroPieza):
    global alPiezas, afPiezas
    
    alPiezas.seek(0)
    aux = pickle.load(alPiezas)
    tamReg = alPiezas.tell() 
    t = os.path.getsize(afPiezas)
    
    alPiezas.seek((nroPieza-1)*tamReg)

'''
Función que calcula el precio de una pieza, dado el número de la misma. Nos posicionamos en el lugar del archivo donde se encuentre la pieza que corresponda utilizando el procedimiento posicionarseEnPieza, luego cargamos esa información en memoria, y realizamos el cálculo del precio según la cantidad de materiales que contenga la pieza.

Nótese que para los materiales, lo que hacemos es posicionarnos al comienzo del archivo, y luego iterar 15 veces para sacar el valor de los 15 materiales distintos. Necesitamos usar el load cada vez que iteramos para poder cargar esa información en memoria.
'''
def calcularPrecio(nroPieza):
    global afPiezas, alPiezas, afMateriales, alMateriales
    
    posicionarseEnPieza(nroPieza)
    
    vrPieza = pickle.load(alPiezas)
    
    auxPrecio = 0
    
    alMateriales.seek(0)
    for i in range(15):
        materialAux = pickle.load(alMateriales)
        auxPrecio += float(vrPieza.materiales[i])*float(materialAux.precio)
    
    return float(auxPrecio)

'''
Mostramos la información de una pieza en particular.
'''
def mostrarPieza(vrPieza, nroPieza):
    print(vrPieza.nombre_pieza.strip(), str(calcularPrecio(nroPieza)))

'''
Listamos las piezas. Se añadió un argumento de tipo booleano llamado "filtrar", para poder reutilizar el procedimiento tanto en el punto 2 como en el 4.
'''
def listarPieza(filtrar=False):
    global afPiezas, alPiezas
    t = os.path.getsize(afPiezas)
    if t==0:
        print ("No hay piezas registradas")
    else:
        print ("Lista de Piezas")
        print ("----------------")
        alPiezas.seek(0)
        i = 1
        while alPiezas.tell()<t:
            vrPieza = pickle.load(alPiezas)
            if(not filtrar or (filtrar and int(vrPieza.stock_disponible) < vrPieza.stock_pendiente)):
                mostrarPieza(vrPieza, i)
            i += 1
    print()

'''
Lógica para realizar un pedido. Incluye modificar el stock de una pieza si se confirma el pedido de la misma, o bien modificar el campo de stock a pedir si no se dispone de stock suficiente.
'''    
def pedidos():
    global alPiezas, afPiezas, alPedidos, afPedidos
    
    nro_pieza = int(input("Ingrese el número de pieza a pedir, ingrese 0 para volver a la sección anterior "))
    while nro_pieza != 0:
        pedido = Pedido()
        pedido.nro_pieza = nro_pieza
        pedido.nombre = input("Ingrese el nombre de la persona que realizará el pedido: ")
        pedido.cant_piezas = int(input("Ingrese la cantidad de piezas a pedir: "))
        
        
        monto = calcularPrecio(pedido.nro_pieza)*pedido.cant_piezas
        confirmoPedido = input("El monto a pagar es de "+str(monto)+". Desea continuar? S/N ")
        while confirmoPedido != "S" and confirmoPedido != "N":
            confirmoPedido = input("Ingrese S para continuar, o N para cancelar el pedido ")        

        if(confirmoPedido == "S"):    
            posicionarseEnPieza(pedido.nro_pieza)    
            vrPieza = pickle.load(alPiezas)
            if (int(vrPieza.stock_disponible) < pedido.cant_piezas):
                confirmoPedido = input("No hay stock disponible. Desea realizar un pedido diferido? S/N ")
                while confirmoPedido != "S" and confirmoPedido != "N":
                    confirmoPedido = input("No hay stock disponible. Desea realizar un pedido diferido? S/N ")
                
                if(confirmoPedido == "S"):
                    posicionarseEnPieza(pedido.nro_pieza)    
                    vrPieza.stock_pendiente += pedido.cant_piezas
                    formatearPieza(vrPieza)
                    pickle.dump(vrPieza, alPiezas)
            else:
                posicionarseEnPieza(pedido.nro_pieza)    
                vrPieza.stock_pendiente += pedido.cant_piezas
                formatearPieza(vrPieza)
                pickle.dump(vrPieza, alPiezas)
                alPiezas.flush()
                    
                formatearPedido(pedido)
                t = os.path.getsize(afPedidos)
                alPedidos.seek(t)
                pickle.dump(pedido, alPedidos)
                alPedidos.flush()
                
        
        nro_pieza = int(input("Ingrese el número de pieza a pedir, ingrese 0 para volver a la sección anterior "))
    
def menuPrincipal():
    global afPiezas, alPiezas
    opt = 1
    while opt != 0:
        print("1- Cargar nueva pieza\n2- Mostrar Piezas\n3- Pedidos de Piezas\n4- Pendientes de Fabricar\n0-Salir")
        opt = int(input("Ingrese una opción"))
        while opt < 0 or opt > 4:
            opt = int(input("Ingrese una opción correcta"))
        if (opt == 1):
            cargarPieza()
        elif (opt == 2):
            listarPieza()
        elif (opt == 3):
            pedidos()
        elif (opt == 4):
            listarPieza(True)           
        
            

afPiezas = "./piezas.dat"  
if not os.path.exists(afPiezas):   
	alPiezas = open (afPiezas, "w+b")   
else:
	alPiezas = open (afPiezas, "r+b")

'''
Inicializo el archivo de materiales. Como lo voy a escribir siempre que inicie el programa, directamente lo inicializo con w+b para que reemplace el contenido en caso de existir.
'''
afMateriales = "./materiales.dat"  
alMateriales = open (afMateriales, "w+b")   
 
afPedidos = "./pedidos.dat"  
if not os.path.exists(afPedidos):   
	alPedidos = open (afPedidos, "w+b")   
else:
	alPedidos = open (afPedidos, "r+b")

inicializarMateriales() 
menuPrincipal()

alPiezas.close()
alPedidos.close()
alMateriales.close()