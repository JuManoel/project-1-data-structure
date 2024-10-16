from ..tree.producto import Producto
import copy
class TiendaAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, producto):
        if self.raiz is None:
            self.raiz = producto
            return [self.raiz]
        else:
            estados = [copy.deepcopy(self.raiz)]
            self.raiz = self._insertar(self.raiz, producto,estados)
            return estados

    def _insertar(self, nodo, producto, estados):
        if not nodo:
            return producto
        if producto.id < nodo.id:
            nodo.izquierda = self._insertar(nodo.izquierda, producto, estados)
        elif producto.id > nodo.id:
            nodo.derecha = self._insertar(nodo.derecha, producto, estados)
        else:
            return nodo  # Los valores duplicados no están permitidos
        estados.append(copy.deepcopy(self.raiz))
        # Actualizar la altura del nodo actual
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        # Obtener el factor de equilibrio para verificar si está balanceado
        balance = self.obtener_balance(nodo)

        # Rotaciones para balancear el árbol

        # Caso 1: Rotación a la derecha
        if balance > 1 and producto.id < nodo.izquierda.id:
            return self.rotacion_derecha(nodo)

        # Caso 2: Rotación a la izquierda
        
        if balance < -1 and producto.id > nodo.derecha.id:
            return self.rotacion_izquierda(nodo)

        # Caso 3: Rotación izquierda-derecha
        if balance > 1 and producto.id > nodo.izquierda.id:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        # Caso 4: Rotación derecha-izquierda
        if balance < -1 and producto.id < nodo.derecha.id:
            nodo.derecha = self.rotacion_derecha(nodo.derecha)
            return self.rotacion_izquierda(nodo)

        return nodo

    # Función para rotación a la izquierda
    def rotacion_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        # Realizar la rotación
        y.izquierda = z
        z.derecha = T2

        # Actualizar alturas
        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    # Función para rotación a la derecha
    def rotacion_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        # Realizar la rotación
        y.derecha = z
        z.izquierda = T3

        # Actualizar alturas
        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    # Obtener la altura de un nodo
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    # Obtener el balance (factor de equilibrio) de un nodo
    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    # Recorrido en inorden
    def recorrido_inorden(self):
        elementos = []
        self._recorrido_inorden(self.raiz, elementos)
        return elementos

    def _recorrido_inorden(self, nodo, elementos):
        if nodo is not None:
            self._recorrido_inorden(nodo.izquierda, elementos)
            elementos.append(nodo.id)
            self._recorrido_inorden(nodo.derecha, elementos)

    def buscarProducto(self, nombre = "", precioMin = 0, precioMax = (2.0)**32-1, categoria = ""):
        """
        arboleAux e nodoPadre sirve para no cambiar el arbole original
        la idea es solo va ocultar algunos nodos y no queremos modificar el arbol original
        """
        arboleAux = copy.deepcopy(self.raiz) 
        estados = []
        self._buscarProducto(arboleAux,arboleAux, nombre, precioMin, precioMax, categoria, estados)
        return arboleAux, estados

    def _buscarProducto(self,nodo,nodoPadre, nombre = "", precioMin = 0, precioMax = (2.0)**32-1, categoria = "", estados = []):
        if nodo is not None:
            nodo.show = nodo.nombre in nombre and (precioMax>=nodo.precio >= precioMin) and nodo.categoria in categoria
            self._buscarProducto(nodo.izquierda, nodoPadre,nombre, precioMin, precioMax, categoria)
            estados.append(copy.deepcopy(nodoPadre))
            self._buscarProducto(nodo.derecha, nodoPadre,nombre, precioMin, precioMax, categoria)
            estados.append(copy.deepcopy(nodoPadre))

    def buscarProductoId(self, id):
        arboleAux = copy.deepcopy(self.raiz)
        estados = [self.raiz]
        self._buscarProductoId(arboleAux,id,estados)
        return arboleAux, estados
    
    def _buscarProductoId(self, nodo,id,estados):
        if nodo is not None:
            nodo.show = nodo.id == id
            estados.append(copy.deepcopy(self.raiz))
            self._buscarProductoId(nodo.izquierda,id,estados)
            self._buscarProductoId(nodo.derecha,id,estados)
    def cambiarProducto(self,id, producto):
        pass
    def _cambiarProducto(self,nodo,id,producto):
        if nodo is not None:
            if id < nodo.id:
                self._cambiarProducto(nodo.izquierda, id, producto)
            elif id > nodo.id:
                nodo.derecha = self._insertar(nodo.derecha, id, producto)
            else:
                hijos = [nodo.izquierda, nodo.derecha]
                nodo = producto
                nodo.izquierda = hijos[0]
                nodo.derecha = hijos[1]