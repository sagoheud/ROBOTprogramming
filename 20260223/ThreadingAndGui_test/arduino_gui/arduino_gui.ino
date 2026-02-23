int led1 = 2; // Check1용 LED
int led2 = 3; // Check2용 LED

void setup() {
  Serial.begin(9600); // 파이썬 baudrate와 일치해야 함
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read(); // 파이썬에서 보낸 문자 읽기

    if (cmd == 'A') {
      digitalWrite(led1, HIGH); // LED1 켜기
    } 
    else if (cmd == 'B') {
      digitalWrite(led1, LOW);  // LED1 끄기
    } 
    else if (cmd == 'C') {
      digitalWrite(led2, HIGH); // LED2 켜기
    } 
    else if (cmd == 'D') {
      digitalWrite(led2, LOW);  // LED2 끄기
    }
  }
}