#include "MeMCore.h"

MeDCMotor motor3(M1);
MeDCMotor motor4(M2);

uint8_t motorSpeed = 100;
uint8_t turnSpeed = 80;

void setup() {
  Serial.begin(9600);

  motor3.stop();
  motor4.stop();
}

void loop() {
  if (Serial.available()) {
    char input = Serial.read();

    if (input == 'w') {
      motor3.run(-motorSpeed);
      motor4.run(motorSpeed);
      delay(2000);
    } else if (input == 's') {
      motor3.run(motorSpeed);
      motor4.run(-motorSpeed);
      delay(2000);
    } else if (input == 'a') {
      motor3.run(-turnSpeed);
      motor4.run(-turnSpeed);
      delay(2000);
    } else if (input == 'd') {
      motor3.run(turnSpeed);
      motor4.run(motorSpeed);
      delay(2000);
    } else {
      motor3.stop();
      motor4.stop();
      delay(2000);
    }
  }
}
