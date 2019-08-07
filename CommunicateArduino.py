import serial
import time
from tkinter import *


class SendToArduino:
    def __init__(self, port):
        string = "/dev/tty"+port
        self.__ser = serial.Serial(string, baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
        self.__receiveInfor="b''"
        self.__UID=""
        self.__transmitData=""


    def sendInfor(self, data):
        # 1|name|pin for get infor
        # 3 for get id
        transmitData=data
        print(transmitData)
        check=0
        count=0
        if data[0]=="1":self.__ser.write(transmitData.encode('utf-8'))
        
        while check==0 and count<10:
            print("waiting")
            self.__receiveInfor=self.__ser.readline();
            self.__receiveInfor=str(self.__receiveInfor)
            if self.__receiveInfor!="b''": check=1
            else: check=0
            count=count+1
            
        print(self.__receiveInfor)
        
        if count==10:
            self.__receiveInfor = "b''"
            return 3
        elif self.__receiveInfor[2:-5]=="Fail":
            self.__receiveInfor="b''"
            return 0
        elif self.__receiveInfor[2:-5]=="USED TAG":
            self.__receiveInfor="b''"
            return 2
        else:
            self.__UID=self.__receiveInfor[2:-5]
            self.__receiveInfor="b''"
            return 1
      
    def sendResultForAccess(self, result):
        transmitData = result
        self.__ser.write(transmitData.encode('utf-8'))

    def sendRequestUID(self):
        #3 is the ask for UID
        transmitData="3"
        self.__ser.write(transmitData.encode('utf-8'))
        check=0
        count=0
        while check==0 and count<10:
            print("waiting")
            self.__receiveInfor= self.__ser.readline()
            self.__receiveInfor = str(self.__receiveInfor)
            if self.__receiveInfor != "b''":
                check = 1
            else:
                check = 0
            count=count+1
        if count==10:
            self.__receiveInfor="b''"
            return 2
        elif self.__receiveInfor[2:-5]=="Fail":
            self.__receiveInfor="b''"
            return 0
        else:
            self.__UID=self.__receiveInfor[2:-5]
            self.__receiveInfor="b''"
            return 1
            
    def getUID(self):
        return self.__UID
    
    def receiveInforFromArduino(self):
        print("waiting")
        self.__infor_access=self.__ser.readline()
        self.__infor_access = str(self.__infor_access)
        if self.__infor_access=="b''": return 0,""
        else: return 1,self.__infor_access[2:-5]
    
   
    def Print(self):
        print("open")

    
    
