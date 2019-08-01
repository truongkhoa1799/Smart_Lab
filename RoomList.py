class RoomList:
    def __init__(self):
        self.__list=[]
        self.__no_rooms=0
        file = open("RoomList.txt", "r")
        f1=file.readlines()
        for x in f1:
            x=x.replace("\n","")
            #  Name | Total | Remained
            self.__list.append(x)
            self.__no_rooms = self.__no_rooms + 1
        file.close()

    def __writeBack(self):
        file = open("RoomList.txt", "w")
        file.write("")
        for i in self.__list:
            infor=i+"\n"
            file.write(infor)
        file.close()

    def checkExistRoom(self, name):
        if name in self.__list: return 1
        else: return 0
    def addRoom(self, name):
        if self.checkExistRoom(name)==0:
            self.__list.append(name)
            self.__list.sort()
            self.__writeBack()
            return 1
        else: return 0
    def getRoom(self):
        return self.__list

# room=RoomList()
# room.addRoom("C5_201")
# print(room.getRoom())
