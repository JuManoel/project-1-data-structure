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
        """
        param: path-> string donde se va guardar el archivo csv
        el metodo init inicializa el data frame que vamos 
        a utilizar para cargar y guardar la base de datos
        """
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
        """
        param: product-> dicionario que tendra todos los atributos basicos de 
        um producto, nombre, precio, cantidad y categoria
        retorna el arbol y los estados de rotacion del arbol
        """
        producto = Producto()
        producto.initDict(product)
        if(producto.cantidad <=0 or producto.precio <= 0):
            return self.getTree()
        self.dataFrame = add_row(producto,self.dataFrame)
        save_DataFrame(self.dataFrame, self.path)
        self.estados = self.tree.insertar(producto)
        return self.tree, self.estados
 
    def cambiarProducto(self, id, product):
        """
        param: id -> el indentifacador del producto que quermos modificar
        param: product -> dicionarios con los nuevos valores del producto
        que queremos modificar
        """
        newProduct = Producto()
        newProduct.initDict(product)
        newProduct.id = id
        #validaciones para producto
        if(newProduct.cantidad == 0):
            return self.eliminarProducto(id)
        elif(newProduct.precio <= 0 or newProduct.cantidad <=0):
            return self.getTree()
        self.tree.cambiarProducto(id,newProduct)
        self.dataFrame = update_row(id, self.dataFrame, newProduct)
        save_DataFrame(self.dataFrame, self.path)
        return self.tree, [self.tree]
    
    def eliminarProducto(self, id):
        """
        param: id -> indentificador del producto que queremos encontrar
        """
        self.dataFrame = remove_row(id, self.dataFrame)
        save_DataFrame(self.dataFrame, self.path)
        self.tree, self.estados = self.getTree()
        return self.tree, self.estados
    
    def buscarProducto(self,nombre = "", precioMin = 0, precioMax = (2.0)**32-1, categoria = ""):
        """
        busqueda avanzada de producto, recibe fragmentos del nombre
        precios minimo y maximo y fragmento de la categoria
        """
        return self.tree.buscarProducto(nombre,precioMin,precioMax,categoria)
         
    def buscarProductoId(self, id):
        """
        busca del producto por el Id
        """
        return self.tree.buscarProductoId(id)

    def getTree(self):
        #funcion que el usuario va utilizar para generar el arbol
        return self._toTree()
    
    def _toTree(self):
        """
        metodo auxiliar para generar un arbol dado la base de datos
        """
        tree = TiendaAVL()
        estados = []
        for index, row in self.dataFrame.iterrows():
            # Convertir cada fila a un objeto producto
            producto = Producto(row['id'],row['nombre'], row['precio'], row['stock'], row['categoria'])
            estados = tree.insertar(producto)
        return tree, estados