import serial
import time
from tkinter import *


class SendToArduino:
    def __init__(self, port):
        string = "/dev/ttyACM"+port
        self.__ser = serial.Serial(string, baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
        self.__receiveInfor="b''"
        self.__UID=""
        self.__transmitData=""


    def sendInfor(self, data):
        # 1|name|pin for get infor
        # 3 for get id
        self.__transmitData=data
        check=0
        self.__ser.write(self.__transmitData.encode('utf-8'))
        while check==0:
            print("waiting")
            self.__receiveInfor=self.__ser.readline();
            self.__receiveInfor=str(self.__receiveInfor)
            if self.__receiveInfor!="b''": check=1
            else: check =0
        if self.__receiveInfor=="b'Fail to add\r\n'":
            return 0
        else: return 1
      


    def sendRequestUID(self):
        #3 is the ask for UID
        self.__ser.write("3")
        check=0
        while check==0:
            print("waiting")
            self.__receiveInfor= self.__ser.readline()
            self.__receiveInfor = str(self.__receiveInfor)
            if self.__receiveInfor != "b''":
                check = 1
            else:
                check = 0
            
    def getUID(self):
        self.__UID=self.__receiveInfor[2:-5]
        return self.__UID


    
    
