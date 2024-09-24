from producto import Product
class TiendaAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, id, nombre, precio, stock, categoria):
        if self.raiz is None:
            self.raiz = Product(id, nombre, precio, stock, categoria)
        else:
            self.raiz = self._insertar(self.raiz, id, nombre, precio, stock, categoria)

    def _insertar(self, nodo, id, nombre, precio, stock, categoria):
        if not nodo:
            return Product(id, nombre, precio, stock, categoria)

        if id < nodo.id:
            nodo.izquierda = self._insertar(nodo.izquierda, id, nombre, precio, stock, categoria)
        elif id > nodo.id:
            nodo.derecha = self._insertar(nodo.derecha, id, nombre, precio, stock, categoria)
        else:
            return nodo  # Los valores duplicados no están permitidos

        # Actualizar la altura del nodo actual
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))

        # Obtener el factor de equilibrio para verificar si está balanceado
        balance = self.obtener_balance(nodo)

        # Rotaciones para balancear el árbol

        # Caso 1: Rotación a la derecha
        if balance > 1 and id < nodo.izquierda.id:
            return self.rotacion_derecha(nodo)

        # Caso 2: Rotación a la izquierda
        if balance < -1 and id > nodo.derecha.id:
            return self.rotacion_izquierda(nodo)

        # Caso 3: Rotación izquierda-derecha
        if balance > 1 and id > nodo.izquierda.id:
            nodo.izquierda = self.rotacion_izquierda(nodo.izquierda)
            return self.rotacion_derecha(nodo)

        # Caso 4: Rotación derecha-izquierda
        if balance < -1 and id < nodo.derecha.id:
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

    # Función para buscar un valor en el árbol
    # def buscar(self, valor):
    #     return self._buscar(self.raiz, valor)

    # def _buscar(self, nodo, valor):
    #     if nodo is None:
    #         return False
    #     if valor == nodo.valor:
    #         return True
    #     elif valor < nodo.valor:
    #         return self._buscar(nodo.izquierda, valor)
    #     else:
    #         return self._buscar(nodo.derecha, valor)

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