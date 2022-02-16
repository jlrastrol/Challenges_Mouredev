'''
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Fecha publicación resolución: 31/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''
class poligono:

    area = 0


    def getArea(self):
        pass

    def printArea(self):
        print(self.area)

class triangulo(poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
 
    def getArea(self):
        self.area = (self.base * self.altura)/2 
        self.printArea()

class rectangulo(poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
 
    def getArea(self):
        self.area = (self.base * self.altura)
        self.printArea()

class cuadrado(poligono):
    def __init__(self, lado):
        self.lado = lado
 
    def getArea(self):
        self.area = (self.lado * self.lado)
        self.printArea()


triangulo(7,3).getArea()
rectangulo(7,3).getArea()
cuadrado(7).getArea()
