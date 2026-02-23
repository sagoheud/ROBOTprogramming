const int steps[4] = {2, 3, 4, 5}; 
const int totalStepsCW = 128; // 90도 회전
const int totalStepsCCW = 256; // 180도 회전
const int circle = 512; // 360도 회전
// 조절 수치에 따라 각도 변화 가능 (512일 때 한바퀴)
int sw1 = 7, sw2 = 8;

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(steps[i], OUTPUT);
  }
  pinMode(sw1, INPUT); 
  pinMode(sw2, INPUT);
}

void moveMotorClockwise() { // 정회전 90도 회전하는 함수
  for (int i = 0; i < totalStepsCW; i++) {
    for (int j = 0; j < 4; j++) {
      digitalWrite(steps[0], (j == 0) ? HIGH : LOW); digitalWrite(steps[1], (j == 1) ? HIGH : LOW);
      digitalWrite(steps[2], (j == 2) ? HIGH : LOW); digitalWrite(steps[3], (j == 3) ? HIGH : LOW);
      delay(10);
    }
  }
  stopMotor();
}

void moveMotorCounterClockwise() { // 역회전 180도 회전하는 함수
  for (int i = 0; i < totalStepsCCW; i++) {
    for (int j = 3; j >= 0; j--) {
      digitalWrite(steps[0], (j == 0) ? HIGH : LOW); digitalWrite(steps[1], (j == 1) ? HIGH : LOW);
      digitalWrite(steps[2], (j == 2) ? HIGH : LOW); digitalWrite(steps[3], (j == 3) ? HIGH : LOW);
      delay(10);
    }
  }
  stopMotor();
}

void stopMotor() { // 모터를 정지시키기 위해 모든 스텝 핀을 LOW로 설정
  for (int k = 0; k < 4; k++) {
    digitalWrite(steps[k], LOW);
  }
}

void Clockwisef() { // 정회전 360도 회전하는 함수
  for (int i = 0; i < circle ; i++) {
    for (int j = 0; j <= 3; j++) {
      digitalWrite(steps[0], (j == 0) ? HIGH : LOW);
      digitalWrite(steps[1], (j == 1) ? HIGH : LOW);
      digitalWrite(steps[2], (j == 2) ? HIGH : LOW);
      digitalWrite(steps[3], (j == 3) ? HIGH : LOW);
      delay(10);
    }
  }
  stopMotor();
}

void Clockwiser() { // 역회전 360도 회전하는 함수
  for (int i = 0; i < circle ; i++) {
    for (int j = 3; j >= 0; j--) {
      digitalWrite(steps[0], (j == 0) ? HIGH : LOW);
      digitalWrite(steps[1], (j == 1) ? HIGH : LOW);
      digitalWrite(steps[2], (j == 2) ? HIGH : LOW);
      digitalWrite(steps[3], (j == 3) ? HIGH : LOW);
      delay(10);
    }
  }
  stopMotor();
}

void loop() {
  sw1 = digitalRead(7); // 스위치1 핀 설정
  sw2 = digitalRead(8); // 스위치2 핀 설정
  
  if (sw1 == 1) { // 스위치1 누르면 정회전 90도, 역회전 180도 회전
    moveMotorClockwise();
    delay(1000);
    moveMotorCounterClockwise();
    delay(1000);
  }
  else if (sw2 == 1) { // 스위치2 누르면 정회전 360도, 역회전 360도 회전
    Clockwisef();
    delay(1000);
    Clockwiser();
    delay(1000);
  }
}