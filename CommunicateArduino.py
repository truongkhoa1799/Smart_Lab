import serial
import time


class SendToArduino:
    def __init__(self, port):
        string = "/dev/ttyACM"+port
        self.__ser = serial.Serial(string, baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
        self.__UID=""


    def sendInfor(self, data):
        self.__ser.write(data.encode('utf-8'))
        print(data)
    
    def receiveInfor(self):
        self.__data=self.__ser.readline()
        self.__data=str(self.__data)
        if self.__data!="b''":
            self.__analyzeInfor()
        #print(data)
    def __analyzeInfor(self):
        if self.__data[2]=="1":
            self.__UID=self.__data[4:-5]
            print(self.__UID)
            
    def getUID(self):
        return self.__UID
    
    
