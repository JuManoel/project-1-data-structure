from ..repository.repository import *
from ..tree.producto import Producto
from ..tree.tienda import TiendaAVL
# aca va recibir los datos del controller y convertir, lo que sea nescesario
# para que el repository pueda funcionar sin problemas
class Service():
    """
        La classe Service sirve para hacer la coneccion entre el repositorio
        e el controller.
        Eso ayuda a encapsular el codigo, lo que permite que sea mas legible y
        actualizable, ya que si adionamos una nueva funcion en repository o controller
        todo que tenemos que hacer es solo adicionar una nueva en essa clase
    """
    def __init__(self, path = "./productos.csv"):
        self.path = path
        try:
            self.dataFrame = read_csv(self.path)
        except Exception as e:
            try:
                self.dataFrame = create_DataFrame(self.path)
            except Exception as e:
                print(f"Error al leer/crear el CSV: {e}")
        self.tree,self.estados = self.getTree()

    def insertarProducto(self, product):
        producto = Producto()
        producto.initDict(product)
        self.dataFrame = add_row(producto,self.dataFrame)
        save_DataFrame(self.dataFrame, self.path)
        self.estados = self.tree.insertar(producto)
        return self.tree, self.estados

    def cambiarProducto(self, id, product):
        newProduct = Producto()
        newProduct.initDict(product)
        newProduct.id = id
        self.tree.cambiarProducto(id,newProduct)
        self.dataFrame = update_row(id, self.dataFrame, newProduct)
        save_DataFrame(self.dataFrame, self.path)
        return self.tree, [self.tree]
    
    def eliminarProducto(self, id):
        self.dataFrame = remove_row(id, self.dataFrame)
        save_DataFrame(self.dataFrame, self.path)
        self.tree, self.estados = self.getTree()
        return self.tree, self.estados
    
    def buscarProducto(self,nombre = "", precioMin = 0, precioMax = (2.0)**32-1, categoria = ""):
        return self.tree.buscarProducto(nombre,precioMin,precioMax,categoria)
         
    def buscarProductoId(self, id):
        return self.tree.buscarProductoId(id)

    def getTree(self):
        return self._toTree()
    
    def _toTree(self):
        tree = TiendaAVL()
        estados = []
        for index, row in self.dataFrame.iterrows():
            # Convertir cada fila a un objeto producto
            producto = Producto(row['id'],row['nombre'], row['precio'], row['stock'], row['categoria'])
            estados = tree.insertar(producto)
        return tree, estados