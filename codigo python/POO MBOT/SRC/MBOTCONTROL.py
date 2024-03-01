import serial

class MbotControl:
    def __init__(self, puerto):
        self.puerto = serial.Serial(puerto, 9600)

    def mover_arriba(self):
        self.puerto.write(b'w')

    def mover_abajo(self):
        self.puerto.write(b's')

