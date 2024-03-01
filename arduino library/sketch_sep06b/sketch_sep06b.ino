#include <MeMCore.h>
#include <SoftwareSerial.h>

MeUltrasonicSensor ultrasonic;
MeDCMotor motor3(M1);
MeDCMotor motor4(M2);

uint8_t motorSpeed = 100;
uint8_t turnSpeed = 80;

void setup() {
  Serial.begin(9600);

  ultrasonic.setpin(3); // Configurar el pin del sensor ultrasónico
}

void loop() {
  int distance = ultrasonic.distanceCm(); // Leer la distancia con el sensor ultrasónico
  Serial.print("Distancia: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  if (distance < 10) {
    // Si la distancia es menor a 10 cm, retrocede durante 1 segundo
    motor3.run(motorSpeed);
    motor4.run(-motorSpeed);
    delay(1000);
  } else {
    // Si la distancia es mayor o igual a 10 cm, avanza hacia adelante
    motor3.run(-motorSpeed);
    motor4.run(motorSpeed);
  }
  
  if (Serial.available()) {
    char input = Serial.read();
    if (input == 's') {
      motor3.stop();
      motor4.stop();
      delay(2000);
    }
  }
}
