from .ListaSimple import ListaEnlazada
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

lista = ListaEnlazada() 

def cargar_archivo(self):
    filename = askopenfilename()
    xml_archivo = ET.parse(filename)
    ruta = xml_archivo.getroot()
    for organismo in ruta.iter('organismo'):    #Agregando el codigo y nombre de los organismos a la lista
        lista.agregarCodigo(organismo.find('codigo').text)
        lista.agregarNombre(organismo.find('nombre').text)
    lista.imprimir()
        
class Menu:
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