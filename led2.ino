int ledPin=2;
int sensorPin = A7; 
int sensorValue = 0; 

void setup()
{ 
analogReference(DEFAULT);
pinMode(ledPin, OUTPUT); 
}

void loop()
{ 
sensorValue = analogRead(sensorPin);
if(sensorValue>80)
{digitalWrite(ledPin, 0);}  
else {digitalWrite(ledPin,1);}
}
