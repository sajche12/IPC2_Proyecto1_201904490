from os import system, startfile
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from .Organismo import Organismo
from .Muestra import Muestra
from .CeldaViva import CeldaViva

class Menu:
    muestraAnalizada:Muestra

    def cargarArchivo(self, xml_archivo):    #Metodo para cargar el archivo xml y guardarlo en las listas
    
        ruta = xml_archivo.getroot()
    
        codigoMuestra = ruta[1][0][0].text
        descripcionMuestra = ruta[1][0][1].text
        filasMuestra = ruta[1][0][2].text
        columnasMuestra = ruta[1][0][3].text
        
        for i in ruta.findall('listaOrganismos'):
            totalOrganismos = len(i)
           
        if int(filasMuestra) > 10000 and int(columnasMuestra) > 10000:
            print("\nLA MUESTRA SUPERA EL LIMITE DE FILAS Y COLUMNAS, PORFAVOR CARGA OTRA MUESTRA")
        elif totalOrganismos > 1000:
            print(f"\nLA MUESTRA SUPERA EL LIMITE DE ORGANISMOS, PORFAVOR CARGA OTRA MUESTRA")
        else:
            nuevaMuestra = Muestra(codigoMuestra, descripcionMuestra, filasMuestra, columnasMuestra)
    
            for organismo in ruta.iter('organismo'):    #Agregando el codigo y nombre de los organismos a la lista
                codigo = organismo.find('codigo').text
                nombre = organismo.find('nombre').text
                nuevoOrganismo = Organismo(codigo, nombre)
                nuevaMuestra.listaOrganismos.agregarNodo(nuevoOrganismo)
        
            for celdaViva in ruta.iter('celdaViva'):
                fila = celdaViva.find('fila').text
                columna = celdaViva.find('columna').text
                codigoOrganismo = celdaViva.find('codigoOrganismo').text
                organismoVivo = CeldaViva(codigoOrganismo, fila, columna)
                nuevaMuestra.listaCeldasVivas.agregarNodo(organismoVivo)
                self.muestraAnalizada = nuevaMuestra

    def graficarMuestra(self):
    
        x = self.muestraAnalizada.dimensionX
        y = self.muestraAnalizada.dimensionY

        codigoGraphiz = """
            digraph structs {
                """
        codigoGraphiz = codigoGraphiz + f'label = "{self.muestraAnalizada.descripcion} - Muestra de: {self.muestraAnalizada.dimensionX} filas y {self.muestraAnalizada.dimensionY} columnas"'
        codigoGraphiz = codigoGraphiz + """
                node [shape=record];
                MATRIZ [
                    label="
        """
        cuentaX = -1
        cuentaY = -1
        while (cuentaX <= int(x)):
            if(cuentaY == -1):
                codigoGraphiz=codigoGraphiz+'{x,y'
            else:
                codigoGraphiz=codigoGraphiz+'{'+str(cuentaX)
            
            cuentaY = 0
            
            while (cuentaY <= int(y)):
                
                if(cuentaX == -1):
                    codigoGraphiz=codigoGraphiz+'|'+str(cuentaY)
                else:
                    listaCeldasVivas  = self.muestraAnalizada.listaCeldasVivas
                    nodoActual = listaCeldasVivas.cabeza

                    codigoOrganismo = ""
                    while nodoActual != None:
                       
                        celdaViva:CeldaViva = nodoActual.dato
                        coordenadaX = celdaViva.x
                        coordenadaY = celdaViva.y
                        
                        if (int(cuentaX)==int(coordenadaX) and int(cuentaY) == int(coordenadaY)):
                            
                            inicio = self.muestraAnalizada.listaOrganismos.cabeza
                            while(inicio!=None):
                                organismo:Organismo = inicio.dato
                                
                                if(celdaViva.organismo==organismo.codigo):
                                    codigoOrganismo='|'+str(organismo.codigo)
                                    break
                                inicio=inicio.siguiente
                            break
                        else:
                            codigoOrganismo='|'
                        nodoActual = nodoActual.siguiente

                    codigoGraphiz = codigoGraphiz + codigoOrganismo
                cuentaY = cuentaY + 1
                
            cuentaX = cuentaX + 1
            
            if(cuentaX == int(x)):
                codigoGraphiz=codigoGraphiz+'}|'
            else:
                codigoGraphiz=codigoGraphiz+'}|'

        codigoGraphiz =codigoGraphiz+ """
                        "];
        """
        inicio = self.muestraAnalizada.listaOrganismos.cabeza
        codigoGraphiz =codigoGraphiz+"\""
        while(inicio!=None):
            organismo:Organismo = inicio.dato
            codigoGraphiz =codigoGraphiz +str(organismo.codigo)+"\n"
            inicio=inicio.siguiente
        codigoGraphiz =codigoGraphiz+ """
                    \"}     
        """
        archivo = open("codigoGraphiz.dot","w")
        archivo.write(codigoGraphiz)
        archivo.close()
        system('dot -Tpng codigoGraphiz.dot -o codigoGraphiz.png')
        system('cd ./codigoGraphiz.png')
        startfile('codigoGraphiz.png')
    
    def analizarOrganismos(self):
        organismos = self.muestraAnalizada.listaOrganismos
        auxiliar = organismos.cabeza
        i = 1
        print()
        while(auxiliar != None):
            organismo:Organismo = auxiliar.dato
            print(f"{i}. {organismo.nombre} - {organismo.codigo}")
            auxiliar = auxiliar.siguiente
            i += 1
        opcion = int(input("\nIngrese el numero del organismo a elegir: "))
        
        
    def pedirNumeroEntero(self):    #Metodo para seleccionar una opcion en el menu
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Introduce un numero entero: "))
                correcto=True
            except ValueError:
                print('Error, introduce un numero entero')
        return num

    def menu(self): #Menu con las opciones a elejir
        salir = False
        opcion = 0
        while not salir:
            print("\n##          ###    ########   #######  ########     ###    ########  #######  ########  ####  #######  ")
            print("##         ## ##   ##     ## ##     ## ##     ##   ## ##      ##    ##     ## ##     ##  ##  ##     ## ")
            print("##        ##   ##  ##     ## ##     ## ##     ##  ##   ##     ##    ##     ## ##     ##  ##  ##     ## ")
            print("##       ##     ## ########  ##     ## ########  ##     ##    ##    ##     ## ########   ##  ##     ## ")
            print("##       ######### ##     ## ##     ## ##   ##   #########    ##    ##     ## ##   ##    ##  ##     ## ")
            print("##       ##     ## ##     ## ##     ## ##    ##  ##     ##    ##    ##     ## ##    ##   ##  ##     ## ")
            print("######## ##     ## ########   #######  ##     ## ##     ##    ##     #######  ##     ## ####  #######  ")
            print("\n------------------------")
            print("-----MENU PRINCIPAL-----")
            print("1. Cargar Archivo XML")
            print("2. Generar Muestra")
            print("3. Seleccionar un organismo")
            print("4. Generar archivo de Salida")
            print("5. Salir")
            print("------------------------\n")
            
            print ("Elige una opcion")
 
            opcion = self.pedirNumeroEntero()
 
            if opcion == 1:
                print("Seleccione el archivo a cargar...")
                filename = askopenfilename(initialdir="C:/")
                xml = ET.parse(filename)
                self.cargarArchivo(xml)
                print("\n¡ARCHIVO CARGADO CORRECTAMENTE!")
            elif opcion == 2:
                self.graficarMuestra()
                print("\n¡LA MUESTRA SE GENERO CORRECTAMENTE!")
            elif opcion == 3:
                self.analizarOrganismos()
            elif opcion == 4:
                pass
            elif opcion == 5:
                salir = True
            else:
                print ("\nIntroduce un numero entre 1 y 5")
        print ("\nFIN DEL PROGRAMA")