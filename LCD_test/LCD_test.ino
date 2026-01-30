#include <Wire.h> // I2C 통신을 위한 핀이 A4 (SDA), A5 (SCL)
#include <LiquidCrystal_I2C.h> // LiquidCrystal I2C 라이브러리 설치
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup()
{
  lcd.init();
  lcd.backlight();
  Serial.begin(9600);
}

void loop()
{
  lcd.print("cursor on_blink"); lcd.cursor(); lcd.blink(); delay(1000); lcd.clear(); // 화면 글자 출력
  lcd.print("cursor off     ");
  lcd.noCursor(); lcd.noBlink(); delay(1000); lcd.clear(); lcd.print("count up"); delay(1000); lcd.clear();
  
  for (int k = 0; k < 10; k++)
  {
    lcd.home(); lcd.print("no : "); lcd.print(k); delay(500); lcd.clear(); // no : 0 ~ no : 9 까지 화면 출력
  }
  
  lcd.print("hello");
  for (int k = 0; k < 3; k++)
  {
    lcd.noDisplay(); delay(500); lcd.display(); delay(500); // 헬로우 3번 온오프 출력
  }
  
  lcd.clear(); lcd.setCursor(6, 0); lcd.print("hello ");
  for (int k = 0; k < 3; k++)
  {
    lcd.scrollDisplayRight(); delay(500); // 헬로우 출력 후 오른쪽 이동
  }
  
  lcd.clear(); lcd.setCursor(6, 0); lcd.print("hello ");
  for (int k = 0; k < 3; k++)
  {
    lcd.scrollDisplayLeft(); delay(500); // 헬로우 출력 후 왼쪽 이동
  }
  
  lcd.clear();
  lcd.print("12345");
  for (int k = 0; k < 16; k++)
  {
    lcd.scrollDisplayRight(); delay(200); // 왼쪽 위부터 12345 출력 후 오른쪽 이동
  }
  
  lcd.clear(); lcd.setCursor(16, 1); lcd.print("67890");
  for (int k = 0; k < 16; k++)
  {
    lcd.scrollDisplayLeft(); delay(200); // 오른쪽 아래부터 67890 출력 후 왼쪽 이동
  }
  
  lcd.clear();
}