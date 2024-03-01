#include <MeMCore.h>
#include <SoftwareSerial.h>

MeBluetooth bluetooth(PORT_5); // Ajusta el puerto según la conexión Bluetooth en tu placa mCore

unsigned char table[128] = {0};

void setup() {
  Serial.begin(115200);
  bluetooth.begin(115200);
  Serial.println("Bluetooth Start!");
}

void loop() {
  int readdata = 0, i = 0, count = 0;
  char outDat;

  // Lectura de datos desde el módulo Bluetooth
  if (bluetooth.available()) {
    while ((readdata = bluetooth.read()) != (int)-1) {
      table[count] = readdata;
      count++;
      delay(1);
    }
    // Enviar datos leídos al puerto serial estándar
    for (i = 0; i < count; i++) {
      Serial.write(table[i]);
    }
  }

  // Lectura de datos desde el puerto serial estándar y envío al módulo Bluetooth
  if (Serial.available()) {
    outDat = Serial.read();
    bluetooth.write(outDat);
  }
}
