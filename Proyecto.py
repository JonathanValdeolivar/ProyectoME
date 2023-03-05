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
        
    #Usar diccionario para relacionar codigos y productos.

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
            producto.cantidad = -1
            return self.productos.get(Codigo_llave)
        else:
            print("El producto se encuentra agotado :C")

    def SeleccionarProducto(self)->None:
        print("Seleccione la opcion a realizar: ")
        
        opcion = input("1. Enlistar todos los productos\n2.Enlistar Productos por tipo:")
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
            lp.append(f'{a.codigo} : {a.nombre}\t${a.precio}')
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
        tipo = str(input("Introduzca el tipo de productos que desea mostrar: "))
        if tipo.lower() == "bebida" or tipo.lower() == "botana" or tipo.lower() == "galletas":        
            lp=[] 
            for a in self.productos.values():
                if a.tipo =='Bebida':
                    lp.append(f'{a.codigo} : {a.nombre}\t${a.precio}')
            print(lp)
            for a in self.productos.values():
                if a.tipo=='Botana':
                    lp.append(f'{a.codigo} : {a.nombre}\t${a.precio}')
            print(lp)
            for a in self.productos.values():
                if a.tipo=='Galletas':
                    lp.append(f'{a.codigo} : {a.nombre}\t${a.precio}')
            print(lp)
        else:
            print("Introduzca el tipo correcto: ")
            
    def AgregarProducto(self, Producto):

        """
        Esta funcion va a agragar productos a la lista de productos disponibles de la maquina

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

class User:
    """
    En esta clase define el atributo nombre del usuario
    utliza el nombre de un usuario

    crea un objeto user
    """

    def __init__(self, nombre, dinero):
        self.nombre=nombre
        self.dinero = dinero
        self.productos = None
        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre del usuario

        Return:
        no retorna nada
        """

    def Comprar(self, MaquinaExp):
        
        MaquinaExp.SeleccionarProducto()
        Codigo_prod = input("Introduzca el codigo del producto: ")
        producto = MaquinaExp.EntregaProductos(Codigo_prod)
        
        dineroIntr = input("Introduzca el dinero a pagar: ")
        if (dineroIntr - producto.precio) > 0:
            BarraProgreso()
            self.dinero = self.dinero-dineroIntr
            cambio = self.dinero+(dineroIntr-producto.precio)
            print(f"Cambio: {cambio}")
            self.dinero = self.dinero + cambio
            self.productos.append(producto.nombre)
            return MaquinaExp.EntregaProducto(Codigo_prod)   
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
    
    def AgregarProducto(self, producto, maquina):

        """
        Esta funcion agraga productos a la lista 

        Arg:
        producto, maquina

        Return:
        no retorna nada
        """

        llave = producto.codigo
        maquina.productos[llave] = producto

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
        
if __name__=="__main__":
    diccionarioProductos = dict()
    Maquina = MaquinaExpendedora(diccionarioProductos, 8000)
    Dueño = UsuarioPremium_Dueño("Juan Perez", "54321", "41", "Juan Expendio")

    #Instanciar Productos
    Pepsi = Sodas("Pepsi", "15.50", "0110", "Bebida", "Negro", "300ml", "PespiCola", 15)
    Takis = Papas("Takis Fuego", "15.00", "0210", "Botana", "Morado", "250g", "Barcel", 20)
    Emperador = Galletas("Emperador", "17.00", "0310", "Galletas", "Rojo", "300g", "Gamesa", 10)

    #Agregar Productos
    Dueño.AgregarProducto(Pepsi, Maquina)
    Dueño.AgregarProducto(Takis, Maquina)
    Dueño.AgregarProducto(Emperador, Maquina)


    Maquina.EscribirRecibo()
    Maquina.EnlistarProducto()
    BarraProgreso()
    
    
# 1. Entregar producto.
# 2. Seleccionar producto.
# 3. Almacenar nuevo producto.   -
# 4. Enlistar total de productos de un tipo.
# 5. Enlistar todos los productos.
# 6. Mostrar costos.
# 7. Regresar cambio.
# 8. Manejo de efectivo (mostrar total, alertar por falta de efectivo, etc.)