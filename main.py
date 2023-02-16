import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import filedialog

class Nodo:     #Creando clase del Nodo
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:    #Creando clase de la lista enlazada
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):    #Metodo para agregar nodos al final de la lista
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
                
def cargar_archivo():
    try:
        raiz = Tk()
        archivo = filedialog.askopenfilename(initialdir="C:/")
        print(archivo)
        xml_datos = ET.fromstring(archivo)
        raiz.mainloop()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        pass


while True:   #Creando Menu de opciones
    print("Menú:")
    print("1. ")
    print("2. Seleccionar una Muestra")
    print("3. Crear o modificar una Muestra")
    print("4. Generar archivo XML")
    print("5. Cargar archivo XML")
    print("6. Salir")
    
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        print("Opción 1 seleccionada")
        # Aquí puedes colocar la lógica que deseas que se ejecute para la opción 1
    elif opcion == "2":
        print("Opción 2 seleccionada")
        # Aquí puedes colocar la lógica que deseas que se ejecute para la opción 2
    elif opcion == "3":
        print("opcion 3")
    elif opcion == "4":
        print("opcion 4")
    elif opcion == "5":
        print("Seleccione el archivo a cargar...")
        cargar_archivo()
    elif opcion == "6":
        print("Saliendo del menú...")
        break
    else:
        print("Opción no válida, por favor seleccione una opción válida.")


