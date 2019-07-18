import serial
import time


class SendToArduino:
    def __init__(self, port):
        string = "/dev/ttyACM"+port
        #self.__ser = serial.Serial(string, baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)


    def sendInfor(self, data):
       # self.__ser.write(data.encode('utf-8'))
        print(data)

