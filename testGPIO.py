import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial("/dev/ttyACM0",baudrate = 9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1)


def blink (pin):
          GPIO.output(pin,GPIO.HIGH)
          time.sleep(1)
          GPIO.output(pin,GPIO.LOW)
          time.sleep(1)
          return
          
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

while True:
    data = "hello"
    ser.write(data.encode('utf-8'))
    print("write")
    temp = ser.readline()
    time.sleep(1)