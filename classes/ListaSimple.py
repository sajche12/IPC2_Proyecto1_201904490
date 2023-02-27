class Nodo:     #Creando clase del Nodo
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:    #Creando clase de la lista enlazada
    def __init__(self):
        self.cabeza = None

    def agregarCodigo(self, dato):    #Metodo para agregar el codigo del organismo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            
    def agregarNombre(self, dato):    #Metodo para agregar el nombre del organismo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            
    def agregarFila(self, dato):    #Metodo para agregar la fila del organismo vivo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            
    def agregarColumna(self, dato):    #Metodo para agregar la columna del organismo vivo al final de la lista
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir(self):     #Metodo para imprimir los nodos
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente