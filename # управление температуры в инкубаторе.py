# управление температуры в инкубаторе

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def turn_on():
    GPIO.output(18, GPIO.HIGH)

def turn_off():
    GPIO.output(18, GPIO.LOW)

while True:
    turn_on()
    time.sleep(60)
    turn_off()
    time.sleep(60)





# подключение DHT 11
    import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to read data from sensor')



# управление освещением

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

while True:
    GPIO.output(22, GPIO.HIGH)
    time.sleep(3600)  # включаем светодиод на 1 час
    GPIO.output(22, GPIO.LOW)
    time.sleep(10800)  # выключаем светодиод на 3 часа



# управление вентиляцией
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

def turn_on():
    GPIO.output(23, GPIO.HIGH)

def turn_off():
    GPIO.output(23, GPIO.LOW)

while True:
    turn_on()
    time.sleep(600)  # включаем моторчик на 10 минут
    turn_off()
    time.sleep(300)  # выключаем моторчик на 5 минут



# управление увлажнением

GPIO.setmode(GPIO.BCM)
GPIO.setup(8, GPIO.OUT)

def turn_on()
    GPIO.output(8, GPIO.HIGT)
    return(10000)

def turn_off()
    GPIO.output(8, GPIO.LOW)
    return(300000)




# управление насосом полива

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

def turn_on():
    GPIO.output(24, GPIO.HIGH)

def turn_off():
    GPIO.output(24, GPIO.LOW)

while True:
    turn_on()
    time.sleep(10)  # включаем насос на 10 секунд
    turn_off()
    time.sleep(600)  # выключаем насос на 10 минут


 управление датчико СО2

GPIO.setmode(GPIO.BCM)
GPIO.setup(   #???#,   GPIO.OUT)


import serial

ser = serial.Serial('/dev/ttyUSB0', 9600) # Подключение к последовательному порту

while True:
    data = ser.readline().decode('utf-8').rstrip() # Чтение строки из порта и удаление лишних символов
    print(data) # Вывод данных в консоль



 управление датчико СО2

GPIO.setmode(GPIO.BCM)
GPIO.setup(   #???#,   GPIO.OUT)


import serial

ser = serial.Serial('/dev/ttyUSB0', 9600) # Подключение к последовательному порту

while True:
    data = ser.readline().decode('utf-8').rstrip() # Чтение строки из порта и удаление лишних символов
    print(data) # Вывод данных в консоль



# Управление системой автоматического освещения
```
int lightSensorPin = A0;
int ledPin = 8;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int lightSensorValue = analogRead(lightSensorPin);
  Serial.print("Light sensor: ");
  Serial.println(lightSensorValue);

  if (lightSensorValue < 500) {
    digitalWrite(ledPin, HIGH);  // включаем светодиод, если освещенность ниже порога
  } else {
    digitalWrite(ledPin, LOW);  // выключаем светодиод
  }

  delay(1000);  // задержка 1 секунда
}
```


# Управление системой автоматического увлажнения

int humiditySensorPin = A0;
int relayPin = 8;

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int humiditySensorValue = analogRead(humiditySensorPin);
  Serial.print("Humidity sensor: ");
  Serial.println(humiditySensorValue);

  if (humiditySensorValue < 500) {
    digitalWrite(relayPin, HIGH);  // включаем увлажнитель, если влажность ниже порога
    delay(10000);  // включаем увлажнитель на 10 секунд
    digitalWrite(relayPin, LOW);  // выключаем увлажнитель
    delay(600000);  // задержка 10 минут
  } else {
    delay(1000);  // задержка 1 секунда
  }
}
```



# управление температурой

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

def turn_on():
    GPIO.output(18, GPIO.HIGH)

def turn_off():
    GPIO.output(18, GPIO.LOW)

while True:
    turn_on()
    time.sleep(60)
    turn_off()
    time.sleep(60)










# управление освещением

    import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

while True:
    GPIO.output(22, GPIO.HIGH)
    time.sleep(3600)  # включаем светодиод на 1 час
    GPIO.output(22, GPIO.LOW)



# ЭТО ХЗ ЧТО , ЧТО ТО С С++

humiditySensorPin = A0
relayPin = 8

def setup():
    pinMode(relayPin, OUTPUT)
    Serial.begin(9600)

def loop():
    humiditySensorValue = analogRead(humiditySensorPin)
    Serial.print("Humidity sensor: ")
    Serial.println(humiditySensorValue)

    if humiditySensorValue < 500:
        digitalWrite(relayPin, HIGH)
        delay(10000)
        digitalWrite(relayPin, LOW)
        delay(600000)
    else:
        delay(1000)

lightSensorPin = A0
ledPin = 8

def setup():
    pinMode(ledPin, OUTPUT)
    Serial.begin(9600)

def loop():
    lightSensorValue = analogRead(lightSensorPin)
    Serial.print("Light sensor: ")
    Serial.println(lightSensorValue)

    if lightSensorValue < 500:
        digitalWrite(ledPin, HIGH)
    else:
        digitalWrite(ledPin, LOW)

    delay(1000)

    
    
    # определение уровня воды
python
import RPi.GPIO as GPIO
import time

# Установка пина для чтения данных с датчика уровня воды
water_level_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(water_level_pin, GPIO.IN)

# Функция для определения уровня воды
def check_water_level():
    if GPIO.input(water_level_pin):
        print("Вода есть в баке")
    else:
        print("Бак пуст")

# Чтение уровня воды каждые 5 секунд
while True:
    check_water_level()
    time.sleep(5)




Для управления работы насоса в вертикальной ферме на языке Python следует использовать соответствующие библиотеки и модули, которые позволяют осуществлять связь с аппаратурой для управления ее функциями.

Например, для управления работой насоса можно использовать библиотеку RPi.GPIO, которая позволяет управлять GPIO-пинами на Raspberry Pi. Для этого следует подключить насос к GPIO-пину и написать соответствующий код на Python.

Пример кода для включения насоса на Raspberry Pi с использованием библиотеки RPi.GPIO:

```
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

GPIO.output(11, GPIO.LOW)

time.sleep(5)

GPIO.output(11, GPIO.HIGH)

GPIO.cleanup()
```

В данном примере насос подключен к пину 11, который настроен как выход. Сначала насос отключен (напряжение на пине равно нулю) на 5 секунд, затем включен (напряжение на пине установлено в 1). После этого выполняется очистка всех настроек.

В зависимости от конкретной аппаратуры и задачи управления, код может быть изменен и дополнен.
