dic = {110: 'CocaCola', 111:'Pepsi', 120: 'Red cola', 121: 'Monster',
        130: 'Fanta', 131: 'Sprite', 140: 'Peñafiel', 141: 'Jarrito',
        210: 'Takis', 211: 'Doritos', 220: 'Cheetos', 221: 'Chips', 
        230: 'Sabritas', 231: 'Ruffles', 240: 'Runners', 241: 'Toreadas',
        511: 'Chokis', 610: 'Emperador', 611:'Principe', 620: 'Marias',
        621: 'Deliciosas', 630: 'Arcoiris', 631: 'Quaker'}


dicGa = {511: 'Chokis', 610: 'Emperador', 611:'Principe', 620: 'Marias',
        621: 'Deliciosas', 630: 'Arcoiris', 631: 'Quaker'}

dicPapas = {210: 'Takis', 211: 'Doritos', 220: 'Cheetos', 221: 'Chips', 
        230: 'Sabritas', 231: 'Ruffles', 240: 'Runners', 241: 'Toreadas'}

dicSodas = {110: 'CocaCola', 111:'Pepsi', 120: 'Red cola', 121: 'Monster',
        130: 'Fanta', 131: 'Sprite', 140: 'Peñafiel', 141: 'Jarrito'}

class MaquinaExpendedora:
    def __init__(self, productos: dict, dinero: float) -> None:
        self.productos = productos
        self.dinero = dinero
    
    #Usar diccionario para relacionar codigos y productos.
    def EntregarProducto(Codigo_llave: int, Dic_Productos: dict)-> str:
        return Dic_Productos.get(Codigo_llave)
        
    def EnlistarProducto():
        print('\n-----Productos totales-----\n')
        print(dic)
        print('\n-----Galletas Disponibles----\n')
        print(dicGa)
        print('\n-----Papas Disponibles-----\n')
        print(dicPapas)
        print('\n-----Sodas Disponibles-----\n')
        print(dicSodas)

    
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
    pass

class Papas(Producto):
   pass
class Galletas(Producto):
    pass
    

def main():

    print('\n-----Bienvenido a TuMaquinaExpendedora-----\n')
    nombre = str(input('Dinos tu nombre: '))

    print('Bienvenido' + nombre + 'Seleccione la opcion que desee...\n'
          + '1. Comprar' + '2. Salir')
    opc = int(input('Opcion: '))
    

    MaquinaExpendedora.EnlistarProducto()



    
    
    
    

# 1. Entregar producto.
# 2. Seleccionar producto.
# 3. Almacenar nuevo producto.
# 4. Enlistar total de productos de un tipo.
# 5. Enlistar todos los productos.
# 6. Mostrar costos.
# 7. Regresar cambio.
# 8. Manejo de efectivo (mostrar total, alertar por falta de efectivo, etc.)