#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(1,0);  
int buzzerPin = 8; 

void setup() {
  Serial.begin(115200);
  bluetoothSerial.begin(115200);  
  Serial.println("Bluetooth Start!");

  pinMode(buzzerPin, OUTPUT); 
}

void loop() {
  if (bluetoothSerial.available()) {
    tone(buzzerPin, 1000); // Emite un tono en el buzzer
  } else {
    noTone(buzzerPin); // Apaga el buzzer
  }
  delay(1000); 
}
