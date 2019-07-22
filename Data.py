class Data:
    def __init__(self):
        self.__list=[]    # save the main infor
        self.__no_users=0
        file=open("data.txt", "r")
        #load the infor from file to list
        f1=file.readlines()
        for x in f1:
            list=["","","","",""]
            self.__changeToList(list, x)
            self.__list.append(list)
            self.__no_users= self.__no_users+1
        file.close()



    def __changeToList(self, list, x):
        count=0
        x=x.replace('\n','') # delete newline
        for i in x:
            if i=="|": count=count+1
            else: list[count]=list[count]+i

    def getList(self):
        return self.__list

    def getInfor(self, option, infor):
       for x in self.__list:
           if x[option]== infor:
               return x
       return []



    def addUser(self, SID,name, email, pin,uid):
        self.__no_users+=1
        self.__list.append([SID, name, email, pin,uid])
        self.__list.sort()
        self.__writeIntoFile()

    def checkUser(self, infor, option):
        #optionName=1 optionSID=0
        for i in self.__list:
            if i[option]==infor: return 1
        return 0

    def changePass(self, SID, pin ):
        for i in range(self.__no_users):
            if self.__list[i][0]==SID:
                self.__list[i][3]=pin
                break
        self.__writeIntoFile()

    def deleteUser(self, index):
        self.__list.remove(self.__list[index])
        self.__no_users=self.__no_users-1
        self.__writeIntoFile()

    def __writeIntoFile(self):
        file = open("data.txt", "w")
        file.write("")
        for i in range(self.__no_users):
            string_infor=self.__list[i][0]+"|"+self.__list[i][1]+"|"+self.__list[i][2]+"|"+self.__list[i][3]+"|"+self.__list[i][4]+"\n"
            file.write(string_infor)
        file.close()

