#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(1,0);  // Cambia los pines 1 y 0 según tu configuración
int ledPin = 13; // Pin para el LED verde, puedes cambiarlo según tu configuración

void setup() {
  Serial.begin(115200);
  bluetoothSerial.begin(115200);  // Asegúrate de que el baud rate sea el mismo que el configurado en tu mCore
  Serial.println("Bluetooth Start!");

  pinMode(ledPin, OUTPUT); // Configura el pin del LED como salida
}

void loop() {
  if (bluetoothSerial.available()) {
    // Si hay datos disponibles en la conexión Bluetooth
    digitalWrite(ledPin, HIGH); // Enciende el LED verde
  } else {
    // Si no hay datos disponibles en la conexión Bluetooth
    digitalWrite(ledPin, LOW); // Apaga el LED verde
  }
  // Puedes agregar aquí cualquier otra lógica que desees realizar en el bucle principal
}
