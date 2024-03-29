from AccountStatus import AccountStatus
class Data:
    def __init__(self):
        self.__list={}    # save the main infor
        self.__no_users=0
        self.__arrayKey=["Name","Gender","ID number","Email","UID","RFID UID"]
        file=open("data.txt", "r")
        #load the infor from file to list
        f1=file.readlines()
        for x in f1:
            #  Name | Gender | ID number | Email | UID | RFID UID | Pin | password
            list={}
            self.__changeToList(list, x)
            self.__list[list.get("ID number")]=list
            self.__no_users= self.__no_users+1
        file.close()



    def __changeToList(self, list, x):
        count=0
        str=""
        x=x.replace('\n','') # delete newline
        for i in x:
            if i != "|":
                str=str+i
            elif i=="|":
                list[self.__arrayKey[count]]=str
                str=""
                count=count+1

    def getList(self):
        return self.__list

    def getInforWithID(self, infor):
        if infor in self.__list:
            return 1,self.__list[infor]
        else: return 0,""

    def get(self):
        return self.__list

    def getUID(self, ID):
        return self.__list[ID].get("UID")


    def addUser(self, list):
        self.__no_users+=1
        self.__list[list.get("ID number")]=list
        self.__writeIntoFile()

    def checkID(self, infor):
        if infor in self.__list:
            return 1
        else: return 0



    def deleteUser(self, infor):
        account= AccountStatus()
        account.Deactive(infor)

    def getIDWithRFID_UID(self, RFID_UID):
        for i in self.__list:
            if self.__list[i]["RFID UID"]==RFID_UID:
                return i
        return 0

    def checkRFID_UID(self,RFID_UID):
        for i in self.__list:
            if self.__list[i]["RFID UID"]==RFID_UID:
                return 1
        return 0

    def checkExist(self, id ):
        if id in self.__list: return 1
        else: return 0
    
    def getUIDWithID(self,id):
        if self.checkExist(id)==0: return 0
        else:
            return self.__list[id]["UID"]

    def __writeIntoFile(self):
        file = open("data.txt", "w")
        file.write("")
        for i in self.__list:
            str=self.__list[i].get("Name")+"|"+self.__list[i].get("Gender")+"|"+self.__list[i].get("ID number")+"|"+self.__list[i].get("Email")+"|"+self.__list[i].get("UID")+"|"+self.__list[i].get("RFID UID")+"|"+"\n"
            file.write(str)
        file.close()


