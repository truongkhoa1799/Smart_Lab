class BorrowedList:
    def __init__(self):
        self.__list={}
        id_list={}
        # Name Device | ID number | Date Rent | Date Back |
        self.__arrayKey=["ID number","Date Rent","Date Back","Amount"]
        file= open("borrowedList.txt","r")
        f1=file.readlines()
        pre_name= self.__getNameDevices(f1[0])
        if pre_name!="close":
            for x in f1:
                name=self.__getNameDevices(x)
                temp_list = {}
                self.__changeToList(temp_list, x)
                if name==pre_name:
                    id_list[temp_list["ID number"]]=temp_list
                elif name!= pre_name and x!="close":
                    self.__list[pre_name]=id_list
                    id_list={}
                    id_list[temp_list["ID number"]] = temp_list
                elif name=="close":
                    self.__list[pre_name] = id_list
                    id_list = {}

                pre_name=name

        file.close()

    def __getNameDevices(self,str):
        name=""
        for i in str:
            if i!="|": name=name+i
            else: break
        return name

    def __changeToList(self,temp_list,x):
        x=x.replace('\n','')
        str=""
        count=-1
        for i in x:
            if i!="|" and count!=-1:
                str=str+i
            elif i=="|" and count!=-1:
                temp_list[self.__arrayKey[count]]=str
                str=""
                count=count+1
            elif i=="|" and count==-1:
                count=count+1

    def getList(self, name):
        return self.__list[name]

    def __writeBack(self):
        file = open("borrowedList.txt", "w")
        file.write("")
        for i in self.__list:
            name=i
            list={}
            for x in self.__list[i]:
                id=x
                date_rent=self.__list[i][x]["Date Rent"]
                date_back=self.__list[i][x]["Date Back"]
                amount=self.__list[i][x]["Amount"]
                str=name+"|"+id+"|"+date_rent+"|"+date_back+"|"+amount+"|"+'\n'
                file.write(str)
        file.write("close")
        file.close()

    def showInfor(self):
        print(self.__list)

    def checkExitList(self,name):
        if name in self.__list: return 1
        else: return 0

    def get(self):
        return self.__list

    def addBorrowedList(self, name, id, date_rent, date_back,amount):
        list={}
        list["Date Rent"]=date_rent
        list["Date Back"] = date_back
        list["ID number"] = id
        list["Amount"]=amount
        if name in self.__list:
            if id in self.__list[name]:
                new_amount=int(amount)+int(self.__list[name][id]["Amount"])
                list["Date Rent"]=self.__list[name][id]["Date Rent"]
                list["Amount"]=str(new_amount)
                self.__list[name][id]=list
            else:
                self.__list[name][id]={}
                self.__list[name][id]=list
        else:
            self.__list[name]={}
            self.__list[name][id]={}
            self.__list[name][id]=list
        self.__writeBack()

    def getListWithName(self,name):
        return self.__list[name]

    def getInforWithNameAndID(self, name, id):
        if name in self.__list:
            if id in self.__list[name]:
                return self.__list[name][id]
            else: return 0
        else: return 0

    def returnDevices(self, name, id):
        amount= self.__list[name][id]["Amount"]
        self.__list[name].pop(id)
        self.__writeBack()
        return int(amount)

# bl=BorrowedList()
# #bl.addBorrowedList("khoa1","1752297","12-12-2312","12-12-2321","20")
# print(bl.get())
