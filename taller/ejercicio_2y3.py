import math


class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def mostrar(self):
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)
        return distancia


if __name__ == "__main__":
   punto1 = Punto(1, 2)
   punto2 = Punto(4, 6)

punto1.mostrar()
punto2.mostrar()


punto1.mover(3, 5)
punto1.mostrar()


distancia = punto1.calcular_distancia(punto2)
print("Distancia entre los puntos:", distancia)



