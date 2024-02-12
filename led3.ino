int ledPin=2;
int sensorPin = A7; 
int sensorValue = 0; 
int th=0;

void setup()
{ 
pinMode(ledPin, OUTPUT); 
Serial.begin(9600);
for(int i=0;i<8;i++)
{ th = th + analogRead(sensorPin);}
 th= th/8; th=th-30;
}

void loop()
{ 
sensorValue = analogRead(sensorPin);
if(sensorValue>th)
{digitalWrite(ledPin, 0);}  
else {digitalWrite(ledPin,1);}
Serial.println(sensorValue,DEC);
delay(1000);
}
