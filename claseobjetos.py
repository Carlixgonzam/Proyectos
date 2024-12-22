class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.ruedas)
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__() + ", Velocidad (km/hr): " + str(self.velocidad)
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + ", Tipo: " + self.tipo
    

vehiculo = Vehiculo("Rojo", 4)
print(vehiculo)

coche= Coche("Azul", 4, 150)
print(coche)

bicicleta = Bicicleta("Blanca", 2, "Urbano")
print(bicicleta)



class Empleado:
    def __init__(self, nombre, cedula, telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_cedula(self, cedula):
        self._cedula = cedula
    def get_cedula(self):
        return self._cedula
    def set_telefono(self, telefono):
        self._telefono = telefono
    def get_telefono(self):
        return self._telefono
