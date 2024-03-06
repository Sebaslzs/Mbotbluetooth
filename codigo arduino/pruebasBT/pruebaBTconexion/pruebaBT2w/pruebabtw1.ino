#include <MeMCore.h>

  

MeDCMotor motor3(M1); 

MeDCMotor motor4(M2); 

  

uint8_t motorSpeed = 100; 

uint8_t turnSpeed = 80; 

  

void setup() 

{ 

  Serial.begin(9600); 

} 

  

void loop() 

{ 

  if (Serial.available()) 

  { 

    char input = Serial.read(); 

    if (input == 'w') 

    { 

      motor3.run(-motorSpeed); 

      motor4.run(motorSpeed); 

      delay(2000); 

    } 

  }
}