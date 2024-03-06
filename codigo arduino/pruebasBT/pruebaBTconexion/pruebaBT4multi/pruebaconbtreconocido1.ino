#include <MeMCore.h>
#include <SoftwareSerial.h>



SoftwareSerial bluetoothSerial(1,0);  

MeDCMotor motor3(M1); 
MeDCMotor motor4(M2); 

uint8_t motorSpeed = 100; 
uint8_t turnSpeed = 80;   

void setup() {
  Serial.begin(115200);
  bluetoothSerial.begin(115200);  
  Serial.println("Bluetooth Start!");

  motor3.stop();  
  motor4.stop();
}

void loop() {
  int readdata = 0;

  if (bluetoothSerial.available()) {
    readdata = bluetoothSerial.read();  

    switch (readdata) {
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
      case 
        motor3.stop();
        motor4.stop();
        break;
      default: 
        motor3.stop();
        motor4.stop();
        break;
    }
  }
}
