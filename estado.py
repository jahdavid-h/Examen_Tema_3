from pais import Pais
from geografia import Geografia

class Estado (Pais, Geografia):
    def __init__(self):
        Pais.__init__(self)
        Geografia.__init__(self)
        self.__estado = ""
        self.__area = ""
        self.__estados_vecinos = ""

    #Getters
    def get_estado(self):
        return self.__estado

    def get_area(self):
        return self.__area

    def get_estados_vecinos(self):
        return self.__estados_vecinos

    #Setters
    def set_estado(self, estado):
        self.__estado = estado

    def set_area(self, area):
        self.__area = area

    def set_estados_vecinos(self, estados_vecinos):
        self.__estados_vecinos = estados_vecinos


    def mostrar_info_estado(self):
        print (f"- Nombre: {self.get_estado()} \n"
                f"- Area: {self.get_area()} \n"
                f"- Estados Vecinos: {self.get_estados_vecinos()}")