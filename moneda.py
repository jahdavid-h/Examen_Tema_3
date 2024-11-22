
from pais import Pais

class Moneda(Pais):
    def __init__(self):
        Pais.__init__(self)
        self.__moneda_nacional = ""
        self.__codigo_iso = ""
        self.__valor = 0
        self.__fecha_emision = ""

    #Getters
    def get_moneda_nacional(self):
        return self.__moneda_nacional

    def get_codigo_iso_moneda(self):
        return self.__codigo_iso

    def get_valor(self):
        return self.__valor

    def get_fecha_emision(self):
        return self.__fecha_emision

    #Setters
    def set_moneda_nacional(self, moneda_nacional):
        self.__moneda_nacional = moneda_nacional

    def set_codigo_iso_moneda(self, codigo_iso_moneda):
        self.__codigo_iso = codigo_iso_moneda

    def set_valor(self, valor):
        self.__valor = valor

    def set_fecha_emision(self, fecha_emision):
        self.__fecha_emision = fecha_emision


    def mostar_info_moneda(self):
        print (f"- Moneda Nacional: {self.get_moneda_nacional()} \n"
                f"- Codigo ISO: {self.get_codigo_iso_moneda()} \n"
                f"- Valor: {self.get_valor()} \n"
                f"- Fecha Emision: {self.get_fecha_emision()}")
