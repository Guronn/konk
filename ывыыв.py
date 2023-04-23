import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import serial



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

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)

    while True:
        GPIO.output(22, GPIO.HIGH)
        time.sleep(3600)  # включаем светодиод на 1 час
        GPIO.output(22, GPIO.LOW)
        time.sleep(10800)  # выключаем светодиод на 3 часа

# включение/выключение моторчика

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

    co2Pin = A0


    # управление температурой

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

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)


    # управление освещением

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)

    while True:
        GPIO.output(22, GPIO.HIGH)
        time.sleep(3600)   # на 1 час
        GPIO.output(22, GPIO.LOW)






    sensor = Adafruit_DHT.DHT11
    pin = 4

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to read data from sensor')



  # python - m pip install pyserial надо будет скачать