int ledPin=2;

void setup()
{ 
pinMode(ledPin, OUTPUT); 
Serial.begin(9600);
Serial.println("ready");
}

void loop()
{ 
    if ( Serial.available()){
      char ch = Serial.read();
    Serial.print(ch);
    if(ch == '1') {digitalWrite(ledPin,1);}
    if(ch == '0') {digitalWrite(ledPin,0);}
   }
}
