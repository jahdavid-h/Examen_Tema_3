
class Continente:

    def __init__(self):
        self.__nombre_continente = ""
        self.__area_continente = ""
        self.__numero_de_paises = ""

    #Getters
    def get_nombre_continente(self):
        return self.__nombre_continente

    def get_area_continente(self):
        return self.__area_continente

    def get_numero_de_paises(self):
        return self.__numero_de_paises

    #Setters
    def set_nombre_continente(self, nombre_continente):
        self.__nombre_continente = nombre_continente

    def set_area_continente(self, area_continente):
        self.__area_continente = area_continente

    def set_numero_de_paises(self, numero_de_paises):
        self.__numero_de_paises = numero_de_paises


    def mostrar_info_continente(self):
        print (f"- Nombre: {self.get_nombre_continente()} \n"
                f"- Area: {self.get_area_continente()} \n"
                f"- Numero de paises: {self.get_numero_de_paises()} ")
