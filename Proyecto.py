import csv
import time
class MaquinaExpendedora:
    def __init__(self, productos: dict, dinero: float) -> None:
        self.productos = productos
        self.dinero = dinero
        
    #Usar diccionario para relacionar codigos y productos.
    def EntregarProducto(self, Codigo_llave: int):
        producto = self.productos[Codigo_llave]
        producto.cantidad = -1
        return self.productos.pop(Codigo_llave)
    

    def SeleccionarProducto()->None:
        print("Aqui se imprime la lista de valores del diccionario")
        
    def EnlistarProducto()->None:
            pass

    def EscribirRecibo(self):
        with open('datos.csv', 'w') as archivo_csv:
            for producto in self.productos.values():
                archivo_csv.write(f'Nombre: {producto.nombre}\t\tCodigo: {producto.codigo}\t\tCantidad: {producto.cantidad}\n')            
class User:
    def __init__(self, nombre, dinero):
        self.nombre=nombre
        self.dinero = dinero
        self.productos = None
    
    def SacarProducto(self, Codigo_prod, MaquinaExp):
        producto = MaquinaExp.productos[Codigo_prod]
        if (self.dinero - producto.precio) > 0:
            BarraProgreso()
            producto = MaquinaExp.EntregaProductos(Codigo_prod)
            self.dinero = self.dinero-producto.precio
            self.productos.append(producto.nombre)
            return producto    
        else:
            print("Dinero Insuficiente")
    
    def Informacion(self):
        print(f'\tNombre: {self.nombre}\n\tSaldo Actual: {self.dinero}\n\tProductos: {self.productos}')
        '''
        Esta informacion mostrará los atributos actuales del usuario. El metodo será ejecutado en todo
        momento para conocer la informacion con la que se cuenta
        
        Return:
        No retorna nada
        '''

class UsuarioBase(User):
    def __init__(self):
        User.__init__(self,'Usuario', 300)
    def SeleccionarProducto(self):
        pass
    
    
class UsuarioPremium_Dueño(User):
    def __init__ (self, nombre, contraseña, edad, compañia):
        super().__init__(nombre, 2000)
        self.contraseña=contraseña
        self.edad=edad
        self.compañia=compañia
    
    def AgregarProducto(self, producto, maquina):
        llave = producto.codigo
        maquina.productos[llave] = producto

class Producto:
    def __init__(self, nombre, precio, codigo, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.cantidad = cantidad

class Sodas(Producto):
    def __init__(self, nombre, precio, codigo, tipo, color, contenido, marca, cantidad):
        super().__init__(nombre, precio, codigo, cantidad)
        self.contenido = contenido
        self.marca = marca
        self.tipo = tipo
        self.color=color

class Papas(Producto):
    def __init__(self, nombre, precio, codigo, tipo, color, contenido, marca, cantidad):
        super().__init__(nombre, precio, codigo, cantidad)
        self.contenido = contenido
        self.marca = marca
        self.tipo = tipo
        self.color=color

class Galletas(Producto):
    def __init__(self, nombre, precio, codigo, tipo, color, contenido, marca, cantidad):
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
    BarraProgreso()
# 1. Entregar producto.
# 2. Seleccionar producto.
# 3. Almacenar nuevo producto.   -
# 4. Enlistar total de productos de un tipo.
# 5. Enlistar todos los productos.
# 6. Mostrar costos.
# 7. Regresar cambio.
# 8. Manejo de efectivo (mostrar total, alertar por falta de efectivo, etc.)