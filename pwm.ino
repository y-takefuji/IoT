void setup() {
  pinMode(2,OUTPUT);

}

void loop() {
  for(int i=0;i<13;i++){
   for(int j=0;j<20-i;j++){
    digitalWrite(2,1);
    delay(i);
    digitalWrite(2,0);
    delay(13-i);
     }       
   }
   for(int i=0;i<13;i++){
   for(int j=0;j<20-i;j++){
    digitalWrite(2,0);
    delay(i);
    digitalWrite(2,1);
    delay(13-i);
     }       
   }
   digitalWrite(2,0);
 
}
