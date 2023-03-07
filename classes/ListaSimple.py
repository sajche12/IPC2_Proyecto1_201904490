class Nodo:     #Creando clase del Nodo
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:    #Creando clase de la lista enlazada
    def __init__(self):
        self.cabeza = None

    def agregarNodo(self, dato):    #Metodo para agregar Nodos a la lista simple
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo