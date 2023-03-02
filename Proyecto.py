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
    def __init__(self, nombre, precio, codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
class Sodas(Producto):
    pass

class Papas(Producto):
    pass

class Galletas(Producto):
    pass
    
def IniciarProductos():
    dic = {110: 'CocaCola', 111:'Pepsi', 210: 'Donas'}#Seguir agregando productos al diccionario


    

# 1. Entregar producto.
# 2. Seleccionar producto.
# 3. Almacenar nuevo producto.
# 4. Enlistar total de productos de un tipo.
# 5. Enlistar todos los productos.
# 6. Mostrar costos.
# 7. Regresar cambio.
# 8. Manejo de efectivo (mostrar total, alertar por falta de efectivo, etc.)