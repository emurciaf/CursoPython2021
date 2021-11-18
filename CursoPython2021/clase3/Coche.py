
class Coche:
    def __init__(self, marca, modelo, tipo):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.capacidad_gasolina = 15
        self.nivel_gasolina = 0

    def gasolina_completo(self):
        self.nivel_gasolina = self.capacidad_gasolina
        print('El depósito de gasolina etá lleno')

    def conducir(self):
        print(f'El {self.modelo} se está conduciendo')

objeto_coche = Coche('SEAT', 'Ateca', '1.0')

class CocheElectrico(Coche):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo, tipo)
        self.battery_size = 100
        self.charge_level = 0

    def cargar(self):
            self.charge_level = 100
            print('El coche está cargado')


# Acceder a los atributos de ese objeto
print(objeto_coche.marca)
print(objeto_coche.modelo)
print(objeto_coche.tipo)

# Llamando a los métodos de la clase
print()     #línea en blanco
objeto_coche.gasolina_completo()
objeto_coche.conducir()

coche_electrico = CocheElectrico('TESLA', 'Model 3', 'Berlina')

print(coche_electrico.modelo)
coche_electrico.cargar()
coche_electrico.conducir()

# print(help(coche_electrico))
print(CocheElectrico.__mro__)


