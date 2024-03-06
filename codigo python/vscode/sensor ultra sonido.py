import serial
arduinoSerialData = serial.Serial('COM4', 9600)
while True:
    if (arduinoSerialData.inWaiting( )> 0):
        myData = arduinoSerialData.readline()
        datos = float(myData)
        print(datos)