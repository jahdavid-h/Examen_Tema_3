
from estado import Estado

class Poblacion(Estado):
    def __init__(self):
        Estado.__init__(self)
        self.__numero_de_habitantes = 0
        self.__distribucion_genero = 0

    #Getters
    def get_numero_de_habitantes(self):
        return self.__numero_de_habitantes

    def get_distribucion_genero(self):
        return self.__distribucion_genero

    #Setters
    def set_numero_de_habitantes(self, numero_de_habitantes):
        self.__numero_de_habitantes = numero_de_habitantes

    def set_distribucion_genero(self, distribucion_genero):
        self.__distribucion_genero = distribucion_genero


    def mostrar_info_poblacion(self):
        print (f"- No. de Habitantes de {self.get_estado()}: {self.get_numero_de_habitantes()} habitantes \n"
               f"- Distribucion de Genero: {self.get_distribucion_genero()}")