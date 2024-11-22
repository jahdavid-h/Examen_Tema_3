from pais import Pais

class Idioma(Pais):
    def __init__(self):
        Pais.__init__(self)
        self.__idioma = ""
        self.__codigo_iso = ""

    #Getters
    def get_idioma(self):
        return self.__idioma

    def get_codigo_iso(self):
        return self.__codigo_iso

    #Setters
    def set_idioma(self, idioma):
        self.__idioma = idioma

    def set_codigo_iso(self, codigo_iso):
        self.__codigo_iso = codigo_iso


    def mostrar_info_idioma(self):
        print (f"- Idioma: {self.get_idioma()} \n"
                f"- Codigo ISO: {self.get_codigo_iso()}")
