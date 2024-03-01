import serial
import time

# Configura el puerto serial
serial_port = "COM5"  # Reemplaza "COMX" con el puerto serial correcto de tu mBot
baud_rate = 9600

# Inicializa la conexión serial
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Función para enviar comandos al mBot
def enviar_comando(comando):
    ser.write((comando + '\n').encode())

# Ejemplo de uso
try:
    # Enviar comando para avanzar durante 2 segundos
    enviar_comando('w')
    time.sleep(2)

    # Enviar comando para detenerse
    enviar_comando('s')
    time.sleep(1)

    # Otros comandos según sea necesario...

finally:
    # Cerrar la conexión serial al finalizar
    ser.close()
