from repository import *
from tree.producto import Product
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
    pass