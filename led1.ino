int ledPin = 2; // LED connected to digital pin 2
int inPin = 13; // pushbutton connected to digital pin 13
//int val = 0;  // variable to store the read value

void setup()
{ 
pinMode(ledPin, OUTPUT);   //set OUTPUT
pinMode(inPin, INPUT);        //set INPUT   
}

void loop()
{ 
//val = digitalRead(inPin);  // read the input pin 
digitalWrite(ledPin, digitalRead(inPin));  // sets the LED to the button's value
}
