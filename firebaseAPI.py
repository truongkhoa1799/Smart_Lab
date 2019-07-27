import pyrebase
import time
from datetime import datetime

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
            self.__pushLoginHistory("Admin")
            print("Successful to authenticate to Firebase as Admin")
        except:
            print("Failed to authenticate to Firebase as Admin")

    def formatFirebase(self):
        return True

    def addUser(self, userData):
        if self.checkAdmin is False:
            print("Add user failed")
            return False, None
        try:
            newUser = self.auth.create_user_with_email_and_password(userData['Email'], userData['password'])
            uid = self.auth.get_account_info(newUser['idToken'])['users'][0]['localId']
            userData['UID'] = uid
            self.refDB.child("List of users").child(userData['ID number']).set(userData, self.admin['idToken'])
            self.refDB.child("Allowed UIDs").child(userData['UID']).set({"Status": 'true'}, self.admin['idToken'])
            print("Add user successful")
            return True, userData
        except:
            print("Add user failed")
            return False, None

    def activateUser(self, UID):
        if self.checkAdmin is False:
            print("Activate failed")
            return False
        else:
            try:
                self.refDB.child("Allowed UIDs").child(UID).set({"Status": 'true'}, self.admin['idToken'])
                print("Activate user successful")
                return True
            except:
                print("Activate user failed")
                return False

    def deactivateUser(self, UID):
        if self.checkAdmin is False:
            print("Deactivate failed")
            return False
        else:
            try:
                self.refDB.child("Allowed UIDs").child(UID).set({"Status": 'false'}, self.admin['idToken'])
                print("Deactivate user successful")
                return True
            except:
                print("Deactivate user failed")
                return False

    def updateUserList(self, userList):
        if self.checkAdmin is False:
            print("Update user list failed")
            return False
        try:
            self.refDB.child("List of users").remove(self.admin['idToken'])
            self.refDB.child("Allowed UIDs").remove(self.admin['idToken'])
            for user in userList:
                self.refDB.child("List of users").child(str(user)).set(userList[user], self.admin['idToken'])
                self.refDB.child("Allowed UIDs").child(userList[user]['UID']).set({"Status": 'true'}, self.admin['idToken'])
            print("Update user list successful")
            return True
        except:
            print("Update user list failed")
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
        except:
            print("Get user list failed")
            return False, None

    def updateLabStatus(self, labData):
        if self.checkAdmin is False:
            print("Update failed")
            return False
        try:
            self.refDB.child("Lab status").child(labData["Name"]).update({'Status': labData["Status"]}, self.admin['idToken'])
            print("Update lab status successful")
            return True
        except:
            print("Update lab status failed")
            return False

    def updateLabStatusList(self, labStatusList):
        if self.checkAdmin is False:
            print("Update lab status list failed")
            return False
        try:
            self.refDB.child("Lab status").remove()
            for lab in labStatusList:
                self.refDB.child("Lab status").child(lab).set(labStatusList[lab], self.admin['idToken'])
            print("Update lab status list successful")
            return True
        except:
            print("Update lab status list failed")
            return False

    def getLabStatus(self):
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
        except:
            print("Get lab status failed")
            return False, None

    def addDevice(self, deviceData):
        if self.checkAdmin is False:
            print("Add failed")
            return False
        try:
            self.refDB.child("List of devices").child(deviceData["Name"]).set(deviceData, self.admin['idToken'])
            print("Add device successful")
            return True
        except:
            print("Add device failed")
            return False

    def updateDevice(self, deviceData):
        if self.checkAdmin is False:
            print("Update failed")
            return False
        try:
            self.refDB.child("List of devices").child(deviceData["Name"]).update(deviceData, self.admin['idToken'])
            print("Update device successful")
            return True
        except:
            print("Update device failed")
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
        except:
            print("Update device list failed")
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
        except:
            print("Get device list failed")
            return False, None

    def __pushLoginHistory(self, type):
        self.refDB.child("Login history").push({'Time': time.time().__round__(), 'Type': str(type)}, self.admin['idToken'])

    def addLoginHistory(self, ID_number):
        if self.checkAdmin is False:
            print("Add login history failed")
            return False
        try:
            self.__pushLoginHistory(ID_number)
            print("Add login history successful")
            return True
        except:
            print("Add login history failed")
            return False

# myfirebase = MyFirebase("smartsystem.hcmut@gmail.com", "ktmtbk2017")
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
# myfirebase.addUser({
#         "Name": "Ngo Duc Tuan",
#         "Gender": "male",
#         "ID number": 1710364,
#         "Email": "tuan.ngo1999@hcmut.edu.vn",
#         "password": "12345678",
#         "RFID UID": "00 c2 02 13"
#     })

#myfirebase.addLoginHistory(1710364)
#check, deviceList = myfirebase.getDeviceList()
# myfire= MyFirebase("smartsystem.hcmut@gmail.com", "ktmtbk2017")
