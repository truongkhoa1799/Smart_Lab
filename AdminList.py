class AdminList:
    def __init__(self):
        self.__list=[]
        self.__no_admins=0
        file = open("AdminList.txt", "r")
        f1=file.readlines()
        for x in f1:
            x=x.replace("\n","")
            self.__list.append(x)
            self.__no_admins = self.__no_admins + 1
        file.close()

    def returnNoAdmins(self):
        return self.__no_admins

    def addAdmin(self,name):
        self.__no_admins=self.__no_admins+1
        self.__list.append(name)
        self.__writeBack()
    def get(self):
        print(self.__list)
    def checkAdmin(self, name):
        if name in self.__list: return 1
        else: return 0

    def __writeBack(self):
        file = open("AdminList.txt", "w")
        file.write("")
        for i in self.__list:
            infor = i +"\n"
            file.write(infor)
        file.close()

# pin=AdminList()
# pin.addAdmin("Admin1")
# pin.get()