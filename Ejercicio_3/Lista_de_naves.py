from Ejercicio_3.Nave import Nave

class Naves():

    def __init__(self, lista_de_naves):
        self.lista_de_naves = lista_de_naves

    def obtener_informacion(self, nombre):
        existe = False
        for nave in self.lista_de_naves:
            if nave.get_nombre() == nombre.lower():
                existe = True
                print(nave)

        if not existe:
            print('No hemos encontrado la nave')

    def naves_con_mas_pasajeros(self):
        lista = list()
        lista_pasajeros = []
        for nave in self.lista_de_naves:
            lista_pasajeros.append(nave.get_n_pasajeros())

        lista_pasajeros.sort()
        lista_pasajeros = lista_pasajeros[:5]
        for nave in self.lista_de_naves:
            if nave.get_n_pasajeros in lista_pasajeros:
                lista.append(nave)

        return lista

    def nave_con_menos_tripulacion(self):
        x = self.lista_de_naves[0].get_tripulacion()
        for nave in self.lista_de_naves:
            if nave.get_tripulacion() <= x:
                x = nave.get_tripulacion()
                nave_necesitada = nave

        return nave

    def naves_que_comienzan_con_AT(self):
        lista = list()

        for nave in self.lista_de_naves:
            nombre = nave.get_nombre().upper()
            if 'A' == nombre[0] and 'T' == nombre[1]:
                lista.append(nave)

        return lista


    def nave_mas_grande(self):
        x = self.lista_de_naves[0].get_largo()
        for nave in self.lista_de_naves:
            if nave.get_largo() >= x:
                x = nave.get_largo()
                nave_mas_grande = nave

        return nave_mas_grande


    def nave_mas_pequeña(self):
        x = self.lista_de_naves[0].get_largo()
        for nave in self.lista_de_naves:
            if nave.get_largo() <= x:
                x = nave.get_largo()
                nave_mas_pequeña = nave

        return nave_mas_pequeña










