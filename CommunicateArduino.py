import serial
import time


class SendToArduino:
    def __init__(self, port):
        string = "/dev/ttyACM"+port
        self.__ser = serial.Serial(string, baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
        self.__receiveInfor="b''"
        self.__UID=""


    def sendInfor(self, data):
        check=0
        self.__ser.write(data.encode('utf-8'))
        while check==0:
            print("waiting")
            self.__receiveInfor=self.__ser.readline();
            self.__receiveInfor=str(self.__receiveInfor)
            if self.__receiveInfor!="b''": check=1
            else: check =0
    
    def receiveInfor(self):
        self.__data=self.__ser.readline()
        self.__data=str(self.__data)
        if self.__data!="b''":
            self.__analyzeInfor()
        #print(data)
            
    def getUID(self):
        self.__UID=self.__receiveInfor[2:-5]
        return self.__UID
    
    
