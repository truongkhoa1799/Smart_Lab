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
        self.__transmitData=data
        self.__root = Tk()
        canvas = Canvas(self.__root, height=100, width=100)
        canvas.pack()
        insert= Button(self.__root, text="Insert your card", command=self.__insertCardAdd)
        insert.place(relx=0, rely=0, relheight=0.5, relwidth=1)
        
        close=Button(self.__root, text="close",  command=self.__closeInsertCardAdd)
        close.place(relx=0, rely=0.5, relheight=0.5, relwidth=1)
        self.__root.mainloop()
        
    def __insertCardAdd(self):
        check=0
        self.__ser.write(self.__transmitData.encode('utf-8'))
        while check==0:
            print("waiting")
            self.__receiveInfor=self.__ser.readline();
            self.__receiveInfor=str(self.__receiveInfor)
            if self.__receiveInfor!="b''": check=1
            else: check =0
            
    def __closeInsertCardAdd(self):
         self.__root.destroy()
    
    def receiveInfor(self):
        self.__data=self.__ser.readline()
        self.__data=str(self.__data)
        if self.__data!="b''":
            self.__analyzeInfor()
        #print(data)
            
    def getUID(self):
        self.__UID=self.__receiveInfor[2:-5]
        return self.__UID
    
    
