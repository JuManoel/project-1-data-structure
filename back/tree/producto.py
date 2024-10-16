from numpy import float32, uint32
from numpy import array
class Producto():
    """
This class represents a product with attributes such as name, price, stock, and category.

Attributes:
-----------
nombre : str
    The name of the product.
precio : numpy.float32
    The price of the product.
stock : numpy.uint32
    The stock quantity of the product.
categoria : str
    The category of the product.
"""
        
    def __init__(self, id=0, nombre="", precio=0.0, cantidad=1, categoria=""):
        """
        Initializes a new instance of the Producto class.

        Parameters:
        -----------
        nombre : str
            The name of the product.
        precio : float
            The price of the product. It will be converted to numpy.float32.
        stock : int
            The stock quantity of the product. It will be converted to numpy.uint32.
        categoria : str
            The category of the product.

        Returns:
        --------
        None
        """
        self.id = uint32(id)
        self.nombre = str(nombre)
        self.precio = float32(precio)
        self.cantidad = uint32(cantidad)
        self.categoria = str(categoria)
        self.izquierda = None
        self.derecha = None
        self.altura = 1
    
    def initDict(self, dict):
        try:
            self.id = uint32(0)
            self.nombre = str(dict["nombre"])
            self.precio = float32(dict["precio"])
            self.cantidad = uint32(dict["cantidad"])
            self.categoria = str(dict["categoría"])
        except KeyError:
            try:
                self.__init__(**dict)
            except TypeError:
                raise ValueError("El diccionario no contiene todos los atributos necesarios")


    def __str__(self):
        return f"id: {self.id}, nombre: {self.nombre}, precio: {self.precio}, cantidad: {self.cantidad}, categoria: {self.categoria}"


    def toNpArray(self):
        return array([self.id, self.nombre, self.precio, self.cantidad, self.categoria])
    
    def toDict(self):
        return {'id': self.id, 'nombre': self.nombre, 'precio': self.precio,'cantidad': self.cantidad, 'categoria': self.categoria}
