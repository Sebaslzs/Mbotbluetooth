#include <MeMCore.h>

MeDCMotor motor3(M1); 
MeDCMotor motor4(M2); 
uint8_t motorSpeed = 100; 
uint8_t turnSpeed = 80;   

void setup() {
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available()) { 
    char input = Serial.read(); 

    switch (input) {
      case 'w': 
        motor3.run(-motorSpeed);
        motor4.run(motorSpeed);
        break;
      case 's': 
        motor3.run(motorSpeed);
        motor4.run(-motorSpeed);
        break;
      case 'a': 
        motor3.run(-turnSpeed);
        motor4.run(-turnSpeed);
        break;
      case 'd': 
        motor3.run(turnSpeed);
        motor4.run(turnSpeed);
        break;
      case 'x': 
        motor3.stop();
        motor4.stop();
        break;
      default: 
        motor3.stop();
        motor4.stop();
        break;
    }
    delay(2000); 
  }
}
