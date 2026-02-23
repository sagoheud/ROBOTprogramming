#include <SoftwareSerial.h>
#include <DHT.h>
#include <Wire.h> // 2C 통신을 위한 핀이 A4 (SDA), A5 (SCL)
#include <LiquidCrystal_I2C.h>

#define DHTPIN 4 // 온습도 센서 핀 4번
#define DHTTYPE DHT11 // 원본의 DHT//를 DHT11로 수정

DHT dht(DHTPIN, DHTTYPE);
SoftwareSerial HC06(2, 3); // RX, TX
LiquidCrystal_I2C lcd(0x27, 16, 2);
float temp = 0; float humi = 0;

void setup() {
  Serial.begin(9600);
  HC06.begin(9600);
  dht.begin();
  
  lcd.init();
  lcd.backlight();
  
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  // LCD 출력 및 초기화
  lcd.clear();
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  String data = String(t) + "," + String(h);
  HC06.println(data);
  Serial.print(h);
  lcd.setCursor(2, 0);
  lcd.print("temp: ");
  lcd.print(t);
  lcd.setCursor(2, 1);
  lcd.print("humi: ");
  lcd.print(h);
  Serial.print(",");
  Serial.println(t);
  delay(1000);

  // 블루투스 제어 명령 수신
  if (HC06.available() > 0) {
    unsigned char data = HC06.read();
    Serial.print("Received: ");
    Serial.println(data);
    switch (data) {
      case 1: // 빨간불 ON
        digitalWrite(6, HIGH);
        break;
      case 2: // 녹색불 ON
        digitalWrite(7, HIGH);
        break;
      case 3: // 파란불 ON
        digitalWrite(8, HIGH);
        break;
      case 4: // 모든 LED OFF
        digitalWrite(6, LOW);
        digitalWrite(7, LOW);
        digitalWrite(8, LOW);
        break;
      case 5: // 모터 작동
        digitalWrite(9, HIGH);
        digitalWrite(10, LOW);
        break;
      case 6: // 모터 정지
        digitalWrite(9, LOW);
        digitalWrite(10, LOW);
        break;
    }
  }
}