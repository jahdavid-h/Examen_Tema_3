from idioma import Idioma
from moneda import Moneda
from poblacion import Poblacion

poblacion = Poblacion()

poblacion.set_nombre_continente("Asia")
poblacion.set_area_continente("44579000")
poblacion.set_numero_de_paises("48")

poblacion.set_nombre_pais("India")
poblacion.set_fronteras("China, Pakistan, Nepal")
poblacion.set_no_estados("28")

poblacion.set_clima("Tropical")
poblacion.set_rios("Ganges, Yamuna")
poblacion.set_monta("Himalayas")

poblacion.set_estado("Maharashtra")
poblacion.set_area("307713")
poblacion.set_estados_vecinos("Goa, Gujarat, Madhya Pradesh")

poblacion.set_numero_de_habitantes("112374333")
poblacion.set_distribucion_genero("Hombres: 55000000, Mujeres: 57374333")


idioma = Idioma()

idioma.set_idioma("Hindi")
idioma.set_codigo_iso("HI")


moneda = Moneda()

moneda.set_moneda_nacional("Rupia India")
moneda.set_codigo_iso_moneda("INR")
moneda.set_valor("75.65")
moneda.set_fecha_emision("15/08/2022")


print("")
print("Informacion Continente")
poblacion.mostrar_info_continente()
print("")
print("Informacion Pais")
poblacion.mostrar_info_pais()
print("")
print("Informacion Idioma")
idioma.mostrar_info_idioma()
print("")
print("Informacion Moneda")
moneda.mostar_info_moneda()
print("")
print("Informacion Geografica")
poblacion.mostrar_info_geografia()
print("")
print("Informacion Estado")
poblacion.mostrar_info_estado()
print("")
print("Informacion Poblacion")
poblacion.mostrar_info_poblacion()