#include <SoftwareSerial.h>
SoftwareSerial mySerial(2,3);
int led = 7;

// 모터 드라이버 핀 설정
int IN1 = 12; int IN2 = 13; int ENA = 11;
int IN3 = 8; int IN4 = 9; int ENB = 10;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(ENA, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT); pinMode(ENB, OUTPUT);
  mySerial.begin(9600);
  Serial.begin(9600);
}

void motor1Forward(int speed) {
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW); analogWrite(ENA, speed);
}

void motor2Forward(int speed) {
  digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW); analogWrite(ENB, speed);
}

void motor1Backward(int speed) {
  digitalWrite(IN1, LOW); digitalWrite(IN2, HIGH); analogWrite(ENA, speed);
}

void motor2Backward(int speed) {
  digitalWrite(IN3, LOW); digitalWrite(IN4, HIGH); analogWrite(ENB, speed);
}

void motorStop() { // 모터 정지 함수
  digitalWrite(IN1, LOW); digitalWrite(IN2, LOW); analogWrite(ENA, 0);
  digitalWrite(IN3, LOW); digitalWrite(IN4, LOW); analogWrite(ENB, 0);
}

void loop() {
  byte r_data;
  if(mySerial.available() > 0){
    r_data = mySerial.read();
    switch(r_data){
      case 0: digitalWrite(led, LOW);
              Serial.println("led off");
              motor1Forward(175);
              motor2Forward(40);
              delay(1500); 
              motorStop(); 
              delay(1500);
              break;
      case 1: digitalWrite(led, HIGH);
              Serial.println("led on");
              motor1Backward(175);
              motor2Backward(40);
              delay(1500);
              motorStop(); 
              delay(1500);
              break;
    }
  }
}
