int ledPin = 2;      // LED 연결 핀
char command;         // 파이썬에서 받은 명령 저장
bool isBlinking = false; // 깜빡임 상태 모드 체크

unsigned long previousMillis = 0; // 마지막으로 LED가 바뀐 시간 저장
const long interval = 500;        // 깜빡이는 간격 (0.5초)
int ledState = LOW;               // LED의 현재 상태

void setup() {
  Serial.begin(9600); // 파이썬의 baudrate와 일치
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW); // 처음엔 끄기
}

void loop() {
  // 1. 파이썬으로부터 신호가 왔는지 확인
  if (Serial.available() > 0) {
    command = Serial.read();

    if (command == 'A') {      // ON 명령
      isBlinking = false;
      digitalWrite(ledPin, HIGH);
    } 
    else if (command == 'B') { // OFF 명령
      isBlinking = false;
      digitalWrite(ledPin, LOW);
    } 
    else if (command == 'C') { // BLINKING 명령
      isBlinking = true;
    }
  }

  // 2. 깜빡임 모드일 때 동작 (비차단 방식)
  if (isBlinking) {
    unsigned long currentMillis = millis();
    
    // 0.5초마다 상태 반전
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;
      
      if (ledState == LOW) ledState = HIGH;
      else ledState = LOW;
      
      digitalWrite(ledPin, ledState);
    }
  }
}