from datetime import date, datetime, timezone,time
import math

#number of tiet / week =84
#=> week 3 has index of tiet= 84(tiet)+1
ROOT = datetime(year = 2019, month= 7, day=29, hour=6)
timeStampRoot= datetime.timestamp(ROOT)





class Room:
    def __init__(self):
        self.__list={}
        self.__list["Classes"]={}
        self.__list["Course detail"]={}
        file = open("Room.txt", "r")
        f1 = file.readlines()
        for x in f1:
            list={}
            #  Name | Total | Remained |
            start, end, lecturer, room, date, course= self.__changeInfor(x)
            day, month, year= self.__changeDate(date)
            list["Lecturer"]= lecturer
            list["Course"]= course
            list["Start"]= start
            list["End"]= end
            list["Room"]= room
            list["Date"]=date
            if room not in self.__list["Classes"]:
                self.__list["Classes"][room]=[0]*4033
                self.__list["Course detail"][room]={}
            reference = self.__determineIndex(int(start), int(day), int(month), int(year))
            list["Reference"]=reference
            #print(list)
            for i in range(int(start), int(end)+1,1):
                index = self.__determineIndex(i, int(day), int(month), int(year))
                self.__list["Classes"][room][index]=reference
            self.__list["Course detail"][room][reference]=list
        file.close()

    def __changeDate(self, string):
        string=string+"-"
        count=0
        array=["","",""]
        for i in string:
            if i !="-":
                array[count]=array[count]+i
            else: count= count+1
        return array[0], array[1], array[2]

    def __determineIndex(self,tiet,day, month, year):
        hour= tiet + 5
        now = datetime(year =year, month= month, day=day, hour=hour)
        timeStampNow = datetime.timestamp(now)
        diff = timeStampNow - timeStampRoot
        days= math.floor(diff / 86400)
        diff= diff - days*(43200)
        index= math.floor(diff/3600)
        return index+1

    def __changeInfor(self, x):
        x= x.replace("\n","")
        array=["","","","","",""]
        count=0
        for i in x:
            if i!="|":
                array[count]=array[count]+i
            else:
                count=count+1
        return array[4], array[5], array[1], array[0], array[3], array[2]

    def getList(self):
        return self.__list

    def __writeBack(self):
        file = open("Room.txt", "w")
        file.write("")
        for i in self.__list["Course detail"]:
            for j in self.__list["Course detail"][i]:
                room = i
                lecturer = self.__list["Course detail"][i][j]["Lecturer"]
                course = self.__list["Course detail"][i][j].get("Course")
                date = self.__list["Course detail"][i][j].get("Date")
                start = self.__list["Course detail"][i][j].get("Start")
                end = self.__list["Course detail"][i][j].get("End")
                infor = room + "|" + lecturer + "|" +course + "|"  +date + "|" +start + "|" +end + "|"+'\n'
                file.write(infor)
        file.close()

    def add(self, room, lecturer, course, date, start, end):
        day, month, year = self.__changeDate(date)
        index = self.__determineIndex(int(start), int(day), int(month), int(year))
        if room not in self.__list["Classes"]:
            self.__list["Classes"][room]=[0]*4033
            self.__list["Course detail"][room] = {}

        if self.__list["Classes"][room][index]!=1:
            list={}
            list["Lecturer"] = lecturer
            list["Course"] = course
            list["Start"] = start
            list["End"] = end
            list["Room"] = room
            list["Date"] = date
            reference = self.__determineIndex(int(start), int(day), int(month), int(year))
            list["Reference"] = reference
            # print(list)
            for i in range(int(start), int(end) + 1, 1):
                index = self.__determineIndex(i, int(day), int(month), int(year))
                self.__list["Classes"][room][index] = reference
            self.__list["Course detail"][room][reference] = list
            self.__writeBack()
            return 1
        else: return 0


    def __changeToWeek(self,day, month, year):
        now = datetime(year=year, month=month, day=day, hour=6)
        timeStampNow=datetime.timestamp(now)
        diff=timeStampNow-timeStampRoot
        no_weeks=math.floor(diff/604800)
        return (no_weeks)

    def check(self, room, tiet, day, month, year):
        #tiet is integer
        index = self.__determineIndex(tiet,day, month, year)
        if self.__list["Classes"][room][index]==0: return 1
        else: return 0
        #1 co 0 khong co
    def determineStartAndendofWeekWith(self, day, month, year):
        week= self.__changeToWeek(day,month,year)
        start=84*week+1
        end=84*(week+1)
        return start, end
    def getCourseDetailWithRoomAndStartEnd(self,start,end,Room):
        list=[]
        list.append("")
        count=0
        #print(start, end, Room)
        for i in range(start,end+1):
            count=count+1
            list.append("")
            index=self.__list["Classes"][Room][i]
            if index in self.__list["Course detail"][Room]:
                print(index)
                list[count]=self.__list["Course detail"][Room][index]
            else:
                temp={}
                temp["Lecturer"]=""
                temp["Course"]=""
                list[count]=temp
        return list
    def getDetailOfWeek(self, day, month, year):
        week=self.__changeToWeek(day, month, year)
        timeStampStart= week * 604800 +  timeStampRoot
        start= datetime.fromtimestamp(timeStampStart)
        timeStampEnd=timeStampStart+518400
        end=datetime.fromtimestamp(timeStampEnd)
        string_start=str(start.date())
        string_end=str(end.date())
        return week,string_start, string_end
        #return week,startWeek, endWeek




# room= Room()
# print(room.getDetailOfWeek(21,8,2019))
# print(room.add("C5_202","Thien","Programming","02-08-2019","4","6"))
# print(room.getList())


