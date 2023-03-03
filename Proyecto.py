class MaquinaExpendedora:
    def __init__(self, productos: dict, dinero: float) -> None:
        self.productos = productos
        self.dinero = dinero
    
    #Usar diccionario para relacionar codigos y productos.
    def EntregarProducto(Codigo_llave: int, Dic_Productos: dict)-> str:
        return Dic_Productos.get(Codigo_llave)
        
    def EnlistarProducto()->None:
            pass
    
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
        User.__init__(self, self.nombre)
        self.usuario=usuario
        self.contraseña=contraseña
        self.edad=edad
        self.compañia=compañia

class Producto:
    def __init__(self, nombre, precio, codigo, tipo, color, contenido, marca ):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.tipo=tipo
        self.color=color
        self.contenido=contenido
        self.marca=marca
    def agregar_producto(Self):
        print('hola')
        # opc=str(input('Seleccione el tipo de producto que desea ingresar \n1. Refresco\n2. Fritura\n3. Galletas'))
        # if opc == '1':
        #     coca=Sodas()
        #     pass

class Sodas(Producto):
    def __init__(self, nombre, precio, codigo, tipo='color', color, contenido, marca):
        super().__init__(self, nombre, precio, codigo, 'Refresco', self.color, self.contenido, self.marca)

class Papas(Producto):
    def __init__(self):
        Producto.__init__(self, self.nombre, self.precio, self.codigo, 'Papas', self.color, self.contenido, self.marca)

class Galletas(Producto):
    def __init__(self):
        Producto.__init__(self, self.nombre, self.precio, self.codigo, 'Galletas', self.color, self.contenido, self.marca)
    
def IniciarProductos():
    dic = {110: 'CocaCola', 111:'Pepsi', 210: 'Donas'}#Seguir agregando productos al diccionario

coca=Sodas( 30, 111, 'negro', '1 litro', 'coca' ,'')
print(coca.agregar_producto())

       

# 1. Entregar producto.
# 2. Seleccionar producto.
# 3. Almacenar nuevo producto.
# 4. Enlistar total de productos de un tipo.
# 5. Enlistar todos los productos.
# 6. Mostrar costos.
# 7. Regresar cambio.
# 8. Manejo de efectivo (mostrar total, alertar por falta de efectivo, etc.)