from CommunicateArduino import SendToArduino
from PinList import PinList
from Data import Data
from AccountStatus import AccountStatus
from firebaseAPI import MyFirebase


communicate = SendToArduino("ACM0")

def analyzeInforForAccess(string):
    string=string+"|"
    count=0
    array=["","","",""]
    for i in string:
        if i!="|":
            array[count]=array[count]+i
        else: count= count+1
    return array[1],array[2], array[3]

def Receive():
    count=0
    while True:
        #checkInfor=1 co signal
        checkInfor,infor=communicate.receiveInforFromArduino()
        print(infor)
        if checkInfor ==1 and infor[0]=="4":
            RFID_UID,id, pin= analyzeInforForAccess(infor)
            id=id[0:7]
            pin=pin[0:4]
            uid=data.getUIDWithID(id)
            print(RFID_UID,uid, id,pin)                                                                                                      
            checkPin=pinList.checkPinWithUID(uid,pin)
            accountStatus= AccountStatus()
            checkStatus=accountStatus.getStatus(id)
            if checkPin==1 and checkStatus=="ACTIVE":
                communicate.sendResultForAccess("4|ACCEPT")
            elif checkPin==0 and checkStatus=="ACTIVE": 
                communicate.sendResultForAccess("4|WRONG PIN")
            elif checkPin==1 and checkStatus=="DEACTIVE":
                communicate.sendResultForAccess("4|DEACTIVE")
            elif uid==0: communicate.sendResultForAccess("4|NOTEXIST")
        elif checkInfor==1 and infor[0]=="5":
            count=count+1
            print("in",count)
            communicate.sendResultForAccess("5|"+str(count))
        elif checkInfor==1 and infor[0]=="6":
            if count>0:
                count=count-1
                print("out",count)
                communicate.sendResultForAccess("5|"+str(count))
            
    time.sleep(0.4)
    
database = MyFirebase("doorsystem@gmail.com", "1234123")
account=AccountStatus()
data = Data()
pinList=PinList()
if __name__=="__main__":
    Receive()