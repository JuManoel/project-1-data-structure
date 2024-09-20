from numpy import float32, uint32
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

Methods:
--------
__init__(self, nombre, precio, stock, categoria)
    Initializes a new instance of the Producto class.
"""
    def __init__(self, nombre, precio, stock, categoria):
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
        self.id = uint32(0)
        self.nombre = nombre
        self.precio = float32(precio)
        self.stock = uint32(stock)
        self.categoria = categoria
    def __init__(self, id, nombre, precio, stock, categoria):
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
        self.__init__(nombre, precio, stock, categoria)
        self.id = uint32(id)
