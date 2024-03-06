#include <MeMCore.h>
#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(1,0);  
MeDCMotor motor3(M1); 
MeDCMotor motor4(M2); 
uint8_t motorSpeed = 100; 

void setup() {
  Serial.begin(115200);
  bluetoothSerial.begin(115200);
}

void loop() {
  while (!bluetoothSerial.available()) {}
    char command = bluetoothSerial.read();
    if (command == 'w') {
      motor3.run(-motorSpeed);
      motor4.run(motorSpeed);
    }
  else {
    motor3.stop();
    motor4.stop();
  }
}
