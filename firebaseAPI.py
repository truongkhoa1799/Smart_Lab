import pyrebase
import time
from datetime import datetime

labScheduleList = {
    "Classes": {
        "C5_202": [0] * 4032,
        "C6_101": [0] * 4032
    },
    "Courses detail": {
        "C5_202": {
            "31": {
                "Lecturer": "Pham Hoang Anh",
                "Course": "Fundamental programming",
                "Start": 7,
                "End": 9,
                "Reference": 24,
                "Room": "C5_202",
                "Date": "31/12/2019"
            }
        },
        "C6_101": {
            "31": {
                "Lecturer": "Pham Hoang Anh",
                "Course": "Fundamental programming",
                "Start": 7,
                "End": 9,
                "Reference": 24,
                "Room": "C6_101",
                "Date": "31/12/2019"
            }
        }
    }
}

i = 31
while i <= 33:
    labScheduleList["Classes"]["C5_202"][i] = 31
    labScheduleList["Classes"]["C6_101"][i] = 31
    i += 1


labStatusList = {
    "C5_202": {
        "Room": "C5_202",
        "Status": "Closed"
    },
    "C6_101": {
        "Room": "C6_101",
        "Status": "Opened"
    },
}

userList = {
    1710364: {
        "Name": "Ngo Duc Tuan",
        "Gender": "male",
        "ID number": "1710364",
        "Email": "tuan.ngo1999@hcmut.edu.vn",
        "UID": "1n3ud914d12e1",
        "RFID UID": "00 c2 02 13",
    }
}

deviceList = {
    "Esp8266": {
        "Name": "Esp8266",
        "Total": 20,
        "Remained": 10
    },
    "Arduino R3": {
        "Name": "Arduino R3",
        "Total": 10,
        "Remained": 10
    }
}

loginHistoryList = {
    "C5_202": [
        {
            "Time": "1564485226",
            "Type": 1710364
        },
        {
            "Time": "1564485229",
            "Type": "Admin"
        }
    ],
    "C6_101": [

    ]

}

def encodeString(email):
    return email.replace('.', ',')

def decodeString(email):
    return email.replace(',', '.')

class MyFirebase:
    __config = {
        "apiKey": "AIzaSyBL5HM4QTaN7GGG6bgAfx8YhPLMP_KFylc",
        "authDomain": "smart-lab-9b1c1.firebaseapp.com",
        "databaseURL": "https://smart-lab-9b1c1.firebaseio.com/",
        "storageBucket": "smart-lab-9b1c1.appspot.com",
    }

    checkAdmin = False

    def __init__(self, adminAcc, adminPass):
        self.firebase = pyrebase.initialize_app(self.__config)
        self.auth = self.firebase.auth()
        try:
            self.admin = self.auth.sign_in_with_email_and_password(adminAcc, adminPass)
            self.checkAdmin = True
            self.refDB = self.firebase.database()
            self.__admin_info = self.auth.get_account_info(self.admin['idToken'])
            self.__pushLoginHistory("Admin", "C5_202")
            print("Successful to authenticate to Firebase as Admin")
        except Exception as e:
            print("Failed to authenticate to Firebase as Admin")
            print(e)

    def formatFirebase(self):
        return True

    def addUser(self, userData, isAdmin = False):
        if self.checkAdmin is False:
            print("Add user failed")
            return False, None, None
        try:
            newUser = self.auth.create_user_with_email_and_password(userData['Email'], userData['Password'])
            uid = self.auth.get_account_info(newUser['idToken'])['users'][0]['localId']
            userData['UID'] = uid
            if "Password" in userData:
                del userData["Password"]
            strPIN = userData['PIN']
            del userData["PIN"]
            self.refDB.child("List PINs").child(userData['UID']).set(strPIN, self.admin['idToken'])
            self.refDB.child("List of users").child(userData['ID number']).set(userData, self.admin['idToken'])
            self.refDB.child("Allowed UIDs").child(userData['UID']).set({"Status": 'true', "ID number": str(userData['ID number'])}, self.admin['idToken'])
            if isAdmin == True:
                self.refDB.child("Admin Key").child(uid).set("true", self.admin['idToken'])
                print("Add admin successful")
                return True, userData, strPIN
            print("Add user successful")
            return True, userData, strPIN
        except Exception as e:
            print("Add user failed")
            print(e)
            return False, None, None

    def activateUser(self, uid):
        if self.checkAdmin is False:
            print("Activate failed")
            return False
        try:
            self.refDB.child("Allowed UIDs").child(uid).child("Status").set("true", self.admin['idToken'])
            print("Activate user successful")
            return True
        except Exception as e:
            print("Activate user failed")
            print(e)
            return False

    def deactivateUser(self, uid):
        if self.checkAdmin is False:
            print("Deactivate failed")
            return False
        try:
            self.refDB.child("Allowed UIDs").child(uid).child("Status").set('false', self.admin['idToken'])
            print("Deactivate user successful")
            return True
        except Exception as e:
            print("Deactivate user failed")
            print(e)
            return False

    def checkTypeLogin(self, uid):
        if self.checkAdmin is False:
            print("Check failed")
            return -1
        else:
            try:
                checkIsAdmin = self.refDB.child("Allowed UIDs").child(uid).get(self.admin['idToken'])
                print(checkIsAdmin.val())
                if "Admin" in checkIsAdmin.val()["ID number"]:
                    print("Check successful")
                    return 1
                if checkIsAdmin.val()["Status"] == "true":
                    print("Check successful")
                    return 2
                print("Check successful")
                return 3
            except Exception as e:
                print("Check failed")
                print(e)
                return -1

    def updateUserList(self, userList):
        if self.checkAdmin is False:
            print("Update user list failed")
            return False
        try:
            self.refDB.child("List of users").remove(self.admin['idToken'])
            self.refDB.child("Allowed UIDs").remove(self.admin['idToken'])
            for user in userList:
                self.refDB.child("List of users").child(str(user)).set(userList[user], self.admin['idToken'])
                self.refDB.child("Allowed UIDs").child(userList[user]['UID']).set({"Status": 'true', "ID number": str(user)}, self.admin['idToken'])
            print("Update user list successful")
            return True
        except Exception as e:
            print("Update user list failed")
            print(e)
            return False

    def getUserList(self):
        if self.checkAdmin is False:
            print("Get user list failed")
            return False, None
        try:
            userList = {}
            temp_data = self.refDB.child("List of users").get(self.admin['idToken'])
            for user in temp_data.each():
                userList[user.key()] = user.val()
            print("Get user list successful")
            return True, userList
        except Exception as e:
            print("Get user list failed")
            print(e)
            return False, None

    def updateLabStatus(self, labData):
        if self.checkAdmin is False:
            print("Update failed")
            return False
        try:
            self.refDB.child("Lab status").child(labData["Name"]).update({'Status': labData["Status"]}, self.admin['idToken'])
            print("Update lab status successful")
            return True
        except Exception as e:
            print("Update lab status failed")
            print(e)
            return False

    def updateLabStatusList(self, labStatusList):
        if self.checkAdmin is False:
            print("Update lab status list failed")
            return False
        try:
            self.refDB.child("Lab status").remove(self.admin['idToken'])
            for lab in labStatusList:
                self.refDB.child("Lab status").child(lab).set(labStatusList[lab], self.admin['idToken'])
            print("Update lab status list successful")
            return True
        except Exception as e:
            print("Update lab status list failed")
            print(e)
            return False

    def getLabStatusList(self):
        if self.checkAdmin is False:
            print("Get lab status list failed")
            return False, None
        try:
            labstatusList = {}
            temp_data = self.refDB.child("Lab status").get(self.admin['idToken'])
            for user in temp_data.each():
                labstatusList[user.key()] = user.val()
            print("Get lab status successful")
            return True, labstatusList
        except Exception as e:
            print("Get lab status failed")
            print(e)
            return False, None

    def addDevice(self, deviceData):
        if self.checkAdmin is False:
            print("Add failed")
            return False
        try:
            self.refDB.child("List of devices").child(deviceData["Name"]).set(deviceData, self.admin['idToken'])
            print("Add device successful")
            return True
        except Exception as e:
            print("Add device failed")
            print(e)
            return False

    def updateDevice(self, deviceData):
        if self.checkAdmin is False:
            print("Update failed")
            return False
        try:
            self.refDB.child("List of devices").child(deviceData["Name"]).update(deviceData, self.admin['idToken'])
            print("Update device successful")
            return True
        except Exception as e:
            print("Update device failed")
            print(e)
            return False

    def updateDeviceList(self, deviceList):
        if self.checkAdmin is False:
            print("Update device list failed")
            return False
        try:
            self.refDB.child("List of devices").remove(self.admin['idToken'])
            for device in deviceList:
                self.refDB.child("List of devices").child(device).set(deviceList[device], self.admin['idToken'])
            print("Update device list successful")
            return True
        except Exception as e:
            print("Update device list failed")
            print(e)
            return False

    def getDeviceList(self):
        if self.checkAdmin is False:
            print("Get device list failed")
            return False, None
        try:
            deviceList = {}
            temp_data = self.refDB.child("List of devices").get(self.admin['idToken'])
            for user in temp_data.each():
                deviceList[user.key()] = user.val()
            print("Get device list successful")
            return True, deviceList
        except Exception as e:
            print("Get device list failed")
            print(e)
            return False, None

    def addCourseToLabSchedule(self, courseDetail):
        if self.checkAdmin is False:
            print("Add course to lab schedule list failed")
            return False
        try:
            i = int(courseDetail["Reference"]) + int(courseDetail["Start"])
            key = i
            while i <= int(courseDetail["Reference"]) + int(courseDetail["End"]):
                self.refDB.child("Lab schedule").child("Classes").child(courseDetail["Room"]).child(str(i)).set(str(key), self.admin['idToken'])
                i += 1
            self.refDB.child("Lab schedule").child("Courses detail").child(courseDetail["Room"]).child(str(key)).set(courseDetail, self.admin['idToken'])
            print("Add course to lab schedule list successful")
            return True
        except Exception as e:
            print("Add course to lab schedule list failed")
            print(e)
            return False

    def updateSheduleLabList(self, labScheduleList):
        if self.checkAdmin is False:
            print("Update lab schedule list failed")
            return False
        try:
            self.refDB.child("Lab schedule").child("Courses detail").set(labScheduleList["Courses detail"], self.admin['idToken'])
            self.refDB.child("Lab schedule").child("Classes").set(labScheduleList["Classes"], self.admin['idToken'])
            print("Update lab schedule list successful")
            return True
        except Exception as e:
            print("Update lab schedule list failed")
            print(e)
            return False

    def getSheduleLabList(self):
        if self.checkAdmin is False:
            print("Get lab schedule list failed")
            return False, None
        try:
            scheduleLabList = {}
            temp_data = self.refDB.child("Lab schedule").get(self.admin['idToken'])
            scheduleLabList = temp_data.val()
            print("Get device list successful")
            return True, scheduleLabList
        except Exception as e:
            print("Get device list failed")
            print(e)
            return False, None

    def refreshToken(self):
        self.admin = self.auth.refresh(self.admin['refreshToken'])


    def __pushLoginHistory(self, type, room):
        self.refDB.child("Login history").child(room).push({'Time': time.time().__round__(), 'Type': str(type)}, self.admin['idToken'])

    def addLoginHistory(self, ID_number, room):
        if self.checkAdmin is False:
            print("Add login history failed")
            return False
        if room not in labStatusList:
            print("Room does not exist")
            return False
        try:
            self.__pushLoginHistory(ID_number, room)
            print("Add login history successful")
            return True
        except Exception as e:
            print("Add login history failed")
            print(e)
            return False

    def getListPINs(self):
        if self.checkAdmin is False:
            print("Get list PIN failed")
            return False, None
        try:
            listPINs = {}
            temp_data = self.refDB.child("List PINs").get(self.admin['idToken'])
            for PIN in temp_data.each():
                listPINs[PIN.key()] = PIN.val()
            print("Get list PINs successful")
            return True, listPINs
        except Exception as e:
            print("Get list PINs failed")
            print(e)
            return False, None




#myfirebase = MyFirebase("smartsystem.hcmut@gmail.com", "ktmtbk2017")
#data_admin1 = {
 #   "Email": "truongkhoa.1799@gmail.com",
  #  'Gender': "Male",
   # "ID number": "Admin1",
   # "Name": "Truong Khoa",
   # "Password": "123456",
   # "PIN": "1234",
   # "RFID UID": "C2 56 53 96",
#}
#check, data, mypin = myfirebase.addUser(data_admin1, True)
#print(check)
#print(data)
#print(mypin)
# check, temp = myfirebase.getSheduleLabList()
# print(temp["Classes"]["C6_101"])
# myfirebase.addUser({
#         "Name": "Ngo Duc Tuan",
#         "Gender": "Male",
#         "ID number": "1710364",
#         "Email": "ngotuan@gmail.com",
#         "Password": "12345678",
#         "RFID UID": "00 c2 02 19",
#         "PIN": 1234
#     }, True)
#myfirebase.updateLabStatusList(labStatusList)
#myfirebase.updateDeviceList(deviceList)
#myfirebase.updateSheduleLabList(labScheduleList)
# myfirebase.addCourseToLabSchedule(mycourse2)
# check, tempList = myfirebase.getSheduleLabList()
# print(tempList["Classes"])

# mydict = {}
# mylist = [0,4,1,13,5]
# for idx, val in enumerate(mylist):
#     mydict[idx] = str(val)
# print(mydict)
#print(labScheduleList["Classes"]["C5_202"])
#print(labScheduleList["Courses detail"])
# for x in labScheduleList["Classes"]["C5_202"]:
#     print(str(x))
# myfirebase.addUser({
#         "Name": "Ngo Duc Tuan",
#         "Gender": "Male",
#         "ID number": "1710333",
#         "Email": "ngotuan@hcmut.edu.vn",
#         "password": "12345678",
#         "RFID UID": "00 c2 02 19",
#         "PIN": "1234"
#     }, True)
# myfirebase.updateUserList({
#     1710321: {
#         "Name": "Ngo Duc Tuan",
#         "Gender": "male",
#         "ID number": 1710364,
#         "Email": "tuan.ngo1999@hcmut.edu.vn",
#         "UID": "1n3ud914d12e1",
#         "RFID UID": "00 c2 02 13"
#     },
#     1710363: {
#         "Name": "Ngo Duc Tuan",
#         "Gender": "male",
#         "ID number": 1710364,
#         "Email": "tuan.ngo1999@hcmut.edu.vn",
#         "UID": "1n3ud93123e1",
#         "RFID UID": "00 c2 02 13"
#     },
# })
# myfirebase.updateDeviceList({
#     "Esp8266": {
#         "Name": "Esp8266",
#         "Total": 20,
#         "Remained": 10
#     },
#     "Arduino R3": {
#         "Name": "Arduino R3",
#         "Total": 10,
#         "Remained": 10
#     }
# })


