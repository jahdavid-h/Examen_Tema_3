
class Geografia:
    def __init__(self):
        self.__clima = ""
        self.__rios = ""
        self.__monta = ""

    # Getters
    def get_clima(self):
        return self.__clima

    def get_rios(self):
        return self.__rios

    def get_monta(self):
        return self.__monta

    # Setters
    def set_clima(self, clima):
        self.__clima = clima

    def set_rios(self, rios):
        self.__rios = rios

    def set_monta(self, monta):
        self.__monta = monta


    def mostrar_info_geografia(self):
        print (f"- Clima: {self.get_clima()} \n"
                f"- Rios: {self.get_rios()} \n"
                f"- Montañas: {self.get_monta()}")