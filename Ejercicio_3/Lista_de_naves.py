from Nave import Nave

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

        return nave_necesitada

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


nave1 = Nave('Halcón Milenario', 20, 32, 6)
nave2 = Nave('Estrella de la Muerte', 20, 33, 1)
nave3 = Nave('ATomar por culo', 25, 35, 8)
nave4 = Nave('atwedm', 6, 45, 23)
nave5 = Nave('Estacion espacial internacional', 23, 8, 12)
nave6 = Nave('Murcia', 87, 4, 3)
nave7 = Nave('aTfm', 9, 5, 4)

naves = Naves([nave1, nave2, nave3, nave4, nave5, nave6, nave7])

print(naves.nave_con_menos_tripulacion())










