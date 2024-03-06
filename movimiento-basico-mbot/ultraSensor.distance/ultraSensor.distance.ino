#include <MeMCore.h>

MeUltrasonicSensor ultraSensor(PORT_5);

void setup()
{
  MeMCore.begin();
  Serial.begin(9600);
}

void loop()
{
  int distance = ultraSensor.distanceCm();

  Serial.print("Distancia: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance <= 10) // Si se detecta un objeto a una distancia menor o igual a 10 cm
  {
    MeMCore.motorsStop(); // Detener ambos motores

    delay(500); // Esperar medio segundo

    // Girar a la derecha
    MeMCore.motorRun(M1, BACKWARD);
    MeMCore.motorRun(M2, FORWARD);
    delay(1000); // Girar durante 1 segundo

    // Seguir recto
    MeMCore.motorRun(M1, FORWARD);
    MeMCore.motorRun(M2, FORWARD);
    delay(2000); // Moverse hacia adelante durante 2 segundos
  }
  else
  {
    // Seguir recto
    MeMCore.motorRun(M1, FORWARD);
    MeMCore.motorRun(M2, FORWARD);
  }
}

