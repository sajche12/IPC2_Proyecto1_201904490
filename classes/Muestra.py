from .ListaSimple import ListaEnlazada

class Muestra:

    dimensionX:int
    dimensionY:int
    listaOrganismos:ListaEnlazada
    listaCeldasVivas:ListaEnlazada

    def __init__(self,codigo,descripcion,dimensionX,dimensionY):
        self.codigo=codigo
        self.descripcion=descripcion
        self.dimensionX=dimensionX
        self.dimensionY=dimensionY
        self.listaOrganismos = ListaEnlazada()
        self.listaCeldasVivas = ListaEnlazada()