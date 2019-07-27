from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from Data import Data
from Devices import Devices
from BorrowedList import BorrowedList
import time
from multiprocessing import Process
from firebaseAPI import MyFirebase
from AccountStatus import AccountStatus

#from CommunicateArduino import SendToArduino


LENGTH_OF_PIN =4
DATA_FROM_ARDUINO=""


#----------------class hoa chu dau
#----------------ham private __roi thuong chu dau, sau do la hoa, public ko co __
#----------------bien thuong het vaf cach nhau _

ADMIN_ID="123"
ADMIN_PASS="1"

MENU_HEIGHT = 600
MENU_WIDTH = 1000
#-------------------------------------------------------------------------------------------------------
class MainMenu:
    def __init__(self, master):
        self.master=master

    def mainMenu(self):
        self.__main_frame = Frame(self.master, bg='#ffffff')
        self.__main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.load = Image.open("SmartLab.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.__logo = Label(self.master, image=self.render, bg='#ffffff')
        self.__logo.place(relx=0.42, rely=0.1)
        self.__controlUserBut()
        self.__controlLabBut()
        self.__controlDevicesBut()
        self.__logOutBut()


    def __controlUserBut(self):
        self.control_user_but = Button(self.master, bg='#00b386', text="Control User", fg='#ffffff', font =('time new roman', 18, 'bold'), command =self.__controlUser)
        self.control_user_but.place(relx=0.2, rely=0.28, relheight= 0.15, relwidth = 0.6)

    def __controlLabBut(self):
        self.control_lab_but = Button(self.master, bg='#00b386', text="Control Lab", fg='#ffffff',font=('time new roman', 18, 'bold'), command=self.__controlLab)
        self.control_lab_but.place(relx=0.2, rely=0.45, relheight=0.15, relwidth=0.6)

    def __logOutBut(self):
        self.load_LogoutBut = Image.open("LogoutBut.png")
        self.render_LogoutBut = ImageTk.PhotoImage(self.load_LogoutBut)
        self.log_out_but = Button(self.master, image=self.render_LogoutBut, bg='#ffffff', relief=FLAT, command = self.__logOut)
        self.log_out_but.place(relx=0.42, rely=0.8, relheight=0.18, relwidth=0.18)


    def __controlDevicesBut(self):
        self.control_device_but = Button(self.master, bg='#00b386', text="Control Devices", fg='#ffffff',font=('time new roman', 18, 'bold'), command= self.__controlDevices)
        self.control_device_but.place(relx=0.2, rely=0.62, relheight=0.15, relwidth=0.6)

    def __controlDevices(self):
        devices=DevicesMenu(self.master)
        devices.mainMenu()

    def __controlLab(self):
        controlLab=ControlLab(self.master)
        controlLab.mainMenu()

    def __logOut(self):
        result=messagebox.askyesno("Log Out","Are you sure to log out?")
        if result==1: SignInScreen.SignInScreen()
        else : self.mainMenu()
    def __controlUser(self):
        controlUser= ControlUser(self.master)
        controlUser.mainMenu()

#-------------------------------------------------------------------------------------------------------

class SignIn:
    def __init__(self, master):
        self.__master=master
        canvas = Canvas(self.__master, height=MENU_HEIGHT, width=MENU_WIDTH)
        canvas.pack()

    def SignInScreen(self):
        self.__main_frame = Frame(self.__master, bg='#ffffff')
        self.__main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.load = Image.open("SmartLab.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.__logo= Label(self.__main_frame, image=self.render, bg='#ffffff' )
        self.__logo.place(relx=0.42, rely=0.1)
        self.__ID()
        self.__PASSWORD()
        self.__LogInBut()
        self.__SignInLogo()

    def __SignInLogo(self):
        self.__load_signinlogo = Image.open("signInID.png")
        self.__render_signinlogo = ImageTk.PhotoImage(self.__load_signinlogo)
        self.__signinlogo = Label(self.__main_frame, image=self.__render_signinlogo, bg='#ffffff')
        self.__signinlogo.place(relx=0.45, rely=0.3,relheight=0.1, relwidth=0.1)

    def __ID(self):
        self.__load_SignInID = Image.open("SignInUserLogo.png")
        self.__render_SignInID = ImageTk.PhotoImage(self.__load_SignInID)
        self.__SignInID = Label(self.__main_frame, image=self.__render_SignInID, bg='#ffffff')
        self.__SignInID.place(relx=0.2, rely=0.5, relheight=0.05, relwidth=0.05)
        self.__entry_ID=Entry(self.__main_frame, bg ='#f2f2f2', borderwidth=1.5,disabledbackground='#595959')
        self.__entry_ID.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.05)

    def __PASSWORD(self):
        self.__load_SignInPass = Image.open("SignInPass.png")
        self.__render_SignInPass = ImageTk.PhotoImage(self.__load_SignInPass)
        self.__SignInPass = Label(self.__main_frame, image=self.__render_SignInPass, bg='#ffffff')
        self.__SignInPass.place(relx=0.2, rely=0.6, relheight=0.05, relwidth=0.05)
        self.__entry_PASS = Entry(self.__main_frame,  bg='#f2f2f2', borderwidth=1.5,disabledbackground='#f2f2f2', show="*")
        self.__entry_PASS.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.05)

    def __LogInBut(self):
        self.__signin_button = Button(self.__master, bg='#00b386', text="Log In", fg='#ffffff',font=('time new roman', 20, 'bold'), command =self.__LogIn)
        self.__signin_button.place(relx=0.3, rely=0.7, relheight=0.1, relwidth=0.4)


    def __LogIn(self):
        self.__string_ID=self.__entry_ID.get()
        self.__string_PASS=self.__entry_PASS.get()
        if self.__string_ID==ADMIN_ID and self.__string_PASS==ADMIN_PASS:
            menu_sreen= MainMenu(self.__master)
            menu_sreen.mainMenu()
        else :
            messagebox.showwarning("Log In", "Wrong Password")
            SignInScreen.SignInScreen()
#-------------------------------------------------------------------------------------------------------

class ControlUser:
    def __init__(self, master):
        self.__master=master

    def mainMenu(self):
        self.__main_frame = Frame(self.__master, bg='#ffffff')
        self.__main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.__load_title = Image.open("controluser.png")
        self.__render_title = ImageTk.PhotoImage(self.__load_title)
        self.__title=Label(self.__main_frame,image= self.__render_title, bg='#ffffff', bd =4, relief = RAISED)
        self.__title.place(relx=0, rely=0, relheight=0.25, relwidth=1)

        self.__backButton()
        self.__addButton()
        self.__checkButton()
        self.__deleteButton()
        self.__changePassButton()

    def __backButton(self):

        self.__load_back = Image.open("back.png")
        self.__render_back = ImageTk.PhotoImage(self.__load_back)
        self.__back_button = Button(self.__master, image=self.__render_back, bd=4, bg='#ffffff', command=self.__back)
        self.__back_button.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)

    def __addButton(self):
        self.__load_plus = Image.open("plus.png")
        self.__render_plus = ImageTk.PhotoImage(self.__load_plus)
        self.__add_button= Button(self.__master, image = self.__render_plus, bd=4, bg ='#ffffff', command=self.__addUseer)
        self.__add_button.place(relx=0, rely=0.25, relheight=0.25, relwidth=0.5)


    def __deleteButton(self):
        self.__load_delete = Image.open("delete.png")
        self.__render_delete = ImageTk.PhotoImage(self.__load_delete)
        self.__delete_button = Button(self.__master, image=self.__render_delete, bd=4, bg='#ffffff', command= self.__deleteUser)
        self.__delete_button.place(relx=0, rely=0.75, relheight=0.25, relwidth=0.5)

    def __checkButton(self):
        self.__load_check = Image.open("check.png")
        self.__render_check = ImageTk.PhotoImage(self.__load_check)
        self.__check_button = Button(self.__master, image=self.__render_check, bd=4, bg='#ffffff', command= self.__checkUser)
        self.__check_button.place(relx=0.5, rely=0.25, relheight=0.25, relwidth=0.5)

    def __changePassButton(self):
        self.__load_changePass = Image.open("changepass.png")
        self.__render_changePass = ImageTk.PhotoImage(self.__load_changePass)
        self.__changePass_button = Button(self.__master, image=self.__render_changePass, bd=4, bg='#ffffff', command= self.__changePass)
        self.__changePass_button.place(relx=0, rely=0.5, relheight=0.25, relwidth=0.5)

    def __addUseer(self):
        addUser= AddUser(self.__master)
        addUser.mainMenu()

    def __checkUser(self):
        checkUser=CheckUser(self.__master)
        checkUser.mainMenu()

    def __changePass(self):
        changePass=ChangePass(self.__master)
        changePass.mainMenu()

    def __deleteUser(self):
        root= Tk()
        deleteUser= DeleteUser(root)
        deleteUser.mainMenu()

    def __back(self):
        mainMenu= MainMenu(self.__master)
        mainMenu.mainMenu()
#-------------------------------------------------------------------------------------------------------
class AddUser:
    def __init__(self, master):
        self.__master=master

    def mainMenu(self):
        self.add_users_frame=Frame(self.__master, bg='#ffffff')
        self.add_users_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.__backButton()
        self.__submitButton()
        self.__nameUser()
        self.__Gender()
        self.__SIDUser()
        self.__Email()
        self.__Pin()
        self.__checkPin()
        self.__Password()
        self.__checkPassword()

    def __backButton(self):
        self.__back_button= Button(self.__master, text="Back",  command= self.__backToControlUser, bd=4,font=("time new roman", 12, 'bold'), fg ='#ffffff', bg ='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.3, rely=0.86, relheight=0.1, relwidth=0.2)

    def __submitButton(self):
        self.__submit_button = Button(self.__master, text="Submit",  command=self.__submitAddUser, bd=4,font=("time new roman", 12,'bold'), fg ='#ffffff', bg ='#00b386')
        self.__submit_button.config(relief=RAISED)
        self.__submit_button.place(relx=0.5, rely=0.86, relheight=0.1, relwidth=0.2)

    def __nameUser(self):
        self.__label_name= Label(self.__master, text ="Name:",font=("times new roman", 14),anchor= 'w', bg= '#ffffff')
        self.__label_name.place(relx=0.25, rely=0.03, relheight=0.05, relwidth=0.1)

        self.__entry_name= Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5, relief =RIDGE)
        self.__entry_name.place(relx=0.25, rely=0.08, relwidth=0.5, relheight=0.05)

    def __Gender(self):
        self.__label_gender = Label(self.__master, text="Gender:", font=("times new roman", 14), anchor= 'w',bg= '#ffffff')
        self.__label_gender.place(relx=0.25, rely=0.13, relheight=0.05, relwidth=0.1)

        self.__entry_gender = Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5,relief =RIDGE)
        self.__entry_gender.place(relx=0.25, rely=0.18, relwidth=0.5, relheight=0.05)

    def __Email(self):
        self.__label_email = Label(self.__master, text="Email:", font=("times new roman", 14),anchor= 'w',bg= '#ffffff')
        self.__label_email.place(relx=0.25, rely=0.23, relheight=0.05, relwidth=0.1)

        self.__entry_email = Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5,relief =RIDGE)
        self.__entry_email.place(relx=0.25, rely=0.28, relwidth=0.5, relheight=0.05)

    def __SIDUser(self):
        self.__label_SID = Label(self.__master, text="Student ID: ", font=("times new roman", 14),anchor= 'w',bg= '#ffffff')
        self.__label_SID.place(relx=0.25, rely=0.33, relheight=0.05, relwidth=0.1)

        self.__entry_SID = Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5, relief =RIDGE)
        self.__entry_SID.place(relx=0.25, rely=0.38, relwidth=0.5, relheight=0.05)



    def __Pin(self):
        self.__label_pin = Label(self.__master, text="Pin(4digits):", font=("times new roman", 14), anchor= 'w',bg= '#ffffff')
        self.__label_pin.place(relx=0.25, rely=0.43, relheight=0.05, relwidth=0.1)

        self.__entry_pin = Entry(self.__master,show="*",bg ='#f2f2f2', borderwidth=1.5,relief =RIDGE)
        self.__entry_pin.place(relx=0.25, rely=0.48, relwidth=0.5, relheight=0.05)



    def __checkPin(self):
        self.__label_check_pin = Label(self.__master, text="Again Pin:", font=("times new roman", 14), anchor='w', bg='#ffffff')
        self.__label_check_pin.place(relx=0.25, rely=0.53 ,relheight=0.05, relwidth=0.1)

        self.__entry_check_pin = Entry(self.__master, show="*", bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_check_pin.place(relx=0.25, rely=0.58, relwidth=0.5, relheight=0.05)

    def __Password(self):
        self.__label_pw = Label(self.__master, text="Password:", font=("times new roman", 14), anchor= 'w',bg= '#ffffff')
        self.__label_pw.place(relx=0.25, rely=0.63, relheight=0.05, relwidth=0.1)

        self.__entry_pw = Entry(self.__master,show="*",bg ='#f2f2f2', borderwidth=1.5,relief =RIDGE)
        self.__entry_pw.place(relx=0.25, rely=0.68, relwidth=0.5, relheight=0.05)



    def __checkPassword(self):
        self.__label_check_pw = Label(self.__master, text="Again Password:", font=("times new roman", 12), anchor='w', bg='#ffffff')
        self.__label_check_pw.place(relx=0.25, rely=0.73, relheight=0.05, relwidth=0.12)

        self.__entry_check_pw = Entry(self.__master, show="*", bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_check_pw.place(relx=0.25, rely=0.78, relwidth=0.5, relheight=0.05)



    def __backToControlUser(self):
        addUser=ControlUser(self.__master)
        addUser.mainMenu()

    # get the infor save in database, and send name and id to arduino, simultaneously get the iud and save in database
    def __submitAddUser(self):
        self.__string_name=self.__entry_name.get()
        self.__string_gender=self.__entry_gender.get()
        self.__string_gender=self.__string_gender.upper()
        self.__string_SID=self.__entry_SID.get()
        self.__string_email=self.__entry_email.get()
        self.__string_check_pin=self.__entry_check_pin.get()
        self.__string_pin = self.__entry_pin.get()
        self.__string_pw= self.__entry_pw.get()
        self.__string_check_pw= self.__entry_check_pw.get()
        result=messagebox.askyesno("Add User","Are you sure about your information?")
        if result ==1:
           self.__submitAddUserConfrim()

    def __submitAddUserConfrim(self):
        if self.__checkAddUsers()==1:
            #check = communicate.sendInfor("1|"+self.__string_name+"|"+self.__string_pin)
            check = 1
            if check==1:
                # if check = 1 do else print fail
                #uid=communicate.getUID()
                uid="82 BB 44 96"
                #print(uid)
                #send infor to arduino to get RFID UID
                list = {}
                list["Name"] = self.__string_name
                list["Gender"] = self.__string_gender
                list["ID number"] = self.__string_SID
                list["Email"] = self.__string_email
                list["RFID UID"] = uid
                list["PIN"] = self.__string_pin
                list["password"] = self.__string_pw
                # send this list to FireBase
                # and receive new list
                print(list)
                check, new_list = database.addUser(list)
                if check==TRUE:
                    data.addUser(new_list)
                    account=AccountStatus()
                    account.addUser(new_list["ID number"])
                    messagebox.showinfo("Add Users", "Add successfully.")
                    self.mainMenu()
                else: messagebox.showinfo("Add User","Fail")
            elif check==0: messagebox.showinfo("Add User","Fail")
            elif check==2: messagebox.showinfo("Add User","Used Tag")
            elif check==3: messagebox.showinfo("Add User","Please insert your Tag")
        elif self.__checkAddUsers()==0:
            messagebox.showwarning("Add Users", "Add unsuccessfully. Please fulfill your information!")
            #self.mainMenu()
        elif self.__checkAddUsers()==2:
            messagebox.showwarning("Add Users", "Add unsuccessfully. Existing an account in system!")
            #self.mainMenu()
        elif self.__checkAddUsers()==3:
            messagebox.showwarning("Add Users", "Add unsuccessfully. Your SID must has 7 digits!")
            #self.mainMenu()
        elif self.__checkAddUsers()==4:
            messagebox.showwarning("Add Users","Wrong password!")
            #self.mainMenu()
        elif self.__checkAddUsers()==5:
            messagebox.showwarning("Add Users", "Invalid SID!")
            #self.mainMenu()
        elif self.__checkAddUsers()==6:
            messagebox.showwarning("Add Users", "Invalid Email!")
            #self.mainMenu()
        elif self.__checkAddUsers()==7:
            messagebox.showwarning("Add Users", "Invalid Password!")
        elif self.__checkAddUsers()==8:
            messagebox.showwarning("Add Users", "Exist Account")

    def __checkValidSID(self, SID):
        count=0
        for i in range(7):
            if ord(SID[i])>=48 and ord(SID[i])<=57: count+=1
        if count==7: return 1
        else: return 0

    def __checkValidEmail(self, email):
        valid="@gmail.com"
        if valid in email: return 1
        else: return 0

    def __checkValidPass(self):
        count=0
        if self.__string_pw== self.__string_check_pw and len(self.__string_pw)>=7:
            for i in self.__string_pw:
                if (ord(i)>= 48 and ord(i)<=57) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
                    count=count+1
        if count==len(self.__string_pw): return 1
        else: return 0

    def __checkExistID(self):
        if data.checkID(self.__string_SID)==1: return 0
        else: return 1

    def __checkAddUsers(self):
        #check =5 invalid SID
        check=1
        if self.__checkExistID()==0: check=8
        elif self.__checkValidSID(self.__string_SID)==0: check=5
        elif self.__checkValidEmail(self.__string_email) == 0: check=6
        elif self.__checkValidPass() == 0: check=7
        #check whether all of entry is fulfilled or not if not check =0
        elif len(self.__string_email) == 0 or len(self.__string_name) == 0 or len(self.__string_pin) ==0 or len(self.__string_SID)  == 0:check=0
        # SID is 7 digits so if there is more or less check =3
        elif len(self.__string_SID)!=7: check=3
        # in this method, check whether the user is in the database, rematch with another
        # users about SID, email or not if yes, return check =2
        #check whether the pin is correct or not
        elif (self.__string_pin!=self.__string_check_pin) or len(self.__string_pin)!=LENGTH_OF_PIN:check=4
        return check
#-------------------------------------------------------------------------------------------------------

class CheckUser:
    def __init__(self, master):
        self.__master=master

    def mainMenu(self):
        self.__check_users_frame = Frame(self.__master, bg='#ffffff')
        self.__check_users_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.__backButton()
        self.__checkButton()
        self.__checkEntry()
        self.__activeButton()


    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backToControlUser, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386',relief=RAISED)
        self.__back_button.place(relx=0.6, rely=0.85, relheight=0.1, relwidth=0.2)

    def __activeButton(self):
        self.__back_button = Button(self.__master, text="Active", command=self.__activeAcount, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', relief=RAISED)
        self.__back_button.place(relx=0.4, rely=0.85, relheight=0.1, relwidth=0.2)

    def __checkButton(self):
        self.__check_button = Button(self.__master, text="Check", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', command = self.__check,relief=RAISED)
        self.__check_button.place(relx=0.2, rely=0.85, relheight=0.1, relwidth=0.2)

    def __nameUser(self):
        self.label_name= Label(self.__master, text ="Name:",font=("times new roman", 12),anchor= 'w', bg= '#ffffff')
        self.label_name.place(relx=0.025, rely=0.25, relheight=0.08, relwidth=0.2)


    def __SIDUserAndGender(self):
        self.label_SID = Label(self.__master, text="Student ID: ", font=("times new roman", 12),anchor= 'w',bg= '#ffffff')
        self.label_SID.place(relx=0.025, rely=0.39, relheight=0.08, relwidth=0.2)

        self.label_gender = Label(self.__master, text="Gender: ", font=("times new roman", 12), anchor='w',bg='#ffffff')
        self.label_gender.place(relx=0.6, rely=0.39, relheight=0.08, relwidth=0.2)



    def __Email(self):
        self.label_email = Label(self.__master, text="Email:", font=("times new roman", 12),anchor= 'w',bg= '#ffffff')
        self.label_email.place(relx=0.025, rely=0.53, relheight=0.08, relwidth=0.2)

    def __Status(self):
        self.label_email = Label(self.__master, text="Email:", font=("times new roman", 12),anchor= 'w',bg= '#ffffff')
        self.label_email.place(relx=0.025, rely=0.71, relheight=0.08, relwidth=0.2)


    def __checkEntry(self):
        self.__entry= Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5, relief =RIDGE)
        self.__entry.place(relx=0.325, rely = 0.1, relwidth = 0.65, relheight= 0.1)

        self.__ID= Menubutton(text ="ID Student:", font =("time new roman", 12), bd=4, bg='#e0e0d1', relief=RAISED)
        self.__ID.place (relx=0.025, rely = 0.1, relwidth = 0.3, relheight= 0.1)


    def __check(self):
        list=[]
        list=data.getInforWithID(self.__entry.get())
        if list!=0:
            self.__showInfor(list)
        else: messagebox.showinfo("Check User","There is no user!")

    def __activeAcount(self):
        result= messagebox.askyesno("Active Account","Are you sure?")
        if result==1:
            ID= self.__entry.get()
            account=AccountStatus()
            account.Active(ID)
            database.activateUser(data.getUID(ID))
            list = []
            list = data.getInforWithID(self.__entry.get())
            self.__showInfor(list)

    def __showInfor(self, list):
        self.__SIDUserAndGender()
        self.__Email()
        self.__nameUser()
        self.__Status()
        account=AccountStatus()

        self.show_SID = Label(self.__master,text=list.get("ID number"), bg='#f2f2f2', borderwidth=1.5, relief=RIDGE, font=("time new roman", 12))
        self.show_SID.place(relx=0.25, rely=0.39, relheight=0.08, relwidth=0.3)

        self.show_gender = Label(self.__master, text=list.get("Gender"), bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        self.show_gender.place(relx=0.8, rely=0.39, relheight=0.08, relwidth=0.15)

        self.show_name = Label(self.__master,text=list.get("Name"), bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        self.show_name.place(relx=0.25, rely=0.25, relheight=0.08, relwidth=0.725)

        self.show_Email = Label(self.__master,text=list.get("Email"), bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        self.show_Email.place(relx=0.25, rely=0.53, relheight=0.08, relwidth=0.725)

        self.show_Status = Label(self.__master, text=account.getStatus(list.get("ID number")), bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        self.show_Status.place(relx=0.25, rely=0.71, relheight=0.08, relwidth=0.725)



    def __backToControlUser(self):
        addUser = ControlUser(self.__master)
        addUser.mainMenu()
#-------------------------------------------------------------------------------------------------------

###### UPDATing
class ChangePass:
    def __init__(self, master):
        self.__master=master

    def mainMenu(self):
        self.__check_users_frame = Frame(self.__master, bg='#ffffff')
        self.__check_users_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.__backButton()
        self.__changeButton()
        self.__Title()
        self.__entrySID()
        self.__entrypass()

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backToControlUser, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', relief=RAISED)
        self.__back_button.place(relx=0.3, rely=0.77, relheight=0.1, relwidth=0.2)

    def __changeButton(self):
        self.__check_button = Button(self.__master, text="Change", bd=4, font=("time new roman", 12, 'bold'),fg='#ffffff', bg='#00b386', relief=RAISED, command=self.__changePass)
        self.__check_button.place(relx=0.5, rely=0.77, relheight=0.1, relwidth=0.2)

    def __Title(self):
        self.__title_frame = Frame(self.__master, bg='#00b386')
        self.__title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.22)
        self.__title = Label(self.__title_frame, text="Change Password", fg='#00b386', font=("time new roman", 30, 'bold'),bd=4, bg='#ffffff')
        self.__title.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.76)

    def __backToControlUser(self):
        addUser = ControlUser(self.__master)
        addUser.mainMenu()



    def __entrySID(self):
        self.__label_SID = Label(self.__master, text="Student ID: ", font=("times new roman", 14), anchor='w', bg='#ffffff')
        self.__label_SID.place(relx=0.25, rely=0.35, relheight=0.05, relwidth=0.1)

        self.__entry_SID = Entry(self.__master, bg ='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_SID.place(relx=0.25, rely=0.4, relwidth=0.5, relheight=0.05)

    def __entrypass(self):
        self.__label_pass = Label(self.__master, text="New Key: ", font=("times new roman", 14), anchor='w', bg='#ffffff')
        self.__label_pass.place(relx=0.25, rely=0.5, relheight=0.05, relwidth=0.1)

        self.__entry_pass = Entry(self.__master, bg ='#f2f2f2', borderwidth=1.5, relief=RIDGE, show="*")
        self.__entry_pass.place(relx=0.25, rely=0.55, relwidth=0.5, relheight=0.05)

    def __changePass(self):
        Pass= self.__entry_pass.get()
        SID=self.__entry_SID.get()
        __result =messagebox.askyesno("Change Password","Are you sure?")
        if __result==1:
            self.__changePassConfirm(SID, Pass)
            self.mainMenu()

    def __changePassConfirm(self, SID, Pass):
        if len(Pass) !=0 and len(SID)!=0:
            data.changePass(SID, Pass)
            messagebox.showinfo("Change Password","Change Password Successfully!")
        else:
            messagebox.showwarning("Change Password","Change Password Unsuccessfully!")
#-------------------------------------------------------------------------------------------------------

class DeleteUser:
    def __init__(self, master):
        self.__master= master
        self.__arrayList = []
        canvas = Canvas(self.__master, height=MENU_HEIGHT, width=MENU_WIDTH)
        canvas.pack()



    def mainMenu(self):
        self.__arrayList=[]
        self.add_users_frame = Frame(self.__master, bg='#ffffff')
        self.add_users_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.__backButton()
        self.__deleteButton()
        self.__scrollFrame()

    def __backButton(self):
        self.back_button = Button(self.__master, text="Back", command=self.__backToControlUser, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.back_button.config(relief=RAISED)
        self.back_button.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.2)

    def __deleteButton(self):
        self.submit_button = Button(self.__master, text="Delete", command=self.__deleteUser, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.submit_button.config(relief=RAISED)
        self.submit_button.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.2)

    def __scrollFrame(self):
        self.__showTag=Label(self.__master,text="STT     SID     RFID UID                Name                              Email                                           UID                                         PIN           Password", font =("time new roman", 12), bg='#ffffff', anchor='w')
        self.__showTag.place(relx=0, rely=0, relheight=0.1, relwidth=0.9)
        #----------------------------------------------------------------
        self.__scroll_frame = Frame(self.__master, bg='#ebebe0')
        self.__scroll_frame.place(relx=0, rely=0.1, relheight=0.7, relwidth=1)

        self.__scroll_barY= Scrollbar(self.__scroll_frame, orient=VERTICAL)
        self.__scroll_barY.pack(side=RIGHT, fill=Y)


        self.__list_box=Listbox(self.__scroll_frame,yscrollcommand = self.__scroll_barY.set)
        list=data.getList()
        count=0
        for i in list:
            accountStatus= AccountStatus()
            if accountStatus.getStatus(list[i].get("ID number"))=="ACTIVE":
                name=list[i].get("Name")
                ID = list[i].get("ID number")
                UID = list[i].get("UID")
                RFID_UID = list[i].get("RFID UID")
                email = list[i].get("Email")
                PIN = list[i].get("PIN")
                password = list[i].get("password")
                self.__arrayList.append("")
                s=[ID,UID]
                self.__arrayList[count] =s
                count += 1
                infor=" "+str(count) + (" "*(6-len(str(count))))+":     "+ID+"  :  "+RFID_UID+("  "*(16-len(RFID_UID)))+":"+("  "*3)+name +("  "*(24-len(name)))+":"+("  "*4)+email + ("  "*(30-len(email)))+":"+("  "*4)+ UID + ("  "*(20-len(UID)))+":"+("  "*3)+ PIN + ("  "*(9-len(PIN)))+":"+("  "*4)+ password
                self.__list_box.insert(END, infor)
        self.__list_box.place(relx=0, rely=0, relheight=1, relwidth=0.98)
        # ----------------------------------------------------------------
        self.__scroll_barY.config(command= self.__list_box.yview)

    def __backToControlUser(self):
        self.__master.destroy()

    def __deleteUser(self):
        result=messagebox.askyesno("Delete User", "Are you sure to delete this user?")
        if result==1: self.__deleteConfirm()

    def __deleteConfirm(self):
        index=self.__list_box.curselection()
        if index!=():
            self.__list_box.delete(index,index)
            data =Data()
            data.deleteUser(self.__arrayList[index[0]][0])
            database.deactivateUser(self.__arrayList[index[0]][1])
            self.__arrayList.remove(self.__arrayList[index[0]])
            messagebox.showinfo("Delete User","Delete user successfully!")
        else:
            messagebox.showwarning("Delete User","You must choose user to execute this task.")

#-------------------------------------------------------------------------------------------------------

class DevicesMenu:
    def __init__(self,master):
        self.__master=master
    def mainMenu(self):
        self.add_users_frame = Frame(self.__master, bg='#ffffff')
        self.add_users_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.__backButton()
        self.__controlDevices()
        self.__borrowedDevices()


    def __backButton(self):
        self.back_button = Button(self.__master, text="Back", command=self.__backToMainMenu, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.back_button.config(relief=RAISED)
        self.back_button.place(relx=0.4, rely=0.85, relheight=0.1, relwidth=0.2)

    def __controlDevices(self):
        self.control_user_but = Button(self.__master, bg='#00b386', text="Control Devices", fg='#ffffff', font =('time new roman', 18, 'bold'), command=self.__controlDevicesWindow)
        self.control_user_but.place(relx=0.2, rely=0.28, relheight= 0.15, relwidth = 0.6)

    def __borrowedDevices(self):
        self.control_user_but = Button(self.__master, bg='#00b386', text="Borrowed Devices", fg='#ffffff',font=('time new roman', 18, 'bold'), command=self.__borrowedDevicesWindow)
        self.control_user_but.place(relx=0.2, rely=0.48, relheight=0.15, relwidth=0.6)

    def __controlDevicesWindow(self):
        controlDevices=ControlDevices(self.__master)
        controlDevices.mainMenu()

    def __borrowedDevicesWindow(self):
        borrowedDevices= BorrowedEquipments(self.__master)
        borrowedDevices.mainMenu()



    def __backToMainMenu(self):
        mainMenu= MainMenu(self.__master)
        mainMenu.mainMenu()

#-------------------------------------------------------------------------------------------------------
class ControlLab:
    def __init__(self,master):
        self.__master=master

    def mainMenu(self):
        self.__main_frame = Frame(self.__master, bg='#ffffff')
        self.__main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.load = Image.open("SmartLab.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.__logo = Label(self.__master, image=self.render, bg='#ffffff')
        self.__logo.place(relx=0.42, rely=0.1)
        self.__scheduleLabBut()
        self.__backButton()

    def __scheduleLabBut(self):
        self.control_user_but = Button(self.__master, bg='#00b386', text="Schedule Lab", fg='#ffffff',font=('time new roman', 18, 'bold'), command=self.__scheduleLab)
        self.control_user_but.place(relx=0.2, rely=0.28, relheight=0.15, relwidth=0.6)

    # def __controlLabBut(self):
    #     self.control_lab_but = Button(self.master, bg='#00b386', text="Control Lab", fg='#ffffff',
    #                                   font=('time new roman', 18, 'bold'), command=self.__controlLab)
    #     self.control_lab_but.place(relx=0.2, rely=0.45, relheight=0.15, relwidth=0.6)
    #
    # def __logOutBut(self):
    #     self.load_LogoutBut = Image.open("LogoutBut.png")
    #     self.render_LogoutBut = ImageTk.PhotoImage(self.load_LogoutBut)
    #     self.log_out_but = Button(self.master, image=self.render_LogoutBut, bg='#ffffff', relief=FLAT,
    #                               command=self.__logOut)
    #     self.log_out_but.place(relx=0.42, rely=0.8, relheight=0.18, relwidth=0.18)
    #
    # def __controlDevicesBut(self):
    #     self.control_device_but = Button(self.master, bg='#00b386', text="Control Devices", fg='#ffffff',
    #                                      font=('time new roman', 18, 'bold'), command=self.__controlDevices)
    #     self.control_device_but.place(relx=0.2, rely=0.62, relheight=0.15, relwidth=0.6)

    def __scheduleLab(self):
        print("1")

    # def __controlLab(self):
    #     controlLab = ControlLab(self.master)
    #     controlLab.mainMenu()
    #
    # def __logOut(self):
    #     result = messagebox.askyesno("Log Out", "Are you sure to log out?")
    #     if result == 1:
    #         SignInScreen.SignInScreen()
    #     else:
    #         self.mainMenu()
    #
    # def __controlUser(self):
    #     controlUser = ControlUser(self.master)
    #     controlUser.mainMenu()

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backTomainMenu, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.4)

    def __backTomainMenu(self):
        mainemu = MainMenu(self.__master)
        mainemu.mainMenu()
#-------------------------------------------------------------------------------------------------------

class ScheduleLab:
    def __init__(self, master):
        self.__master=master

    def mainMenu(self):
        self.__main_frame = Frame(self.__master, bg='#ffffff')
        self.__main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        
#-------------------------------------------------------------------------------------------------------


class ControlDevices:
    def __init__(self, master):
        self.__master=master
        self.__arrayKey=[]
    def mainMenu(self):
        self.__arrayKey=[]
        self.add_users_frame = Frame(self.__master, bg='#ffffff')
        self.add_users_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.__addButton()
        self.__deleteButton()
        self.__deleteButton()
        self.__backButton()
        self.__scrollFrame()

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backToControlDevices, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.6, rely=0.85, relheight=0.1, relwidth=0.2)

    def __deleteButton(self):
        self.__delete_button = Button(self.__master, text="Delete", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', command=self.__deleteDevicces)
        self.__delete_button.config(relief=RAISED)
        self.__delete_button.place(relx=0.4, rely=0.85, relheight=0.1, relwidth=0.2)

    def __addButton(self):
        self.__add_button = Button(self.__master, text="Add", command=self.__addDevices, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__add_button.config(relief=RAISED)
        self.__add_button.place(relx=0.2, rely=0.85, relheight=0.1, relwidth=0.2)

    def __addDevices(self):
        index= self.__list_box.curselection()
        if index!=():
            index=int(index[0])
            devices= Devices()
            addWin=Tk()
            addDevicesWin= AddDevicesWin(addWin,self.__master, self.__arrayKey[index])
            addDevicesWin.mainMenu()
        else:
            addWin = Tk()
            addDevicesWin = AddNewDevicesWin(addWin, self.__master)
            addDevicesWin.mainMenu()

    def __deleteDevicces(self):
        index_delete = self.__list_box.curselection()
        if index_delete!=():
            deleteWin = Tk()
            index=int(index_delete[0])
            deleteDevicesWin= DeleteDevicesWin(deleteWin, self.__master, self.__arrayKey[index])
            deleteDevicesWin.mianMenu()
        else:
            messagebox.showwarning("Delete User","Choose one device to delete")



    def __scrollFrame(self):
        self.__showTag=Label(self.__master,text="STT  Name                 Amount       Current", font =("time new roman", 12), bg='#ffffff', anchor='w')
        self.__showTag.place(relx=0, rely=0, relheight=0.1, relwidth=0.9)
        #----------------------------------------------------------------
        self.__scroll_frame = Frame(self.__master, bg='#ebebe0')
        self.__scroll_frame.place(relx=0, rely=0.1, relheight=0.7, relwidth=1)

        self.__scroll_barY= Scrollbar(self.__scroll_frame, orient=VERTICAL)
        self.__scroll_barY.pack(side=RIGHT, fill=Y)

        self.__scroll_barX = Scrollbar(self.__scroll_frame, orient=HORIZONTAL)
        self.__scroll_barX.pack(side=BOTTOM, fill=X)

        self.__list_box=Listbox(self.__scroll_frame,yscrollcommand = self.__scroll_barY.set, xscrollcommand= self.__scroll_barX.set)
        devices=Devices()
        list=devices.getList()
        count=0
        for i in list:
            name= list[i]["Name"]
            total = list[i]["Total"]
            remained = list[i]["Remained"]
            self.__arrayKey.append("")
            self.__arrayKey[count]=name
            count+=1
            infor=str(count) + (" "*(6-len(str(count))))+":     "+name+("  "*(16-len(name)))+":"+("  "*(7-len(total)))+total+("  "*(8-len(total)))+":"+("  "*(8-len(total)))+remained
            self.__list_box.insert(END, infor)
        self.__list_box.place(relx=0, rely=0, relheight=0.92, relwidth=0.95)
        # ----------------------------------------------------------------
        self.__scroll_barY.config(command= self.__list_box.yview)
        self.__scroll_barX.config(command=self.__list_box.xview)



    def __backToControlDevices(self):
        devices= DevicesMenu(self.__master)
        devices.mainMenu()
#-------------------------------------------------------------------------------------------------------

class AddDevicesWin:
    def __init__(self, master, master_controlDevices, name):
        self.__master = master
        self.__masterControlDevices=master_controlDevices
        self.__name= name
        canvas = Canvas(self.__master, height=100, width=200)
        canvas.pack()

    def mainMenu(self):
        self.__amountDevices()
        self.__submitButton()
        self.__backButton()


    def __amountDevices(self):
        self.__label_total = Label(self.__master, text="Amount: ", font=("times new roman", 13), anchor='w',bg='#ffffff')
        self.__label_total.place(relx=0.35, rely=0.1, relheight=0.2, relwidth=0.3)

        self.__entry_total = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_total.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.2)

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__closeAddDevicesWin, bd=4,font=("time new roman", 10, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.5, rely=0.7, relheight=0.2, relwidth=0.3)

    def __submitButton(self):
        self.__submit_button = Button(self.__master, text="Submit", command=self.__submit, bd=4,font=("time new roman", 10, 'bold'), fg='#ffffff', bg='#00b386')
        self.__submit_button.config(relief=RAISED)
        self.__submit_button.place(relx=0.2, rely=0.7, relheight=0.2, relwidth=0.3)

    def __submit(self):
        result=messagebox.askyesno("Add Devices", "Are you sure?")
        if result==1:self.__submitConfirm()


    def __submitConfirm(self):
        self.__string_total = self.__entry_total.get()
        check=self.__checkValidAmount()
        if check==1:
            devices= Devices()
            list={}
            list["Name"]=self.__name
            list["Total"]=self.__string_total
            list["Remained"]=self.__string_total
            new_list=devices.updateTotalRemained(list)
            check=database.addDevice(new_list)
            if check==TRUE:
                devices.addDevices(new_list)
                controlDevices = ControlDevices(self.__masterControlDevices)
                controlDevices.mainMenu()
                self.__closeAddDevicesWin()
            else: messagebox.showwarning("Add devices","Something wrong in adding devices!")
        else:
            messagebox.showwarning("Add devices", "Invalid Amount Devices!")
            self.__closeAddDevicesWin()

    def __closeAddDevicesWin(self):
        self.__master.destroy()

    def __checkValidAmount(self):
        count=0
        for i in range(len(self.__string_total)):
            if ord(self.__string_total[i])>= 48 and ord(self.__string_total[i])<=57: count+=1
        if count==len(self.__string_total) and len(self.__string_total)!=0: return 1
        else: return 0

#-------------------------------------------------------------------------------------------------------
class AddNewDevicesWin:
    def __init__(self, master, master_controlDevices):
        self.__master = master
        self.__masterControlDevices=master_controlDevices
        canvas = Canvas(self.__master, height=250, width=300)
        canvas.pack()

    def mainMenu(self):
        self.__nameDevices()
        self.__amountDevices()
        self.__submitButton()
        self.__backButton()



    def __nameDevices(self):
        self.__label_name = Label(self.__master, text="Name Device: ", font=("times new roman", 10), anchor='w',bg='#ffffff')
        self.__label_name.place(relx=0.025, rely=0.25, relheight=0.08, relwidth=0.25)

        self.__entry_name = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_name.place(relx=0.3, rely=0.25, relwidth=0.65, relheight=0.1)

    def __amountDevices(self):
        self.__label_total = Label(self.__master, text="Amount: ", font=("times new roman", 10), anchor='w',bg='#ffffff')
        self.__label_total.place(relx=0.025, rely=0.4, relheight=0.08, relwidth=0.25)

        self.__entry_total = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_total.place(relx=0.3, rely=0.4, relwidth=0.65, relheight=0.1)

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__closeAddDevicesWin, bd=4,font=("time new roman", 10, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.5, rely=0.8, relheight=0.15, relwidth=0.25)

    def __submitButton(self):
        self.__submit_button = Button(self.__master, text="Submit", command=self.__submit, bd=4,font=("time new roman", 10, 'bold'), fg='#ffffff', bg='#00b386')
        self.__submit_button.config(relief=RAISED)
        self.__submit_button.place(relx=0.25, rely=0.8, relheight=0.15, relwidth=0.25)

    def __submit(self):
        result=messagebox.askyesno("Add Devices", "Are you sure?")
        if result==1:self.__submitConfirm()


    def __submitConfirm(self):
        self.__string_name = self.__entry_name.get()
        self.__string_total = self.__entry_total.get()
        check_name=self.__checkVaildName()
        if check_name==0:
            check_amount=self.__checkValidAmount()
            if check_amount==0:
                devices= Devices()
                list={}
                list["Name"]=self.__string_name
                list["Total"] = self.__string_total
                list["Remained"] = self.__string_total
                check=database.addDevice(list)
                if check != FALSE:
                    devices.addDevices(list)
                    controlDevices = ControlDevices(self.__masterControlDevices)
                    controlDevices.mainMenu()
                    self.__closeAddDevicesWin()
                else: messagebox.showwarning("Add devices","Something fail in adding devices!")
            else:
                messagebox.showwarning("Add devices", "Invalid Amount Devices!")
                self.__closeAddDevicesWin()
        else:
            messagebox.showwarning("Add New Devices","Invalid Name")
            self.__closeAddDevicesWin()

    def __closeAddDevicesWin(self):
        self.__master.destroy()

    def __checkValidAmount(self):
        count=0
        for i in range(len(self.__string_total)):
            if ord(self.__string_total[i])>= 48 and ord(self.__string_total[i])<=57: count+=1
        if count==len(self.__string_total) and len(self.__string_total)!=0: return 0
        else: return 1

    def __checkVaildName(self):
        devices=Devices()
        if len(self.__string_name)!=0 and devices.checkExistdevices(self.__string_name)==0: return 0
        else: return 1
#-------------------------------------------------------------------------------------------------------

class DeleteDevicesWin:
    def __init__(self, master, master_controlDevicesWin, name):
        self.__master = master
        self.__masterControlDevicesWin = master_controlDevicesWin
        self.__name=name
        canvas = Canvas(self.__master, height=100, width=200)
        canvas.pack()


    def mianMenu(self):
        self.__amount()
        self.__submitButton()
        self.__backButton()

    def __amount(self):
        self.__label_amount = Label(self.__master, text="Amount: ", font=("times new roman", 13), anchor='w', bg='#ffffff')
        self.__label_amount.place(relx=0.35, rely=0.1, relheight=0.2, relwidth=0.3)

        self.__entry_amount = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_amount.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.2)

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__closeAddDevicesWin, bd=4,font=("time new roman", 9, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.5, rely=0.7, relheight=0.2, relwidth=0.3)

    def __submitButton(self):
        self.__back_button = Button(self.__master, text="Submit", command=self.__submit, bd=4,font=("time new roman", 9, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.2, rely=0.7, relheight=0.2, relwidth=0.3)

    def __closeAddDevicesWin(self):
        self.__master.destroy()

    def __submit(self):
        result= messagebox.askyesno("Delete User","Are you sure")
        if result==1:
            if len(self.__entry_amount.get())!=0:
                if self.__check_amount()==2:
                    amount=self.__entry_amount.get()
                    amount=int(amount)
                    self.__submitConfirm(amount)
                elif self.__check_amount()==0:
                    messagebox.showwarning("Delete User","There is not enough devices to throw!")
                elif self.__check_amount()==1:
                    messagebox.showwarning("Delete User","Invalid amount!")
            else:
                messagebox.showwarning("Delete Devices","Invalid amount!")
                self.__closeAddDevicesWin()

    def __check_amount(self):
        devices = Devices()
        amount= int(self.__entry_amount.get())
        current= devices.getCurrent(self.__name)
        if current==0: return 0
        elif current<amount: return 1
        else: return 2

    def __submitConfirm(self, amount):
        devices = Devices()
        list={}
        list["Name"]=self.__name
        list["Total"]=str(-1*(amount))
        list["Remained"] = str(-1 * (amount))
        new_list= devices.updateTotalRemained(list)
        check=database.addDevice(new_list)
        if check==TRUE:
            devices.addDevices(new_list)
            controlDevices = ControlDevices(self.__masterControlDevicesWin)
            controlDevices.mainMenu()
            self.__closeAddDevicesWin()
        else: messagebox.showwarning("Delete devices","Something wrong occuring in deleting devices!")
#-------------------------------------------------------------------------------------------------------

class BorrowedEquipments:
    def __init__(self, master):
        self.__master= master
        self.__arrrayKey=[]

    def mainMenu(self):
        self.__arrayKey=[]
        self.add_users_frame = Frame(self.__master, bg='#ffffff')
        self.add_users_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.__checkButton()
        self.__borrowButton()
        self.__returnButton()
        self.__backButton()
        self.__scrollFrame()


    def __scrollFrame(self):
        self.__showTag=Label(self.__master,text="STT  Name", font =("time new roman", 12), bg='#ffffff', anchor='w')
        self.__showTag.place(relx=0, rely=0, relheight=0.1, relwidth=0.9)
        #----------------------------------------------------------------
        self.__scroll_frame = Frame(self.__master, bg='#ebebe0')
        self.__scroll_frame.place(relx=0, rely=0.1, relheight=0.7, relwidth=1)

        self.__scroll_barY= Scrollbar(self.__scroll_frame, orient=VERTICAL)
        self.__scroll_barY.pack(side=RIGHT, fill=Y)

        self.__scroll_barX = Scrollbar(self.__scroll_frame, orient=HORIZONTAL)
        self.__scroll_barX.pack(side=BOTTOM, fill=X)

        self.__list_box=Listbox(self.__scroll_frame,yscrollcommand = self.__scroll_barY.set, xscrollcommand= self.__scroll_barX.set)
        devices=Devices()
        list=devices.getList()
        count=0
        for i in list:
            self.__arrayKey.append("")
            self.__arrayKey[count]=list[i]["Name"]
            count+=1
            infor=str(count) + (" "*(6-len(str(count))))+":     "+list[i]["Name"]
            self.__list_box.insert(END, infor)
        self.__list_box.place(relx=0, rely=0, relheight=0.92, relwidth=0.95)
        # ----------------------------------------------------------------
        self.__scroll_barY.config(command= self.__list_box.yview)
        self.__scroll_barX.config(command=self.__list_box.xview)

    def __backToControlDevices(self):
        controlDevices = DevicesMenu(self.__master)
        controlDevices.mainMenu()

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backToControlDevices, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.7, rely=0.85, relheight=0.1, relwidth=0.2)

    def __checkButton(self):
        self.__check_button = Button(self.__master, text="Check", command=self.__checkListBorrowed, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__check_button.config(relief=RAISED)
        self.__check_button.place(relx=0.1, rely=0.85, relheight=0.1, relwidth=0.2)

    def __borrowButton(self):
        self.__check_button = Button(self.__master, text="Borrow", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', command=self.__borrowDevices)
        self.__check_button.config(relief=RAISED)
        self.__check_button.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.2)
    def __borrowDevices(self):
        askUID=messagebox.askyesno("Ask UID","Please insert your card")
        if askUID==1:
            #check=communicate.sendRequestUID()
            #uid=communicate.getUID()
            uid="82 BB 44 96"
            id=data.getIDWithRFID_UID(uid)
            if id!=0:
                cursor= self.__list_box.curselection()
                if cursor!=():
                    root= Tk()
                    rentDevices= RentDevices(root,id, self.__arrayKey[int(cursor[0])])
                    rentDevices.mainMenu()
                else:
                    messagebox.showwarning("Error","Please choose your device!")
            else: messagebox.showwarning("Rent Devices","You are not allowed to rent devices!")


    def __returnButton(self):
        self.__check_button = Button(self.__master, text="Return", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', command =self.__returnDevices)
        self.__check_button.config(relief=RAISED)
        self.__check_button.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.2)

    def __returnDevices(self):
        index=self.__list_box.curselection()
        root= Tk()
        name= self.__arrayKey[int(index[0])]
        returnBD= ReturnBorrowedDevicesWindow(root, name)
        returnBD.mainMenu()


    def __checkListBorrowed(self):
        index=self.__list_box.curselection()
        if index!=():
            index=int(index[0])
            devices=Devices()
            check=BorrowedList()
            name=self.__arrayKey[index]
            if check.checkExitList(name)==1:
                checkBEW= Tk()
                CheckBEW= CheckBorrowedEquipmentsWin(checkBEW, name)
                CheckBEW.mainMenu()
            else:
                messagebox.showinfo("Empty","This list is empty!")
        else:
            messagebox.showwarning("ERROR","Choose one one device!")
#-------------------------------------------------------------------------------------------------------
class ReturnBorrowedDevicesWindow:
    def __init__(self, root,name):
        self.__root=root
        self.__name= name
        self.__bdl = BorrowedList()
        self.__ID=""
        self.__amount=""
        self.__device=Devices()
        canvas = Canvas(self.__root, height=200, width=200)
        canvas.pack()

    def mainMenu(self):
        insert = Button(self.__root, text="Insert your card", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', command = self.__insertCardReturn)
        insert.place(relx=0, rely=0, relheight=0.5, relwidth=1)
        self.__backButton()

    def __backButton(self):
        back = Button(self.__root, text="Back", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386',command= self.__close)
        back.place(relx=0, rely=0.5, relheight=0.5, relwidth=1)

    def __insertCardReturn(self):
        # ask UID
        #check=communicate.sendRequestUID()
        #uid=communicate.getUID()
        uid="82 BB 44 96"
        id= data.getIDWithRFID_UID(uid)
        list = self.__bdl.getInforWithNameAndID(self.__name, id)
        if list!=0:
            self.__ID = id
            self.__amount=list["Amount"]
            self.__showInfor(list)
        else: messagebox.showwarning("Return Devices","There is no users in system")

    def __showInfor(self,list):
        self.__frame = Frame(self.__root, bg='#ffffff')
        self.__frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        label_DR = Label(self.__frame, text="Date Rent: ", font=("times new roman", 12), anchor='w',bg='#ffffff')
        label_DR.place(relx=0.05, rely=0.1, relheight=0.12, relwidth=0.4)
        show_DR = Label(self.__frame, text=list["Date Rent"], bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        show_DR.place(relx=0.5, rely=0.1, relheight=0.12, relwidth=0.45)

        label_DB = Label(self.__frame, text="Date Return: ", font=("times new roman", 12), anchor='w', bg='#ffffff')
        label_DB.place(relx=0.05, rely=0.29, relheight=0.12, relwidth=0.4)
        show_DB = Label(self.__frame, text=list["Date Back"], bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        show_DB.place(relx=0.5, rely=0.29, relheight=0.12, relwidth=0.45)

        label_Amount = Label(self.__frame, text="Amount: ", font=("times new roman", 12), anchor='w', bg='#ffffff')
        label_Amount.place(relx=0.05, rely=0.48, relheight=0.12, relwidth=0.4)
        show_Amount = Label(self.__frame, text=list["Amount"], bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        show_Amount.place(relx=0.5, rely=0.48, relheight=0.12, relwidth=0.45)
        self.__backInShowInfor()
        self.__returnButton()

    def __backInShowInfor(self):
        back = Button(self.__frame, text="Back", bd=4, font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386',command=self.__close)
        back.place(relx=0.5, rely=0.7, relheight=0.2, relwidth=0.3)

    def __returnButton(self):
        returnBut = Button(self.__root, text="Return", bd=4, font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386',command=self.__returnDevice)
        returnBut.place(relx=0.2, rely=0.7, relheight=0.2, relwidth=0.3)

    def __returnDevice(self):
        result= messagebox.askyesno("Return devices","Are you sure?")
        if result==1:
            list={}
            list = self.__device.getListDEviceAFterReturn(self.__name, int(self.__amount))
            check = database.addDevice(list)
            if check == TRUE:
                amount = self.__bdl.returnDevices(self.__name, self.__ID)
                self.__device.returnDevice(self.__name, amount)
                self.__close()
                messagebox.showinfo("Rent devices", "Successfully")
            else:
                messagebox.showwarning("Rent devices", "Something wrong in adding devices!")



    def __close(self):
        self.__root.destroy()


class RentDevices:
    def __init__(self,master, id, name):
        self.__ID=id
        self.__master=master
        self.__name=name
        self.__devices= Devices()
        self.__borrowedList= BorrowedList()
        canvas= Canvas(self.__master , height=170 , width= 350)
        canvas.pack()

    def mainMenu(self):
        self.__frame = Frame(self.__master, bg='#ffffff')
        self.__frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.__labelRentDate()
        self.__labelReturnDate()
        self.__amountDevices()
        self.__backButton()
        self.__submitButton()

    def __labelRentDate(self):
        self.__label_rent_date = Label(self.__master, text="Rent Date    (dd-mm-yy): ", font=("times new roman", 11), anchor='w',bg='#ffffff')
        self.__label_rent_date.place(relx=0.025, rely=0.1, relheight=0.18, relwidth=0.45)

        self.__entry_rent_date = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, disabledbackground='#595959',relief =RIDGE)
        self.__entry_rent_date.place(relx=0.5, rely=0.1, relwidth=0.1, relheight=0.18)

        self.__entry_rent_month = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, disabledbackground='#595959',relief =RIDGE)
        self.__entry_rent_month.place(relx=0.65, rely=0.1, relwidth=0.1, relheight=0.18)

        self.__entry_rent_year = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, disabledbackground='#595959',relief =RIDGE)
        self.__entry_rent_year.place(relx=0.8, rely=0.1, relwidth=0.175, relheight=0.18)

    def __labelReturnDate(self):
        self.__label_return_date = Label(self.__master, text="Return Date (dd-mm-yy): ", font=("times new roman", 11),anchor='w', bg='#ffffff')
        self.__label_return_date.place(relx=0.025, rely=0.33, relheight=0.18, relwidth=0.45)

        self.__entry_return_date = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, disabledbackground='#595959',relief =RIDGE)
        self.__entry_return_date.place(relx=0.5, rely=0.33, relwidth=0.1, relheight=0.18)

        self.__entry_return_month = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, disabledbackground='#595959',relief =RIDGE)
        self.__entry_return_month.place(relx=0.65, rely=0.33, relwidth=0.1, relheight=0.18)

        self.__entry_return_year = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, disabledbackground='#595959',relief =RIDGE)
        self.__entry_return_year.place(relx=0.8, rely=0.33, relwidth=0.175, relheight=0.18)

    def __amountDevices(self):
        self.__label_number_devices = Label(self.__master, text="Number of Devices: ", font=("times new roman", 11),anchor='w', bg='#ffffff')
        self.__label_number_devices.place(relx=0.025, rely=0.56, relheight=0.18, relwidth=0.45)

        self.__entry_number_devices = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, disabledbackground='#595959',relief =RIDGE)
        self.__entry_number_devices.place(relx=0.5, rely=0.56, relwidth=0.475, relheight=0.18)

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backToBorrowedEquipments, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.5, rely=0.8, relheight=0.15, relwidth=0.3)

    def __backToBorrowedEquipments(self):
        self.__master.destroy()

    def __submitButton(self):
        self.__back_button = Button(self.__master, text="Submit", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', command=self.__Submit)
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.2, rely=0.8, relheight=0.15, relwidth=0.3)

    def __checkDate(self):
        date_rent= int(self.__entry_rent_date.get())
        month_rent=int(self.__entry_rent_month.get())
        year_rent = int(self.__entry_rent_year.get())

        date_back = int(self.__entry_return_date.get())
        month_back = int(self.__entry_return_month.get())
        year_back = int(self.__entry_return_year.get())

        if len(self.__entry_rent_date.get()) !=2 and len(self.__entry_rent_month.get()) !=2 and len(self.__entry_rent_year.get()) !=4 and len(self.__entry_return_date.get()) !=2 and len(self.__entry_return_month.get()) !=2 and len(self.__entry_return_year.get()) !=4:
            return 0
        else:
            if year_back>year_rent: return 1
            elif year_back==year_rent:
                if month_back>month_rent: return 1
                elif month_back==month_rent:
                    if date_back>date_rent: return 1
                    else: return 0
                elif month_back<month_rent: return 0
            elif year_back<year_rent: return 0

    def __checkAmount(self):
        amount=int(self.__entry_number_devices.get())
        return self.__devices.checkAmount(amount,self.__name)

    def __Submit(self):
        result=messagebox.askyesno("Rent Devices","Are you sure?")
        if result==1:
            amount = int(self.__entry_number_devices.get())
            if self.__checkDate()==1 and self.__checkAmount()==1:
                list = {}
                list=self.__devices.getListDEviceAFterRent(self.__name,amount)
                check = database.addDevice(list)
                if check == TRUE:
                    rent_date = self.__entry_rent_date.get() + "-" + self.__entry_rent_month.get() + "-" + self.__entry_rent_year.get()
                    back_date = self.__entry_return_date.get() + "-" + self.__entry_return_month.get() + "-" + self.__entry_return_year.get()
                    self.__borrowedList.addBorrowedList(self.__name, self.__ID, rent_date, back_date, str(amount))
                    self.__devices.rentDevice(self.__name,amount)
                    self.__backToBorrowedEquipments()
                    messagebox.showinfo("Rent devices", "Successfully")
                else:
                    messagebox.showwarning("Rent devices", "Something wrong in adding devices!")
            elif self.__checkAmount()==0:
                messagebox.showwarning("Rent Devices","Invalid Amount")
            elif self.__checkDate()==0:
                messagebox.showwarning("Rent Devices","Invalid Date")
#-------------------------------------------------------------------------------------------------------
class CheckBorrowedEquipmentsWin:
    def __init__(self, master, name):
        self.__master=master
        self.__name=name
        self.__borrowedList = BorrowedList()
        canvas = Canvas(self.__master, height=MENU_HEIGHT, width=450)
        canvas.pack()


    def mainMenu(self):
        self.__backButton()
        self.__scrollFrame()

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backToBorrowedEquipments, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.4)



    def __backToBorrowedEquipments(self):
        self.__master.destroy()

    def __scrollFrame(self):
        self.__showTag = Label(self.__master, text="STT     SID        Borrowed Date     Return Date     Amount", font=("time new roman", 12), bg='#ffffff', anchor='w')
        self.__showTag.place(relx=0, rely=0, relheight=0.1, relwidth=0.9)
        # ----------------------------------------------------------------
        self.__scroll_frame = Frame(self.__master, bg='#ebebe0')
        self.__scroll_frame.place(relx=0, rely=0.1, relheight=0.7, relwidth=1)

        self.__scroll_barY = Scrollbar(self.__scroll_frame, orient=VERTICAL)
        self.__scroll_barY.pack(side=RIGHT, fill=Y)

        self.__scroll_barX = Scrollbar(self.__scroll_frame, orient=HORIZONTAL)
        self.__scroll_barX.pack(side=BOTTOM, fill=X)

        self.__list_box = Listbox(self.__scroll_frame, yscrollcommand=self.__scroll_barY.set,xscrollcommand=self.__scroll_barX.set)
        list = self.__borrowedList.getListWithName(self.__name)
        count = 0
        for i in list:
            count += 1
            name=i
            date_rent=list[i]["Date Rent"]
            date_back=list[i]["Date Back"]
            amount=list[i]["Amount"]
            infor = str(count) + (" " * (6 - len(str(count)))) + ":     " + name+"       :       "+date_rent+"          :          "+date_back+"          :          "+amount
            self.__list_box.insert(END, infor)
        self.__list_box.place(relx=0, rely=0, relheight=0.92, relwidth=0.95)
        # ----------------------------------------------------------------
        self.__scroll_barY.config(command=self.__list_box.yview)
        self.__scroll_barX.config(command=self.__list_box.xview)


data = Data()
database = Data()
database = MyFirebase("smartsystem.hcmut@gmail.com", "ktmtbk2017")
root= Tk()
#communicate= SendToArduino("0")
SignInScreen = SignIn(root)
SignInScreen.SignInScreen()


def loopGUI():
    root.mainloop()

# def Receive():
#     count=0
#     print("start")
#     while count<1000:
#         time.sleep(0.01)
#         count=count+1
#     print("end")

if __name__=="__main__":
    # p1 = Process(target=Receive)
    # p1.start()
    p2=Process(target=loopGUI)
    p2.start()

    








