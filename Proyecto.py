import csv
class MaquinaExpendedora:
    def __init__(self, productos: dict, dinero: float) -> None:
        self.productos = productos
        self.dinero = dinero
        
    #Usar diccionario para relacionar codigos y productos.
    def EntregarProducto(self, Codigo_llave: int)-> str:
        return self.productos.get(Codigo_llave)

    def SeleccionarProducto()->None:
        print("Aqui se imprime la lista de valores del diccionario")

    def EnlistarProducto()->None:
            Pro=[]
            Pro=list(diccionarioProductos.values())
            print(Pro[0].nombre)
    
    def AgregarProducto(self, Producto):
        llave = Producto.codigo
        self.productos.setdefault(llave, Producto)
        
    def EscribirRecibo(self):
        with open('datos.csv', 'w') as archivo_csv:
            #escritor = csv.writer(archivo_csv)
            for producto in self.productos.values():
                archivo_csv.write(f'Nombre: {producto.nombre}\t\tCodigo: {producto.codigo}\t\tCantidad: {producto.cantidad}\n')            
class User:
    def __init__(self, nombre):
        self.nombre=nombre
    
    def SacarProducto(self, Codigo_prod, MaquinaExp):
        producto = MaquinaExp.EntregaProductos(Codigo_prod)
        return producto

class UsuarioBase(User):
    def __init__(self):
        User.__init__(self,'Usuario')
    def SeleccionarProducto(self):
        pass

class UsuarioPremium_Dueño(User):
    def __init__ (self, nombre, contraseña, edad, compañia):
        super().__init__(nombre)
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