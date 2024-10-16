from ..service.service import Service


# Cristian, usted solo va poder manusear a su gusto esa classe controller
# espero que me haya quedado claro (se q es impossible soy ~color cafe~, pero me entiendes)

class Controller():
    """
        Aca conecta lo que se ve, con lo que funciona, el front, vamos a intentar
        trabajar juntos en ese archivo, a medida que usted nescesita una nueva funcion, usted la
        crea y me hare cargo de crear todo lo nescesario en repository y service
        ok?
    """
    def __init__(self, path = "./productos.csv"):
        self.service = Service(path)

    def insertarProducto(self, productoDict = {}):
        return  self.service.insertarProducto(productoDict)
        
    def modificarProducto(self, id, productoDict = {}):
        return self.service.cambiarProducto(id, productoDict)
    def eliminarProducto(self, id):
        return  self.service.eliminarProducto(id)
    
    def buscarProducto(self, nombre = "", precioMin = 0, precioMax = (2.0)**32-1, categoria = ""):
        if(precioMin<0 or precioMax<=0):
            return self.service.tree()
        if(precioMax<precioMin):
            precioMin,precioMax = precioMax,precioMin
        return self.service.buscarProducto(nombre,precioMin,precioMax,categoria)
    def buscarProductoId(self, id = 0):
        if(id<0):
            return self.service.tree()
        return self.service.buscarProductoId(id)