class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangulo:
    def __init__(self, esquina_inferior, esquina_superior):
        self.esquina_inferior = esquina_inferior
        self.esquina_superior = esquina_superior

    def perimetro(self):
        base = abs(self.esquina_superior.x - self.esquina_inferior.x)
        altura = abs(self.esquina_superior.y - self.esquina_inferior.y)
        perimetro = 2 * (base + altura)
        return perimetro


    def area(self):
        base = abs(self.esquina_superior.x - self.esquina_inferior.x)
        altura = abs(self.esquina_superior.y - self.esquina_inferior.y)
        area = base * altura
        return area


    def es_cuadrado(self):
        base = abs(self.esquina_superior.x - self.esquina_inferior.x)
        altura = abs(self.esquina_superior.y - self.esquina_inferior.y)
        return base == altura

if __name__ == "__main__":
    punto_inferior = (1, 2)
    punto_superior = (4, 5)

rectangulo = Rectangulo(punto_inferior, punto_superior)

perimetro = rectangulo.perimetro()
area = rectangulo.area()
print("el perímetro del rectángulo es: ", perimetro)
print("el area del rectángulo es: ", area)


if rectangulo.es_cuadrado():
    print("El rectángulo es un cuadrado")
else:
    print("El rectángulo no es un cuadrado")
