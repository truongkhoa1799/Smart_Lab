#list = name amount current

class Devices:
    def __init__(self):
        self.__list=[]
        self.__no_devices=0
        file = open("devices.txt", "r")
        f1=file.readlines()
        for x in f1:
            list=["","",""]
            self.__changeToList(list,x)
            self.__list.append(list)
            self.__no_devices+=1
        file.close()
    def __changeToList(self, list,infor):
        count = 0
        infor = infor.replace('\n', '')  # delete newline
        for i in infor:
            if i == "|":
                count = count + 1
            else:
                list[count] = list[count] + i

    def addDevices(self, name, amount):
        check=0
        for i in range(self.__no_devices):
            if self.__list[i][0]==name:
                int_amount=int(self.__list[i][1])+ int(amount)
                self.__list[i][1]=str(int_amount)
                int_current= int(self.__list[i][2])+int(amount)
                self.__list[i][2]= str(int_current)
                check=1
                break
        if check==0:
            list=[name,amount, amount]
            self.__no_devices+=1
            self.__list.append(list)
        self.__list.sort()
        self.__writeFile()

    def __writeFile(self):
        file=open("devices.txt","w")
        file.write("")
        for x in self.__list:
            infor = x[0]+"|"+x[1]+"|"+x[2]+'\n'
            file.write(infor)
        file.close()

    def getList(self):
        return self.__list

    def deteleDevices(self, index, amount):
        int_amount= int(self.__list[index][1])
        if int_amount==amount:
            self.__list.remove(self.__list[index])
        else:
            self.__list[index][1]=  str(int(self.__list[index][1])-amount)
            self.__list[index][2] = str(int(self.__list[index][2]) - amount)
        self.__writeFile()

    def getCurrent(self, index):
        return int(self.__list[index][2])

    def getNoDevices(self):
        return self.__no_devices

    def getNameWithIndex(self, index):
        return self.__list[index][0]
