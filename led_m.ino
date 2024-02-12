//download Arduino-Scheduler-master.zip
//add Scheduler.cpp and Scheduler.h
#include "Scheduler.h"

int led1 = 2;
int led2 = 3;
int led3 = 4;

void loop1() {
  digitalWrite(led1, HIGH);
  delay(250);
  digitalWrite(led1, LOW);
  delay(250);
}

void loop2() {
  digitalWrite(led2, HIGH);
  delay(500);
  digitalWrite(led2, LOW);
  delay(500);
}

void setup() {
 pinMode(led1,OUTPUT);
 pinMode(led2,OUTPUT);
 pinMode(led3,OUTPUT);
 Scheduler.startLoop(loop1);
 Scheduler.startLoop(loop2);
}

void loop() {
  digitalWrite(led3, HIGH);
  delay(1000);
  digitalWrite(led3, LOW);
  delay(1000); 
}

