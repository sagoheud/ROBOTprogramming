const int steps[4] = {2, 3, 4, 5}; 
const int totalStepsCW = 128; // 256스텝 -> 90도
const int totalStepsCCW = 256; // 512스텝 -> 180도
const int circle = 512; // 1024스텝 -> 360도
int sw1Pin = 7, sw2Pin = 8;
const int stepPattern[4][4] = {{HIGH, HIGH, LOW, LOW}, {LOW, HIGH, HIGH, LOW}, {LOW, LOW, HIGH, HIGH}, {HIGH, LOW, LOW, HIGH}};
// 1스텝(0.176도) -> 신호를 계속 바꿔주며 반복해야 비로소 모터가 회전
// 2상 여자 구동 방식 -> 더 큰힘, 더 정밀해짐 , 전원 소모 크므로 외부 전원 연결 필요

void setup() { // 핀 모드 설정
  for (int i = 0; i < 4; i++) {
    pinMode(steps[i], OUTPUT);
  }
  pinMode(sw1Pin, INPUT); 
  pinMode(sw2Pin, INPUT);
}

void setStep(int step) { // 모터 한 칸 움직이기
  for (int i = 0; i < 4; i++){
    digitalWrite(steps[i],stepPattern[step][i]);
  }
}

void moveMotorClockwise(int stepsCount) { // 정방향 한칸 회전
  for (int i = 0; i < stepsCount; i++) {
    for (int j = 0; j < 4; j++) {
      setStep(j);
      delay(10);
    }
  }
  stopMotor();
}

void moveMotorCounterClockwise(int stepsCount) { // 역방향 한칸 회전
  for (int i = 0; i < stepsCount; i++) {
    for (int j = 3; j >= 0; j--) {
      setStep(j);
      delay(10);
    }
  }
  stopMotor();
}

void stopMotor() { // 모터를 정지시키기 위해 모든 스텝 핀을 LOW로 설정
  for (int i = 0; i < 4; i++) {
    digitalWrite(steps[i], LOW);
  }
}

void loop() {
  int sw1 = digitalRead(sw1Pin); // 스위치1 핀 설정
  int sw2 = digitalRead(sw2Pin); // 스위치2 핀 설정
  
  if (sw1 == HIGH) { // 스위치1 누르면 정방향으로 90도, 역방향으로 180도 회전
    moveMotorClockwise(totalStepsCW);
    delay(1000);
    moveMotorCounterClockwise(totalStepsCCW);
    delay(1000);
  }
  else if (sw2 == HIGH) { // 스위치1 누르면 정방향으로 360도, 역방향으로 360도 회전
    moveMotorClockwise(circle);
    delay(1000);
    moveMotorCounterClockwise(circle);
    delay(1000);
  }
}