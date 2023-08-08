class Vehiculo:
    def __init__(self, velociadad_maxima: float, kilometraje: float):
        self.velocidad_maxima: float = velociadad_maxima
        self.kilometraje: float = kilometraje

if __name__ == "__main__":
    v: Vehiculo = Vehiculo( 160, 10000)

print(v.velocidad_maxima)
print(v.kilometraje)
