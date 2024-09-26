import pandas as pd

"""
    Repository esta mas cerca de la base de datos que los demas archivos .py
    ella es responsable de hacer el CRUD (Create, Read, Update, Delete)
    La base de datos sera un CSV (comma separated values), por ser mas facil
"""


def read_csv(filename):
    """
        param: filename: str
        Lee un archivo CSV (filename) y lo convierte en un DataFrame de pandas.
    """
    dataFrame = pd.read_csv(filename)
    return dataFrame

def add_row(producto, dataFrame):
    """
        param: producto: Producto
        param: dataFrame: DataFrame
        Agrega una columna con la información del producto al DataFrame.
    """
    lastId = dataFrame['id'].max()
    producto.id = lastId + 1
    dataFrame.add(producto.toNpArray())
    return dataFrame

def remove_row(id, dataFrame):
    """
        param: id: int32
        param: dataFrame: DataFrame
        Elimina la fila con el id dado del DataFrame.
    """
    dataFrame = dataFrame[dataFrame['id'] != id]
    return dataFrame

def update_row(id, dataFrame, newProduct):
    """
        param: id: int32
        param: dataFrame: DataFrame
        param: newProduct: Producto
        Actualiza la fila con el id dado del DataFrame con la información del nuevo producto
    """
    dataFrame.loc[dataFrame['id'] == id] = newProduct.toNpArray()
    return dataFrame

def save_DataFrame(dataFrame, filename):
    """
        param: dataFrame: DataFrame
        param: filename: str
        Guarda el DataFrame en un archivo CSV con el nombre dado.
    """
    dataFrame.to_csv(filename, index=False)
    return dataFrame

def create_DataFrame(filename):
    """
    param: filename: str
    Crea un DataFrame vacío con las columnas id, nombre, precio, stock y categoria.
     """
    columns = ['id','nombre','precio','stock','categoria']
    dataFrame = pd.DataFrame(columns = columns)
    return dataFrame

# Apartir de aca voy a crear las opciones de busqueda en la base de datos
# Aca todo va retornar o un Producto o una lista de Productos

# --Pendiente--