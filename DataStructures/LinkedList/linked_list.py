# Creamos una clase para los nodos.
class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Aquí guardamos el dato.
        self.siguiente = None  # Este será el enlace al siguiente nodo, inicialmente es None.

# Creamos una clase para la lista enlazada.
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicialmente, la cabeza es None porque la lista está vacía.

    # Método para agregar un nuevo nodo al final de la lista.
    def agregar(self, dato):
        if not self.cabeza:  # Si la lista está vacía...
            self.cabeza = Nodo(dato)  # ... creamos un nuevo nodo y lo hacemos la cabeza de la lista.
        else:  # Si la lista no está vacía...
            nodo_actual = self.cabeza  # Comenzamos con la cabeza.
            while nodo_actual.siguiente:  # Mientras el nodo actual tenga un siguiente nodo...
                nodo_actual = nodo_actual.siguiente  # ... pasamos al siguiente nodo.
            nodo_actual.siguiente = Nodo(dato)  # Cuando ya no haya un siguiente nodo, agregamos el nuevo nodo.

    # Método para imprimir todos los elementos de la lista.
    def imprimir_lista(self):
        nodo_actual = self.cabeza  # Comenzamos con la cabeza.
        while nodo_actual:  # Mientras haya un nodo actual...
            print(nodo_actual.dato)  # ...imprimimos su dato.
            nodo_actual = nodo_actual.siguiente  # Y pasamos al siguiente nodo.

# Función para insertar un nuevo nodo en un índice específico.
    def insertar(self, indice, dato):
        if indice == 0:
            nuevo_nodo = Nodo(dato)
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            posicion_actual = 0
            while nodo_actual and posicion_actual < indice:
                if posicion_actual == indice - 1:
                    nuevo_nodo = Nodo(dato)
                    nuevo_nodo.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente = nuevo_nodo
                nodo_actual = nodo_actual.siguiente
                posicion_actual += 1

    # Función para eliminar un nodo por dato.
    def eliminar(self, dato):
        nodo_actual = self.cabeza
        anterior = None
        while nodo_actual and nodo_actual.dato != dato:
            anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        if anterior is None:
            self.cabeza = nodo_actual.siguiente
        elif nodo_actual:
            anterior.siguiente = nodo_actual.siguiente

    # Función para buscar un dato en la lista.
    def buscar(self, dato):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.dato == dato:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

mi_lista = ListaEnlazada()
mi_lista.agregar('A')
mi_lista.agregar('B')
mi_lista.agregar('C')
mi_lista.imprimir_lista()

# Output:
# A
# B
# C