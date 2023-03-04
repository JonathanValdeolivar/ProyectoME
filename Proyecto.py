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
            Pro=list(diccionarioProductos.keys())
            print(Pro)
            # print(Pro[0].values)
    
    def AgregarProducto(self, Producto):
        llave = Producto.codigo
        self.productos.setdefault(llave,Producto)
        
    def EscribirRecibo(self):
        with open('datos.csv', 'w') as archivo_csv:
            #escritor = csv.writer(archivo_csv)
            for producto in self.productos.values():
                archivo_csv.write(f'Nombre: {producto.nombre} Codigo: {producto.codigo} Cantidad: {producto.cantidad}')
            a = 0            
class User:
    def __init__(self, nombre):
        self.nombre=nombre

class Usuario(User):
    def __init__(self):
        User.__init__(self,'Usuario')
    def SeleccionarProducto(self):
        pass
class UsuarioPremium(User):
    def __init__ (self,  usuario, contraseña, edad, compañia):
        super().__init__(self, self.nombre)
        self.usuario=usuario
        self.contraseña=contraseña
        self.edad=edad
        self.compañia=compañia

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
Pepsi = Sodas("Pepsi", "15.50", "0110", "Bebida", "Negro", "300ml", "PespiCola",15)
Pepsi = Sodas("Pepsi", "15.50", "0110", "Bebida", "Negro", "300ml", "PespiCola",15)
Maquina.AgregarProducto(Pepsi)


#Maquina.AgregarProducto()

# coca=Sodas( 30, 111, 'negro', '1 litro', 'coca' ,'')
# print(coca.agregar_producto())

#print(Maquina.productos)
# print(diccionarioProductos)
Maquina.EscribirRecibo()
MaquinaExpendedora.EnlistarProducto()

# 1. Entregar producto.
# 2. Seleccionar producto.
# 3. Almacenar nuevo producto.
# 4. Enlistar total de productos de un tipo.
# 5. Enlistar todos los productos.
# 6. Mostrar costos.
# 7. Regresar cambio.
# 8. Manejo de efectivo (mostrar total, alertar por falta de efectivo, etc.)