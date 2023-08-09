import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

    def punto_pertenece(self, punto):
        distancia_centro = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia_centro <= self.radio

if __name__ == "__main__":
    centro = Punto(3, 4)
    circulo = Circulo(centro, 5)


area = circulo.calcular_area()
perimetro = circulo.calcular_perimetro()

print("Área del círculo: ", area)
print("Perímetro del círculo: ", perimetro)


punto_prueba = Punto(6, 5)
if circulo.punto_pertenece(punto_prueba):
    print("El punto pertenece al círculo.")
else:
    print("El punto no pertenece al círculo.")