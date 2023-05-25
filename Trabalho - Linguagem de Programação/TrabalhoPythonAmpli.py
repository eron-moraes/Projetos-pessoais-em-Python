class FormaGeometrica:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass


class Retangulo(FormaGeometrica):
    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Quadrado(FormaGeometrica):
    def calcular_area(self):
        return self.base ** 2

    def calcular_perimetro(self):
        return 4 * self.base


class Circulo(FormaGeometrica):
    def calcular_area(self):
        return 3.14 * (self.base/2) ** 2

    def calcular_perimetro(self):
        return 2 * 3.14 * (self.base/2)


# Programa principal
retangulo = Retangulo(5, 3)
area_retangulo = retangulo.calcular_area()
perimetro_retangulo = retangulo.calcular_perimetro()

quadrado = Quadrado(4, 0)  # Base e altura são iguais para um quadrado
area_quadrado = quadrado.calcular_area()
perimetro_quadrado = quadrado.calcular_perimetro()

circulo = Circulo(6, 0)  # Base representa o diâmetro do círculo
area_circulo = circulo.calcular_area()
perimetro_circulo = circulo.calcular_perimetro()

# Exibindo os resultados
print("Retângulo:")
print("Área:", area_retangulo)
print("Perímetro:", perimetro_retangulo)

print("\nQuadrado:")
print("Área:", area_quadrado)
print("Perímetro:", perimetro_quadrado)

print("\nCírculo:")
print("Área:", area_circulo)
print("Perímetro:", perimetro_circulo)
