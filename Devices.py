#list = name amount current

class Devices:
    def __init__(self):
        self.__list={}
        self.__no_devices=0
        self.__arrayKey=["Name","Total","Remained"]
        file = open("devices.txt", "r")
        f1=file.readlines()
        for x in f1:
            #  Name | Total | Remained |
            list = {}
            self.__changeToList(list, x)
            self.__list[list.get("Name")] = list
            self.__no_devices = self.__no_devices + 1
        file.close()
    def __changeToList(self, list,x):
        count = 0
        temp=""
        x = x.replace('\n', '')  # delete newline
        for i in x:
            if i != "|":
                temp=temp+i
            else:
                list[self.__arrayKey[count]] = temp
                temp=""
                count = count +1

    def addDevices(self, list):
        self.__list[list["Name"]]=list
        self.__writeFile()
        self.__no_devices=self.__no_devices+1

    def updateTotalRemained(self, list):
        total = int(list["Total"])
        remained = int(list["Remained"])

        total_list = int(self.__list[list["Name"]].get("Total"))
        remained_list = int(self.__list[list["Name"]].get("Remained"))

        list["Total"] = str(total + total_list)
        list["Remained"] = str(remained + remained_list)
        return list

    def __writeFile(self):
        file=open("devices.txt","w")
        file.write("")
        for i in self.__list:
            name= self.__list[i].get("Name")
            total = self.__list[i].get("Total")
            remained = self.__list[i].get("Remained")
            infor = name+"|"+total+"|"+remained+"|"+'\n'
            file.write(infor)
        file.close()

    def getList(self):
        return self.__list


    def getCurrent(self, name):
        return int(self.__list[name]["Remained"])

    def getNoDevices(self):
        return self.__no_devices

    def checkExistdevices(self, name):
        if name in self.__list: return 1
        else: return 0

    def checkAmount(self, amount,name):
        current_amount= int(self.__list[name]["Remained"])
        if amount<=current_amount: return 1
        else: return 0

    def rentDevice(self,name, amount):
        afterRentAmount= int(self.__list[name]["Remained"])-amount
        self.__list[name]["Remained"]=str(afterRentAmount)
        self.__writeFile()
    def getListDEviceAFterRent(self, name, amount):
        list={}
        list["Name"]=name
        afterRentAmount = int(self.__list[name]["Remained"]) - amount
        list["Remained"] = str(afterRentAmount)
        list["Total"]=self.__list[name]["Total"]
        return list
    def getListDEviceAFterReturn(self, name, amount):
        list={}
        list["Name"]=name
        afterRentAmount = int(self.__list[name]["Remained"]) + amount
        list["Remained"] = str(afterRentAmount)
        list["Total"]=self.__list[name]["Total"]
        return list
    def getInforWithName(self, name):
        return self.__list[name]

    def returnDevice(self, name,amount):
        self.__list[name]["Remained"]=str(int(self.__list[name]["Remained"])+amount)
        self.__writeFile()



