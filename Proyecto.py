import csv
import time
class MaquinaExpendedora:

    """
    En esta clase se definen los atributos y metodos para una maquina expendedora

    utiliza un diccionario llamado productos y dinero de tipo flotante 

    crea un objeto maquina 
    """

    def __init__(self, productos: dict, dinero: float) -> None:

        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        diccionario llamado productos, dinero que contiene la maquina

        Return:
        no retorna nada
        """

        self.productos = productos
        self.dinero = dinero

    def EntregarProducto(self, Codigo_llave: int)-> str:

        """
        Esta funcion sirve para entregar los productos al usuario

        Arg:
        Codigo_llave de tipo entero

        Return:
        retorna el producto que esta en el diccionario
        """
        producto = self.productos[Codigo_llave]
        if producto.cantidad > 0:    
            producto.cantidad = producto.cantidad-1
            return self.productos.get(Codigo_llave)
        if producto.cantidad < 0:
            print("El producto se encuentra agotado :C")

    def SeleccionarProducto(self)->None:
        print("Seleccione la opcion a realizar: ")
        while 1:
            try:
                opcion = int(input("1. Enlistar todos los productos\n2. Enlistar Productos por tipo\n: "))
                break
            except ValueError:
                print('Opción no reconocida\tIntente de nuevo')
        if(opcion == 1):
            self.EnlistarProducto()
        if(opcion == 2):
            self.EnlistarProductos_Tipo()
            
    def EnlistarProducto(self)->None:
            
        """
        Esta funcion va a enlistar todos los productos disponibles en la maquina expendedora

        Arg:
        No tiene

        Return:
        no retorna nada
        """
        print('----Bienvenido a maquina expendedora-----')
        print('Contamos con los siguientes productos')
        lp=[]
        for a in self.productos.values():
            lp.append(f'{a.codigo} : {a.nombre}(${a.precio})    ')
        print(lp)

    def EnlistarProductos_Tipo(self)->None:
        """
        Esta funcion va a enlistar todos los productos disponibles en la maquina expendedora

        Arg:
        No tiene

        Return:
        no retorna nada
        """
        print('----Bienvenido a maquina expendedora-----')
        print('Bebida, Botana, Galletas. Son los tipos de productos con los que esta maquina cuenta')
        tipo = str(input("Introduzca el tipo de productos que desea mostrar: "))
        lp=[] 
        if tipo.lower() == "bebida":        
            print('BEBIDAS')
            for a in self.productos.values():
                if a.tipo =='Bebida':
                    lp.append(f'{a.codigo} : {a.nombre}(${a.precio})    ')
            print(lp)
        if tipo.lower() == "botana":
            print('BOTANAS')
            for a in self.productos.values():
                if a.tipo=='Botana':
                    lp.append(f'{a.codigo} : {a.nombre}(${a.precio})    ')
            print(lp)
        if tipo.lower() == "galletas":
            print('GALLETAS')
            for a in self.productos.values():
                if a.tipo=='Galletas':
                    lp.append(f'{a.codigo} : {a.nombre}(${a.precio})    ')
            print(lp)
        else:
            print("Introduzca el tipo correcto: ")
            
    def AgregarProducto(self, Producto):

        """
        Esta funcion va a agregar productos a la lista de productos disponibles de la maquina

        Arg:
        producto (diccionario)

        Return:
        no retorna nada
        """
        
        llave = Producto.codigo
        self.productos.setdefault(llave, Producto)
            
            
            
    def EscribirRecibo(self):
        """
        Esta funcion va a escribir el recibo de la compra del producto o productos

        Arg:
        No tienes

        Return:
        no retorna nada
        """
        with open('datos.csv', 'w') as archivo_csv:
            for producto in self.productos.values():
                archivo_csv.write(f'Nombre: {producto.nombre}\t\tCodigo: {producto.codigo}\t\tCantidad: {producto.cantidad}\n')  
    def Menu(self):
        return "\n\n1.Iniciar Usuario Premium\n2.Actualizar Productos\n3.Seleccionar Producto\n4.Almacenar nuevo producto (Premium)\n5. Salir\n: "

    def ActualizarValores(self, contraseña):
        if contraseña != None:
            self.EnlistarProducto()
            while(True):
                producto_clave = str(input("Introduzca la clave del producto a modificar"))
                producto = self.productos.get(producto_clave)
                opcion = int(input("\tModificar:\n\t\t1.Nombre\n\t\t2.Precio\n\t\t3.Clave\n\t\t4.Tipo\n\t\t5.Color\n\t\t6.Contenido\n\t\t7.Marca\n\t\t8.Cantidad\n\t\t9.Salir"))
                valAct = str(input("Introduzca el nuevo valor"))
                
                if opcion == 1:
                    producto.setNombre(valAct)
                if opcion == 2:
                    producto.setPrecio(float(valAct))
                if opcion == 3:
                    producto.setCodigo(valAct)
                if opcion == 4:
                    producto.setTipo(valAct)
                if opcion == 5:
                    producto.setColor(valAct)
                if opcion == 6:
                    producto.setContenido(valAct)
                if opcion == 7:
                    producto.setMarca(valAct)
                if opcion == 8:
                    producto.setCantidad(valAct)
                if opcion == 9:
                    break
        else:
            print("No tienes los permisos para hacer este proceso...")


    def Añadir_producto(self, contraseña = None):
        if contraseña != None:
            producto = None
            opc=str(input('Ingrese el tipo de producto que añadirá\n1. Bebida\n2.Botana\n3.Galletas\n4.Cancelar accion'))
            while True:
                if opc=='1':
                    producto = self.InstanciarProductos('Bebida')
                    self.AgregarProducto(producto)
                    break
                elif opc=='2':
                    producto = self.InstanciarProductos('Botana')
                    self.AgregarProducto(producto)
                    break
                elif opc=='3':
                    producto = self.InstanciarProductos('Galletas')
                    self.AgregarProducto(producto)
                    break
                elif opc=='4':
                    break
                else:
                    print('Instrucción no reconocida, intente de nuevo')
        else:
            print("\nNo tiene los permisos para realizar este proceso...")
            
        
        
        '''
        Esta funcion es diferente a AgregarProducto, la funcion de este metodo es añadir un objeto
        desde teclado, haciendo uso de la funcion 'InstanciarProducto' y creando el objeto dentro de
        la funcion. Al final de la funcion, se hace uso del mismo metodo de AñadirProducto para añadirlo
        a la maquina.
        
        '''
    def InstanciarProductos(tipo):
        nombre=str(input('Ingrrese el nombre del producto: '))
        precio=float(input(f'Costo de {nombre}: '))
        codigo=float(input(f'Codigo para identificar a {nombre}'))
        color=str(input(f'Color de {nombre}: '))
        contenido= str(input(f'Cantidad en ml que contiene {nombre}'))
        marca=str(input(f'Marca distribuidora de {nombre}: '))
        cantidad=int(input(f'Cantidad del producto {nombre} que se ingresará a la maquina: '))
        if tipo=='Bebida':
            producto=Sodas(nombre, precio, codigo, 'Bebida', color, contenido, marca, cantidad)
        elif tipo=='Botana':
            producto=Papas(nombre, precio, codigo, 'Botana', color, contenido, marca, cantidad)
        elif tipo =='Galletas':
            producto=Galletas(nombre, precio, codigo, 'Galletas', color, contenido, marca, cantidad)
        return producto

    
class User:
    """
    En esta clase define el atributo nombre del usuario
    utliza el nombre de un usuario

    crea un objeto user
    """

    def __init__(self, nombre, dinero):
        self.nombre=nombre
        self.dinero = dinero
        self.productos = []
        self.contraseña = None
        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre del usuario

        Return:
        no retorna nada
        """
    def Comprar(self, MaquinaExp):
        
        MaquinaExp.SeleccionarProducto()
        while 1:
            try:
                Codigo_prod = str(input("Introduzca el codigo del producto: "))
                if Codigo_prod not in Maquina.productos.keys():
                    raise CodigoNoReconocido()
                else:
                    break
            except CodigoNoReconocido as err:
                print('El código que ingreso no coincide con ninguno de los mostrados\tPor favor intente de nuevo')

        producto = MaquinaExp.EntregarProducto(Codigo_prod)
        while 1:
            try:
                dineroIntr = float(input("Introduzca el dinero a pagar: "))
                break
            except ValueError:
                print('Dinero no reconocido')
                sa=str(input('¿Desea salir de la operación?\n1.Sí\t2.Presione cualquier otra tecla\n : '))
                if sa=='1':
                    exit()
                else:
                    print('Vuelva a ingresar su dinero')


        if dineroIntr >= producto.precio:
            BarraProgreso()
            self.dinero = self.dinero-dineroIntr
            cambio = dineroIntr-producto.precio
            print(f"Cambio: {cambio}")
            self.dinero = self.dinero + cambio
            self.productos.append(producto.nombre)
            return MaquinaExp.EntregarProducto(Codigo_prod)   
        else:
            print("Dinero Insuficiente")
            
        """
        Esta funcion...

        Arg:
        Maquina expendedora

        Return:
        retorna producto como el codigo del producto que se entrego
        """

    def Informacion(self):
        print(f'\tNombre: {self.nombre}\n\tSaldo Actual: {self.dinero}\n\tProductos: {self.productos}')
        '''
        Esta informacion mostrará los atributos actuales del usuario. El metodo será ejecutado en todo
        momento para conocer la informacion con la que se cuenta
        
        Return:
        No retorna nada
        '''

class UsuarioBase(User):

    """
    Esta clase hereda el atributo de la clase padre (user)

    utiliza el nombre del ususario

    crea un objeto usuarioBase
    """

    def __init__(self):
        User.__init__(self,'Usuario', 300)
    def SeleccionarProducto(self):
        pass
    
class UsuarioPremium_Dueño(User):

    """
    Esta clase define los atributos y metodos de un usuario premium, el dueño de la maquina

    utliza el nombre, contraseña, edad y compañia del usuario premium

    crea un objeto dueño
    """

    def __init__ (self, nombre, contraseña, edad, compañia):
        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre, contraseña, edad, compañia

        Return:
        no retorna nada
        """
        super().__init__(nombre, 2000)
        self.contraseña=contraseña
        self.edad=edad
        self.compañia=compañia

class Producto:

    """
    Esta clase define atributos y metodos de los productos
    """

    def __init__(self, nombre, precio, codigo, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.cantidad = cantidad
        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre, precio, codigo, cantidad de los productos 

        Return:
        no retorna nada
        """
        
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def setCodigo(self, codigo):
        self.codigo = codigo
    
    def setTipo(self, tipo):
        self.tipo = tipo
    
    def setColor(self, color):
        self.color = color
    
    def setContenido(self, contenido):
        self.contenido = contenido
        
    def setMarca(self, marca):
        self.marca = marca

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

class Sodas(Producto):

    """
    Esta clase define los atributos y metodo de los productos de tipo soda

    utliza nombre, precio,codigo, tipo, color, contenido, marca, cantidad

    crea un objeto sodas
    """

    def __init__(self, nombre, precio, codigo, tipo, color, contenido, marca, cantidad):

        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre, precio, codigo, tipo, color, contenido, marca, cantidad del producto

        Return:
        no retorna nada
        """

        super().__init__(nombre, precio, codigo, cantidad)
        self.contenido = contenido
        self.marca = marca
        self.tipo = tipo
        self.color=color

class Papas(Producto):

    """
    Esta clase define los atributos y metodo de productos tipo papas

    utliza nombre, precio, codigo, tipo, color, contenido, marca, cantidad

    crea objeto papas
    """

    def __init__(self, nombre, precio, codigo, tipo, color, contenido, marca, cantidad):

        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre, precio, codigo, tipo, color, contenido, marca, cantidad del producto

        Return:
        no retorna nada
        """

        super().__init__(nombre, precio, codigo, cantidad)
        self.contenido = contenido
        self.marca = marca
        self.tipo = tipo
        self.color=color

        


class Galletas(Producto):

    """
    Esta clase define los atributos y metodo de productos tipo galletas

    utliza nombre, precio, codigo, tipo, color, contenido, marca, cantidad

    crea objeto galleta
    """

    def __init__(self, nombre, precio, codigo, tipo, color, contenido, marca, cantidad):

        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre, precio, codigo, tipo, color, contenido, marca, cantidad del producto

        Return:
        no retorna nada
        """

        super().__init__(nombre, precio, codigo, cantidad)
        self.contenido = contenido
        self.marca = marca
        self.tipo = tipo
        self.color=color

def BarraProgreso():
    cadena = '-' * 50
    caracter = '#'
    b = 0
    
    for i in range(100):
        if(i%2==0):
            x = list(cadena)
            x[b] = caracter
            cadena = "".join(x)
            
        print(f'[{cadena}]{i+1}%', end='\r')
        time.sleep(0.03)
    print('\n')
    print('Entrega Lista')
    
    '''
    Esta funcion simula una barra de progreso, se usará en la entrega de productos
    
    Return:
    No retorna nada
    '''

    
def CrearUsuario():
    nombre=str(input('Ingresee su nombre:'))
    while 1 :
        contraseña=str(input('Contraseña: '))
        contraseña1=str(input('Repita su contraseña: '))
        if contraseña==contraseña1:
            break
        print('Las contraseñas no coinciden, intente de nuevo')
    edad = int(input('Ingrese su edad: '))
    compañia=str(input('Compañía para la que trabaja: '))
    Usuario = UsuarioPremium_Dueño(nombre, contraseña, edad, compañia)
    return Usuario        

class CodigoNoReconocido(Exception):
    def __init__(self):
        pass
    def mensaje(self):
        print('ERROR CODIGO NO EXISTETE <<<<<<<<')

if __name__=="__main__":
    
    diccionarioProductos = dict()
    Maquina = MaquinaExpendedora(diccionarioProductos, 8000)
        
    #Instanciar Productos
    
    Pepsi = Sodas("Pepsi", 15.50, "0110", "Bebida", "Negro", "300ml", "PespiCola", 15)
    Coca = Sodas('Cocacola', 18.00, '0111', 'Bebida', 'Negro', '600ml', 'Cocacola', 25)
    fanta = Sodas('Fanta', 16.00, '0112', 'Bebida', 'Naranja', '500ml', 'Fanta', 18)
    Seven = Sodas('Seven up', 16.5, '0115', 'Bebidas', 'verde', '500ml', 'Seven up', 15)
    peñaFiel = Sodas('Peñafiel', 15.00, '0117', 'Bebidas', 'transparente', '600ml', 'Peñafiel', 10)
    Takis = Papas("Takis Fuego", 15.00, "0210", "Botana", "Morado", "250g", "Barcel", 20)
    Chips = Papas('Chips Fuego', 17.00, '0211', 'Botana', 'Morado', '30g', 'Barcel', 14)
    cheetos = Papas('Cheetos', 12.00, '0212', 'Botana', 'Naranja', '30g', 'Cheetos', 13) 
    runners = Papas('Runners', 15.00, '0215', 'Botana', 'Rojo', '28g', 'Barcel', 7)
    Doritos = Papas('Doritos Nacho', 16.00, '0217', 'Botana', 'Naranja', '32g', 'Barcel', 15)
    Emperador = Galletas("Emperador", 17.00, "0310", "Galletas", "Rojo", "300g", "Gamesa", 10)
    Principe = Galletas('Principe', 18.00, '0311', 'Galletas', 'Azul', '200g', 'Marinela', 6)
    Arcoiris = Galletas('Arcoiris', 15.00, '0312', 'Galletas', 'Blanco', '250g', 'Gamesa', 4)
    Maria = Galletas('Maria', 14.00, '0315', 'Galletas', 'Naranja', '225g', 'Gamesa', 6)
    Deliciosas = Galletas('Deliciosas', 16.50, '0317', 'Galletas', 'Rosa', '200g', 'Gamesa', 5)


    #Agregar Productos
    Maquina.AgregarProducto(Pepsi)
    Maquina.AgregarProducto(Coca)
    Maquina.AgregarProducto(fanta)
    Maquina.AgregarProducto(Seven)
    Maquina.AgregarProducto(peñaFiel)
    Maquina.AgregarProducto(Takis)
    Maquina.AgregarProducto(Chips)
    Maquina.AgregarProducto(cheetos)
    Maquina.AgregarProducto(runners)
    Maquina.AgregarProducto(Doritos)
    Maquina.AgregarProducto(Emperador)
    Maquina.AgregarProducto(Principe)
    Maquina.AgregarProducto(Arcoiris)
    Maquina.AgregarProducto(Maria)
    Maquina.AgregarProducto(Deliciosas)

    Usuario = UsuarioBase()
    while(True):   
        Maquina.EscribirRecibo()
        while 1:
            try:
                opcion = int(input(Maquina.Menu()))
                break
            except ValueError:
                print('Opcion no reconocida\nIntente de nuevo')
        if opcion == 1:
            Usuario = CrearUsuario()
            print("Usuario Creado")
        if opcion == 2:
            Maquina.ActualizarValores(Usuario.contraseña)
        if opcion == 3:
            Usuario.Informacion()
            Usuario.Comprar(Maquina)
        if opcion == 4:
            Usuario.Informacion()
            Maquina.Añadir_producto(Usuario.contraseña)
        if opcion == 5:
            exit()


