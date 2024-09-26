from service.service import Service


# Cristian, usted solo va poder manusear a su gusto esa classe controller
# espero que me haya quedado claro (se q es impossible soy ~color cafe~, pero me entiendes)

class Controller():
    """
        Aca conecta lo que se ve, con lo que funciona, el front, vamos a intentar
        trabajar juntos en ese archivo, a medida que usted nescesita una nueva funcion, usted la
        crea y me hare cargo de crear todo lo nescesario en repository y service
        ok?
    """
    def __init__(self, path = "./"):
        self.service = Service(path)

    def insertarProducto(self, productoDict = {}):
        tree = self.service.insertarProducto(productoDict)
        return tree

    def modificarProducto(self, id, productoDict = {}):
        tree = self.service.cambiarProducto(id, productoDict)
        return tree

    def eliminarProducto(self, id):
        tree = self.service.eliminarProducto(id)
        return tree
    
    def getTree(self):
        return self.service.getTree()