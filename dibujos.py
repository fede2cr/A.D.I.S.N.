# Clase para imprimir las caras, dado que no hay para dibujar BMPs
# en Circuitpython

from board import *
import busio
# Import the HT16K33 LED matrix module.
from adafruit_ht16k33 import matrix
# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
matrix = matrix.Matrix8x8(i2c)

class Caritas:

    def sonrisa():
        matrix.fill(0)
        # Son 8 columnas... contando del 0 al 7
        # Columna 0
        matrix.pixel(0, 2, 1)
        matrix.pixel(0, 3, 1)
        matrix.pixel(0, 4, 1)
        matrix.pixel(0, 5, 1)
        # Columna 1
        matrix.pixel(1, 1, 1)
        matrix.pixel(1, 6, 1)
        # Columna 2
        matrix.pixel(2, 0, 1)
        matrix.pixel(2, 3, 1)
        matrix.pixel(2, 4, 1)
        matrix.pixel(2, 7, 1)
        # Columna 3
        matrix.pixel(3, 0, 1)
        matrix.pixel(3, 2, 1)
        matrix.pixel(3, 5, 1)
        matrix.pixel(3, 7, 1)
        # Columna 4
        matrix.pixel(4, 0, 1)
        matrix.pixel(4, 7, 1)
        # Columna 5
        matrix.pixel(5, 0, 1)
        matrix.pixel(5, 2, 1)
        matrix.pixel(5, 5, 1)
        matrix.pixel(5, 7, 1)
        # Columna 6
        matrix.pixel(6, 1, 1)
        matrix.pixel(6, 6, 1)
        # Columna 7
        matrix.pixel(7, 2, 1)
        matrix.pixel(7, 3, 1)
        matrix.pixel(7, 4, 1)
        matrix.pixel(7, 5, 1)
        matrix.show()

    def neutral():
        matrix.fill(0)
        # Son 8 columnas... contando del 0 al 7
        # Columna 0
        matrix.pixel(0, 2, 1)
        matrix.pixel(0, 3, 1)
        matrix.pixel(0, 4, 1)
        matrix.pixel(0, 5, 1)
        # Columna 1
        matrix.pixel(1, 1, 1)
        matrix.pixel(1, 6, 1)
        # Columna 2
        matrix.pixel(2, 0, 1)
        matrix.pixel(2, 2, 1)
        matrix.pixel(2, 3, 1)
        matrix.pixel(2, 4, 1)
        matrix.pixel(2, 5, 1)
        matrix.pixel(2, 7, 1)
        # Columna 3
        matrix.pixel(3, 0, 1)
        matrix.pixel(3, 7, 1)
        # Columna 4
        matrix.pixel(4, 0, 1)
        matrix.pixel(4, 7, 1)
        # Columna 5
        matrix.pixel(5, 0, 1)
        matrix.pixel(5, 2, 1)
        matrix.pixel(5, 5, 1)
        matrix.pixel(5, 7, 1)
        # Columna 6
        matrix.pixel(6, 1, 1)
        matrix.pixel(6, 6, 1)
        # Columna 7
        matrix.pixel(7, 2, 1)
        matrix.pixel(7, 3, 1)
        matrix.pixel(7, 4, 1)
        matrix.pixel(7, 5, 1)
        matrix.show()

    def triste():
        matrix.fill(0)
        # Son 8 columnas... contando del 0 al 7
        # Columna 0
        matrix.pixel(0, 2, 1)
        matrix.pixel(0, 3, 1)
        matrix.pixel(0, 4, 1)
        matrix.pixel(0, 5, 1)
        # Columna 1
        matrix.pixel(1, 1, 1)
        matrix.pixel(1, 6, 1)
        # Columna 2
        matrix.pixel(2, 0, 1)
        matrix.pixel(2, 2, 1)
        matrix.pixel(2, 5, 1)
        matrix.pixel(2, 7, 1)
        # Columna 3
        matrix.pixel(3, 0, 1)
        matrix.pixel(3, 3, 1)
        matrix.pixel(3, 4, 1)
        matrix.pixel(3, 7, 1)
        # Columna 4
        matrix.pixel(4, 0, 1)
        matrix.pixel(4, 7, 1)
        # Columna 5
        matrix.pixel(5, 0, 1)
        matrix.pixel(5, 2, 1)
        matrix.pixel(5, 5, 1)
        matrix.pixel(5, 7, 1)
        # Columna 6
        matrix.pixel(6, 1, 1)
        matrix.pixel(6, 6, 1)
        # Columna 7
        matrix.pixel(7, 2, 1)
        matrix.pixel(7, 3, 1)
        matrix.pixel(7, 4, 1)
        matrix.pixel(7, 5, 1)
        matrix.show()
