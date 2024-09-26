from repository.repository import *
from tree.producto import Producto
from tree.tienda import TiendaAVL
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
    def __init__(self, path = "./"):
        self.path = path
        try:
            self.dataFrame = read_csv(self.path)
        except Exception as e:
            try:
                self.dataFrame = create_DataFrame(self.path)
            except Exception as e:
                print(f"Error al leer/crear el CSV: {e}")

    def insertarProducto(self, product):
        producto = Producto(product)
        self.dataFrame = add_row(producto,self.dataFrame)
        save_DataFrame(self.dataFrame, self.path)
        return self.getTree()

    def cambiarProducto(self, id, product):
        newProduct = Producto(product)
        self.dataFrame = update_row(id, self.dataFrame, newProduct)
        save_DataFrame(self.dataFrame, self.path)
        self.getTree()
    
    def eliminarProducto(self, id):
        self.dataFrame = remove_row(id, self.dataFrame)
        save_DataFrame(self.dataFrame, self.path)
        self.getTree()
    
    def getTree(self):
        return self._toTree()
    
    def _toTree(self):
        tree = TiendaAVL()
        for index, row in self.dataFrame.iterrows():
            # Convertir cada fila a un objeto producto
            producto = Producto(row['id'],row['nombre'], row['precio'], row['stock'], row['categoria'])
            # Agregarlo al arbol
            tree.insertar(producto)
        return tree