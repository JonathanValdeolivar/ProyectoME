import csv
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
        retorna el codigo llave del producto que esta en el diccionario
        """

        return self.productos.get(Codigo_llave)

    def SeleccionarProducto()->None:

        """
        Esta funcion sirve para seleccionar el producto que se desee

        Arg:
        no tiene 

        Return:
        no retorna nada
        """

        print("Aqui se imprime la lista de valores del diccionario")

    def EnlistarProducto()->None:
            
        """
        Esta funcion va a enlistar todos los productos disponibles en la maquina expendedora

        Arg:
        No tiene

        Return:
        no retorna nada
        """

        Pro=[]
        Pro=list(diccionarioProductos.keys())
        print(Pro)
        # print(Pro[0].values)
    
    def AgregarProducto(self, Producto):

        """
        Esta funcion va a agragar productos a la lista de productos disponibles de la maquina

        Arg:
        producto (diccionario)

        Return:
        no retorna nada
        """

        llave = Producto.codigo
        self.productos.setdefault(llave,Producto)
        
    def EscribirRecibo(self):

        """
        Esta funcion va a escribir el recibo de la compra del producto o productos

        Arg:
        No tienes

        Return:
        no retorna nada
        """

        with open('datos.csv', 'w') as archivo_csv:
            #escritor = csv.writer(archivo_csv)
            for producto in self.productos.values():
                archivo_csv.write(f'Nombre: {producto.nombre}\t\tCodigo: {producto.codigo}\t\tCantidad: {producto.cantidad}\n')            



class User:

    """
    En esta clase define el atributo nombre del usuario

    utliza el nombre de un usuario

    crea un objeto user
    """

    def __init__(self, nombre):

        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre del usuario

        Return:
        no retorna nada
        """

        self.nombre=nombre
    
    def SacarProducto(self, Codigo_prod, MaquinaExp):

        """
        Esta funcion saca producto de la maquina expendedora

        Arg:
        Codigo del producto, Maquina expendedora

        Return:
        retorna producto como el codigo del producto que se entrego
        """

        producto = MaquinaExp.EntregaProductos(Codigo_prod)
        return producto
    


class UsuarioBase(User):

    """
    Esta clase hereda el atributo de la clase padre (user)

    utiliza el nombre del ususario

    crea un objeto usuarioBase
    """

    def __init__(self):
        User.__init__(self,'Usuario')
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

        super().__init__(nombre)
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

        """
        Esta funcion constructor le da valores a los atributos

        Arg:
        nombre, precio, codigo, cantidad de los productos 

        Return:
        no retorna nada
        """

        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
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

    crea obketo papas
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
MaquinaExpendedora.EnlistarProducto()

# 1. Entregar producto.
# 2. Seleccionar producto.
# 3. Almacenar nuevo producto.   -
# 4. Enlistar total de productos de un tipo.
# 5. Enlistar todos los productos.
# 6. Mostrar costos.
# 7. Regresar cambio.
# 8. Manejo de efectivo (mostrar total, alertar por falta de efectivo, etc.)