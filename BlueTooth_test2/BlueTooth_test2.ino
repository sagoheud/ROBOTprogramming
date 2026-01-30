#include <SoftwareSerial.h>
SoftwareSerial BTSerial(2,3); // rx, tx
int led = 7;

// 모터 드라이버 핀 설정
int IN1 = 12; int IN2 = 13; int ENA = 11;
int IN3 = 8; int IN4 = 9; int ENB = 10;

bool isRepeat = false;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(ENA, OUTPUT);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT); pinMode(ENB, OUTPUT);
  BTSerial.begin(9600);
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

void motorStop() {
  digitalWrite(IN1, LOW); digitalWrite(IN2, LOW); analogWrite(ENA, 0);
  digitalWrite(IN3, LOW); digitalWrite(IN4, LOW); analogWrite(ENB, 0);
}

void loop() {
  char bt;
  if(BTSerial.available() > 0) {
    bt = BTSerial.read();
    if(bt == 'a') {
      digitalWrite(led, HIGH);
      Serial.println(bt);
      isRepeat = true;
    }
    else if(bt == 'b') {
      digitalWrite(led, LOW);
      Serial.println(bt);
      isRepeat = false;
    }
  }

  if (isRepeat) {
    motor1Forward(175);
    motor2Forward(40);
    delay(1500); 
    motorStop(); 
    delay(500);
    
    motor1Backward(175);
    motor2Backward(40);
    delay(1500);
    motorStop(); 
    delay(500);
  }
}
