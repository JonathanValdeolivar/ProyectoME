import csv
class MaquinaExpendedora:
    def __init__(self, productos: dict, dinero: float) -> None:
        self.productos = productos
        self.dinero = dinero

    #Usar diccionario para relacionar codigos y productos.
    def EntregarProducto(Codigo_llave: int, Dic_Productos: dict)-> str:
        return Dic_Productos.get(Codigo_llave)

    def SeleccionarProducto()->None:
        print("Aqui se imprime la lista de valores del diccionario")
    def EnlistarProducto()->None:
            pass
    
    def AgregarProducto(self, Producto):
        self.productos[Producto.codigo] = Producto
        

    def EscribirRecibo(self):
        with open('datos.csv', 'w') as archivo_csv:
            #escritor = csv.writer(archivo_csv)
            claves = self.productos.keys()
            for productos in self.productos.values():
                #archivo_csv.write(claves[i])
                archivo_csv.write(productos+" ")
                i+=1
                
                

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
        self.contenido = contenido
        self.marca = marca
        self.tipo = tipo


        # self.tipo=tipo
        self.color=color
        # self.contenido=contenido
        # self.marca=marca


class Sodas(Producto):
    def __init__(self, nombre, precio, codigo):
        super().__init__(self, nombre, precio, codigo, 'Refresco')

class Papas(Producto):
    def __init__(self):
        Producto.__init__(self, self.nombre, self.precio, self.codigo, 'Papas', self.color, self.contenido, self.marca)

class Galletas(Producto):
    def __init__(self):
        Producto.__init__(self, self.nombre, self.precio, self.codigo, 'Galletas', self.color, self.contenido, self.marca)


#coca=Sodas( 30, 111, 'negro', '1 litro', 'coca' ,'')
#print(coca.agregar_producto())

diccionarioProductos = dict()
Maquina = MaquinaExpendedora(diccionarioProductos, 8000)
Pepsi = Sodas("Pepsi", "15.50", "0110", "Bebida", "Negro", "300ml", "PespiCola")




Maquina.AgregarProducto()



print(Maquina.productos)
Maquina.EscribirRecibo()



    
    
    
    

# 1. Entregar producto.
# 2. Seleccionar producto.
# 3. Almacenar nuevo producto.
# 4. Enlistar total de productos de un tipo.
# 5. Enlistar todos los productos.
# 6. Mostrar costos.
# 7. Regresar cambio.
# 8. Manejo de efectivo (mostrar total, alertar por falta de efectivo, etc.)