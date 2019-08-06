class PinList:
    def __init__(self):
        self.__list={}
        self.__no_users=0
        file = open("PinList.txt", "r")
        f1=file.readlines()
        for x in f1:
            x=x.replace("\n","")
            # ID number | pin
            id, pin= self.__change(x)
            self.__list[id]=pin
            self.__no_users = self.__no_users + 1
        file.close()
    def __change(self, x):
        array=["",""]
        count =0
        for i in x:
            if i!="|": array[count]=array[count]+i
            else : count= count+1
        return array[0], array[1]

    def get(self):
        print(self.__list)

    def addPin(self, id , pin):
        self.__list[id]=pin
        self.__no_users=self.__no_users+1
        self.__writeBack()
    def changePin(self, id, pin):
        self.addPin(id, pin)
    def __writeBack(self):
        file = open("PinList.txt", "w")
        file.write("")
        for i in self.__list:
            infor = i +"|"+ self.__list[i]+"|"+"\n"
            file.write(infor)
        file.close()
    def checkPinwithID(self, id,pin):
        if self.__list[id]==pin: return 1
        else: return 0

# pin=PinList()
# pin.addPin("1752222","1234")
# pin.get()