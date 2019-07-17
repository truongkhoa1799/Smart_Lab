class BorrowedList:
    def __init__(self):
        self.__list={}
        file= open("borrowedList.txt","r")
        f1=file.readlines()
        sub_list = ["", "", ""]
        list = []
        pre_index=self.__changeToList(f1[0],sub_list)
        for x in f1:
            sub_list = ["", "", ""]
            index=self.__changeToList(x, sub_list)
            if pre_index!=index:
                self.__list[pre_index]=list
                list=[]
                list.append(sub_list)
            else:list.append(sub_list)
            pre_index=index
        file.close()

    def __addCloseToEndFile(self):
        file = open("data.txt", "a")
        file.write("close")
        file.close()

    def __changeToList(self, x, sub_list):
        x=x.replace('\n','')
        index=""
        count=-1
        for i in x:
            if i=='|':
                count+=1
            elif count==-1 and i!='|':
                index=index+i
            elif i!='|' and count>=0:
                sub_list[count]=sub_list[count]+i
        return index

    def getList(self, name):
        return self.__list[name]

    def showInfor(self):
        print(self.__list)

    def checkExitList(self,name):
        return self.__list.has_key(name)




