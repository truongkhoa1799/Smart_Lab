class AccountStatus:
    def __init__(self):
        self.__list = {}
        file = open("accountStatus.txt", "r")
        f1 = file.readlines()
        for x in f1:
            list=["",""]
            self.__changeToList(x, list)
            self.__list[list[0]]=list[1]
        file.close()
    def __changeToList(self, x, list):
        count =0
        x=x.replace('\n','')
        for i in x:
            if i!="|":
                list[count]=list[count]+i
            elif i=="|":
                count=count+1

    def Deactive(self, infor):
        self.__list[infor]="DEACTIVE"
        self.__writeFile()

    def Active(self, infor):
        self.__list[infor]="ACTIVE"
        self.__writeFile()

    def __writeFile(self):
        file = open("accountStatus.txt", "w")
        file.write("")
        for x in self.__list:
            infor = x+"|"+self.__list[x] + '\n'
            file.write(infor)
        file.close()

    def addUser(self, infor):
        self.__list[infor]="ACTIVE"
        self.__writeFile()

    def getStatus(self, ID):
        if ID in self.__list:
            return self.__list[ID]
        else: return 0


