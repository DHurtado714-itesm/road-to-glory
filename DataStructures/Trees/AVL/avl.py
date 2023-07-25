class NodoAVL:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None
        self.altura = 1  # Altura del nodo

class AVL:
    def insertar(self, raiz, dato):
        # Primero, realiza la inserción normal de BST
        if not raiz:
            return NodoAVL(dato)
        elif dato < raiz.dato:
            raiz.izquierdo = self.insertar(raiz.izquierdo, dato)
        else:
            raiz.derecho = self.insertar(raiz.derecho, dato)

        # Actualiza la altura del nodo padre
        raiz.altura = 1 + max(self.obtenerAltura(raiz.izquierdo), self.obtenerAltura(raiz.derecho))

        # Obtén el factor de equilibrio
        balance = self.obtenerBalance(raiz)

        # Si el nodo está desequilibrado, entonces intenta 4 casos
        # Caso 1 - Rotación simple a la derecha
        if balance > 1 and dato < raiz.izquierdo.dato:
            return self.rotarDerecha(raiz)

        # Caso 2 - Rotación simple a la izquierda
        if balance < -1 and dato > raiz.derecho.dato:
            return self.rotarIzquierda(raiz)

        # Caso 3 - Rotación doble izquierda-derecha
        if balance > 1 and dato > raiz.izquierdo.dato:
            raiz.izquierdo = self.rotarIzquierda(raiz.izquierdo)
            return self.rotarDerecha(raiz)

        # Caso 4 - Rotación doble derecha-izquierda
        if balance < -1 and dato < raiz.derecho.dato:
            raiz.derecho = self.rotarDerecha(raiz.derecho)
            return self.rotarIzquierda(raiz)

        return raiz

    def obtenerAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    def obtenerBalance(self, raiz):
        if not raiz:
            return 0
        return self.obtenerAltura(raiz.izquierdo) - self.obtenerAltura(raiz.derecho)

    def rotarDerecha(self, z):
        y = z.izquierdo
        T3 = y.derecho
        y.derecho = z
        z.izquierdo = T3
        z.altura = 1 + max(self.obtenerAltura(z.izquierdo), self.obtenerAltura(z.derecho))
        y.altura = 1 + max(self.obtenerAltura(y.izquierdo), self.obtenerAltura(y.derecho))
        return y  # nueva raíz

    def rotarIzquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo
        y.izquierdo = z
        z.derecho = T2
        z.altura = 1 + max(self.obtenerAltura(z.izquierdo), self.obtenerAltura(z.derecho))
        y.altura = 1 + max(self.obtenerAltura(y.izquierdo), self.obtenerAltura(y.derecho))
        return y  # nueva raíz
