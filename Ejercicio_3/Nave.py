class Nave():
    def __init__(self, nombre, largo , tripulacion, n_pasajeros):
        self.nombre = nombre
        self. largo = largo
        self.tripulacion = tripulacion
        self.n_pasajeros = n_pasajeros


    ##Getters y setters(encapsulación)
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_largo(self):
        return self.largo

    def set_largo(self, largo):
        self.largo = largo

    def get_tripulacion(self):
        return self.tripulacion

    def set_tripulacion(self, tripulacion):
        self.tripulacion = tripulacion

    def get_n_pasajeros(self):
        return self.n_pasajeros

    def set_n_pasajeros(self, n_pasajeros):
        self.n_pasajeros = n_pasajeros

    def __str__(self):
        return f'nombre {self.nombre}\n largo {self. largo}\n tripulacion {self.tripulacion} n_pasajeros {self.n_pasajeros}'
