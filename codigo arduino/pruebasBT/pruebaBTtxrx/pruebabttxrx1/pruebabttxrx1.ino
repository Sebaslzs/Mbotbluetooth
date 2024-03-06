#include <MeMCore.h>
#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(1,0);  
unsigned char table[128] = {0};

void setup()
{
  Serial.begin(115200);
  bluetoothSerial.begin(115200);  
  Serial.println("Bluetooth Start!");

  Serial.println("Connecting to Bluetooth...");
}

void loop()
{ 
  int readdata = 0, i = 0, count = 0;
  char outDat;

  if (bluetoothSerial.available())
  {
    while ((readdata = bluetoothSerial.read()) != -1)
    {
      table[count] = readdata;
      count++;
      delay(1);
    }
    for (i = 0; i < count; i++)
    {
      Serial.write(table[i]);
    }
  }

  if (Serial.available())
  {
    outDat = Serial.read();
    bluetoothSerial.write(outDat);
  }

  if (bluetoothSerial.available() > 0 || bluetoothSerial.read() != -1)
  {
    Serial.println("Bluetooth Connected!");
  }
  else
  {
    Serial.println("Bluetooth Disconnected!");
  }
}
