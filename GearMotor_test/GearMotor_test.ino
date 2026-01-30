int IN1 = 7; int IN2 = 8; int ENA = 6; // 아날로그 신호의 경우 3, 5, 6, 9, 10, 11번만 가능
int sw1 = 2; int sw2 = 3;

void setup() { // 핀 설정
  pinMode(sw1, INPUT); pinMode(sw2, INPUT);
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); pinMode(ENA, OUTPUT);
  Serial.begin(9600);
  Serial.println("모터 제어 테스트 시작");
}

void motorForward(int speed) { // 정회전 함수
  digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW); analogWrite(ENA, speed); // 0~255
}

void motorBackward(int speed) { // 역회전 함수
  digitalWrite(IN1, LOW); digitalWrite(IN2, HIGH); analogWrite(ENA, speed);
}

void motorStop() { // 모터 정지 함수
  digitalWrite(IN1, LOW); digitalWrite(IN2, LOW); analogWrite(ENA, 0);
}

void loop() {
  sw1 = digitalRead(2); sw2 = digitalRead(3);
  if(sw1 == 1) {
    Serial.println("정회전 : 속도 100"); 
    motorForward(100); 
    delay(5000);
    Serial.println("정회전 : 속도 255 (최대)"); 
    motorForward(255); 
    delay(5000);
    Serial.println("정지"); 
    motorStop(); 
    delay(1500);
  }
  if(sw2 == 1) {
    Serial.println("역회전 : 속도 200"); 
    motorBackward(200); 
    delay(2000);
    Serial.println("정지"); 
    motorStop(); 
    delay(1500);
  }
}