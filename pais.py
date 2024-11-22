from continente import Continente

class Pais(Continente):

    def __init__(self):
        Continente.__init__(self)
        self.__nombre_pais = ""
        self.__fronteras = ""
        self.__no_estados = ""

    #Getters
    def get_nombre_pais(self):
        return self.__nombre_pais

    def get_fronteras(self):
        return self.__fronteras

    def get_no_estados(self):
        return self.__no_estados

    #Setters
    def set_nombre_pais(self, nombre_pais):
        self.__nombre_pais = nombre_pais

    def set_fronteras(self, fronteras):
        self.__fronteras = fronteras

    def set_no_estados(self, no_estados):
        self.__no_estados = no_estados


    def mostrar_info_pais(self):
        print (f"- Nombre: {self.get_nombre_pais()} \n"
                f"- Fronteras: {self.get_fronteras()} \n"
                f"- No. de estados: {self.get_no_estados()} ")