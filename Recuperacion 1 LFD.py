import math
import unittest

def calcular_area_circulo(radio):
    """
    Funcion para calcular el área de un círculo.
    :param radio: Radio del círculo.
    :return: El área del círculo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * radio**2

def calcular_area_triangulo(base, altura):
    """
    Funcion para calcular el área de un triángulo.
    :param base: Longitud de la base del triángulo.
    :param altura: Altura del triángulo.
    :return: El área del triángulo.
    """
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura deben ser mayores a cero.")
    return 0.5 * base * altura

def calcular_area_cuadrado(lado):
    """
    Funcion para calcular el área de un cuadrado.
    :param lado: Longitud de un lado del cuadrado.
    :return: El área del cuadrado.
    """
    if lado < 0:
        raise ValueError("El lado no puede ser negativo.")
    return lado**2

def calcular_volumen_cubo(lado):
    """
    Funcion para calcular el volumen de un cubo.
    :param lado: Longitud de un lado del cubo.
    :return: El volumen del cubo.
    """
    if lado < 0:
        raise ValueError("El lado no puede ser negativo.")
    return lado**3

# Pruebas unitarias de las areas y volumenes
class TestCalculadoraGeometrica(unittest.TestCase):

    def test_area_circulo(self):
        self.assertAlmostEqual(calcular_area_circulo(2), math.pi * 4)
    
    def test_area_triangulo(self):
        self.assertEqual(calcular_area_triangulo(3, 4), 6)
    
    def test_area_cuadrado(self):
        self.assertEqual(calcular_area_cuadrado(5), 25)
    
    def test_volumen_cubo(self):
        self.assertEqual(calcular_volumen_cubo(2), 8)

if __name__ == "__main__":
    unittest.main()

