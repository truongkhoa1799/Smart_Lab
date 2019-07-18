from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from Data import Data
from Devices import Devices
from BorrowedList import BorrowedList

LENGTH_OF_PIN =4

#----------------class hoa chu dau
#----------------ham private __roi thuong chu dau, sau do la hoa, public ko co __
#----------------bien thuong het vaf cach nhau _

ADMIN_ID="123"
ADMIN_PASS="1"

MENU_HEIGHT = 300
MENU_WIDTH = 350
#-------------------------------------------------------------------------------------------------------
class MainMenu:
    def __init__(self, master):
        self.master=master

    def mainMenu(self):
        self.__main_frame = Frame(self.master, bg='#ffffff')
        self.__main_frame.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.load = Image.open("SmartLab.png")
        self.render = ImageTk.PhotoImage(self.load.resize((217, 91)))
        self.__logo = Label(self.master, image=self.render, bg='#ffffff')
        self.__logo.place(relx=0.27, rely=0)
        self.__controlUserBut()
        self.__controlLabBut()
        self.__controlDevicesBut()
        self.__logOutBut()


    def __controlUserBut(self):
        self.control_user_but = Button(self.master, bg='#00b386', text="Control User", fg='#ffffff', font =('time new roman', 18, 'bold'), command =self.__controlUser)
        self.control_user_but.place(relx=0.2, rely=0.28, relheight= 0.15, relwidth = 0.6)

    def __controlLabBut(self):
        self.control_lab_but = Button(self.master, bg='#00b386', text="Control Lab", fg='#ffffff',font=('time new roman', 18, 'bold'))
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
        self.__logo.place(relx=0.27, rely=0)
        self.__ID()
        self.__PASSWORD()
        self.__LogInBut()
        self.__SignInLogo()

    def __SignInLogo(self):
        self.__load_signinlogo = Image.open("signInID.png")
        self.__render_signinlogo = ImageTk.PhotoImage(self.__load_signinlogo)
        self.__signinlogo = Label(self.__main_frame, image=self.__render_signinlogo, bg='#ffffff')
        self.__signinlogo.place(relx=0.4, rely=0.27,relheight=0.2, relwidth=0.2)

    def __ID(self):
        self.__load_SignInID = Image.open("SignInUserLogo.png")
        self.__render_SignInID = ImageTk.PhotoImage(self.__load_SignInID)
        self.__SignInID = Label(self.__main_frame, image=self.__render_SignInID, bg='#ffffff')
        self.__SignInID.place(relx=0.1, rely=0.5, relheight=0.1, relwidth=0.1)
        self.__entry_ID=Entry(self.__main_frame, bg ='#f2f2f2', borderwidth=1.5,disabledbackground='#595959')
        self.__entry_ID.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.1)

    def __PASSWORD(self):
        self.__load_SignInPass = Image.open("SignInPass.png")
        self.__render_SignInPass = ImageTk.PhotoImage(self.__load_SignInPass)
        self.__SignInPass = Label(self.__main_frame, image=self.__render_SignInPass, bg='#ffffff')
        self.__SignInPass.place(relx=0.1, rely=0.65, relheight=0.1, relwidth=0.1)
        self.__entry_PASS = Entry(self.__main_frame,  bg='#f2f2f2', borderwidth=1.5,disabledbackground='#f2f2f2', show="*")
        self.__entry_PASS.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.1)

    def __LogInBut(self):
        self.__signin_button = Button(self.__master, bg='#00b386', text="Log In", fg='#ffffff',font=('time new roman', 20, 'bold'), command =self.__LogIn)
        self.__signin_button.place(relx=0.2, rely=0.8, relheight=0.14, relwidth=0.6)


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
        deleteUser= DeleteUser(self.__master)
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
        self.__SIDUser()
        self.__Email()
        self.__Pin()
        self.__checkPin()
        self.__Title()

    def __backButton(self):
        self.__back_button= Button(self.__master, text="Back",  command= self.__backToControlUser, bd=4,font=("time new roman", 12, 'bold'), fg ='#ffffff', bg ='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.3, rely=0.86, relheight=0.1, relwidth=0.2)

    def __submitButton(self):
        self.__submit_button = Button(self.__master, text="Submit",  command=self.__submitAddUser, bd=4,font=("time new roman", 12,'bold'), fg ='#ffffff', bg ='#00b386')
        self.__submit_button.config(relief=RAISED)
        self.__submit_button.place(relx=0.5, rely=0.86, relheight=0.1, relwidth=0.2)

    def __nameUser(self):
        self.__label_name= Label(self.__master, text ="Name:",font=("times new roman", 12),anchor= 'w', bg= '#ffffff')
        self.__label_name.place(relx=0.025, rely=0.25, relheight=0.08, relwidth=0.2)

        self.__entry_name= Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5, relief =RIDGE)
        self.__entry_name.place(relx=0.25, rely=0.25, relwidth=0.7, relheight=0.1)

    def __SIDUser(self):
        self.__label_SID = Label(self.__master, text="Student ID: ", font=("times new roman", 12),anchor= 'w',bg= '#ffffff')
        self.__label_SID.place(relx=0.025, rely=0.37, relheight=0.08, relwidth=0.2)

        self.__entry_SID = Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5, relief =RIDGE)
        self.__entry_SID.place(relx=0.25, rely=0.37, relwidth=0.7, relheight=0.1)

    def __Email(self):
        self.__label_email = Label(self.__master, text="Email:", font=("times new roman", 12),anchor= 'w',bg= '#ffffff')
        self.__label_email.place(relx=0.025, rely=0.49, relheight=0.08, relwidth=0.2)

        self.__entry_email = Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5,relief =RIDGE)
        self.__entry_email.place(relx=0.25, rely=0.49, relwidth=0.7, relheight=0.1)

    def __Pin(self):
        self.__label_pin = Label(self.__master, text="Pin(4digits):", font=("times new roman", 12), anchor= 'w',bg= '#ffffff')
        self.__label_pin.place(relx=0.025, rely=0.61, relheight=0.08, relwidth=0.2)

        self.__entry_pin = Entry(self.__master,show="*",bg ='#f2f2f2', borderwidth=1.5,relief =RIDGE)
        self.__entry_pin.place(relx=0.25, rely=0.61, relwidth=0.7, relheight=0.1)

    def __checkPin(self):
        self.__label_check_pin = Label(self.__master, text="Check Pin:", font=("times new roman", 12), anchor='w', bg='#ffffff')
        self.__label_check_pin.place(relx=0.025, rely=0.73, relheight=0.08, relwidth=0.2)

        self.__entry_check_pin = Entry(self.__master, show="*", bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_check_pin.place(relx=0.25, rely=0.73, relwidth=0.7, relheight=0.1)


    def __Title(self):
        self.__title_frame= Frame(self.__master, bg= '#00b386')
        self.__title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.22)
        self.__title=Label(self.__title_frame, text ="Add User", fg='#00b386', font =("time new roman", 30, 'bold'), bd=4, bg='#ffffff' )
        self.__title.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.76)


    def __backToControlUser(self):
        addUser=ControlUser(self.__master)
        addUser.mainMenu()

    # get the infor save in database, and send name and id to arduino, simultaneously get the iud and save in database
    def __submitAddUser(self):
        self.__string_name=self.__entry_name.get()
        self.__string_SID=self.__entry_SID.get()
        self.__string_pin=self.__entry_pin.get()
        self.__string_email=self.__entry_email.get()
        self.__string_check_pin=self.__entry_check_pin.get()
        result=messagebox.askyesno("Add User","Are you sure about your information?")
        if result ==1: self.__submitAddUserConfrim()

    def __submitAddUserConfrim(self):
        if self.__checkAddUsers()==1:
            data.addUser(self.__string_SID, self.__string_name, self.__string_email, self.__string_pin)
            messagebox.showinfo("Add Users", "Add successfully.")
            self.mainMenu()
        elif self.__checkAddUsers()==0:
            messagebox.showwarning("Add Users", "Add unsuccessfully. Please fulfill your information!")
            self.mainMenu()
        elif self.__checkAddUsers()==2:
            messagebox.showwarning("Add Users", "Add unsuccessfully. Existing an account in system!")
            self.mainMenu()
        elif self.__checkAddUsers()==3:
            messagebox.showwarning("Add Users", "Add unsuccessfully. Your SID must has 7 digits!")
            self.mainMenu()
        elif self.__checkAddUsers()==4:
            messagebox.showwarning("Add Users","Wrong password!")
            self.mainMenu()
        elif self.__checkAddUsers()==5:
            messagebox.showwarning("Add Users", "Invalid SID!")
            self.mainMenu()
        elif self.__checkAddUsers()==6:
            messagebox.showwarning("Add Users", "Invalid Email!")
            self.mainMenu()

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


    def __checkAddUsers(self):
        #check =5 invalid SID
        if self.__checkValidSID(self.__string_SID)==1:check=1
        else: check=5
        if self.__checkValidEmail(self.__string_email) == 1: check = 1
        else: check=6
        #check whether all of entry is fulfilled or not if not check =0
        if len(self.__string_email) == 0 or len(self.__string_name) == 0 or len(self.__string_pin) ==0 or len(self.__string_SID)  == 0:
            check=0
        # SID is 7 digits so if there is more or less check =3
        elif len(self.__string_SID)!=7: check=3
        # in this method, check whether the user is in the database, rematch with another
        # users about SID, email or not if yes, return check =2
        elif data.checkUser(self.__string_name, 1)==1 or data.checkUser(self.__string_SID,0)==1:
            check=2
        #check whether the pin is correct or not
        elif (self.__string_pin!=self.__string_check_pin) or len(self.__string_pin)!=LENGTH_OF_PIN:
            check=4
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
        self.__Title()
        self.__checkEntry()


    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backToControlUser, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386',relief=RAISED)
        self.__back_button.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.2)

    def __checkButton(self):
        self.__check_button = Button(self.__master, text="Check", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386', command = self.__check,relief=RAISED)
        self.__check_button.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.2)

    def __nameUser(self):
        self.label_name= Label(self.__master, text ="Name:",font=("times new roman", 12),anchor= 'w', bg= '#ffffff')
        self.label_name.place(relx=0.025, rely=0.43, relheight=0.08, relwidth=0.2)


    def __SIDUser(self):
        self.label_SID = Label(self.__master, text="Student ID: ", font=("times new roman", 12),anchor= 'w',bg= '#ffffff')
        self.label_SID.place(relx=0.025, rely=0.57, relheight=0.08, relwidth=0.2)



    def __Email(self):
        self.label_email = Label(self.__master, text="Email:", font=("times new roman", 12),anchor= 'w',bg= '#ffffff')
        self.label_email.place(relx=0.025, rely=0.71, relheight=0.08, relwidth=0.2)


    def __checkEntry(self):
        self.__entry= Entry(self.__master,bg ='#f2f2f2', borderwidth=1.5, relief =RIDGE)
        self.__entry.place(relx=0.25, rely = 0.28, relwidth = 0.75, relheight= 0.1)

        self.__option= Menubutton(text ="Options", font =("time new roman", 12), bd=4, bg='#e0e0d1', relief=RAISED)
        self.__option.place (relx=0.025, rely = 0.28, relwidth = 0.25, relheight= 0.1)
        self.__option.menu= Menu(self.__option, tearoff=0)
        self.__option["menu"]= self.__option.menu

        self.__name=IntVar()
        self.__SID=IntVar()


        self.__option.menu.add_checkbutton(label="Name", variable=self.__name)
        self.__option.menu.add_checkbutton(label="SID", variable=self.__SID)

        self.__option.place (relx=0.025, rely = 0.28, relwidth = 0.225, relheight= 0.1)

    def __check(self):
        list=[]
        if (self.__name.get()==1 and self.__SID.get()==1) or (self.__name.get()==0 and self.__SID.get()==0):
            messagebox.showwarning("Warning","Just choose one of them!")
        # check whether there is exist a user in database or not
        elif self.__name.get()==1:
            list=data.getInfor(1,self.__entry.get())
            if list!=[]:
                self.__showInfor(list)
            else:messagebox.showinfo("Search User", "This user is not existed!")
        elif self.__SID.get()==1:
            list = data.getInfor(0, self.__entry.get())
            if list!=[]:
                self.__showInfor( list)
            else:messagebox.showinfo("Search User", "This user is not existed!")

    def __showInfor(self, list):
        self.__SIDUser()
        self.__Email()
        self.__nameUser()

        self.show_SID = Label(self.__master,text=list[0], bg='#f2f2f2', borderwidth=1.5, relief=RIDGE, font=("time new roman", 12))
        self.show_SID.place(relx=0.25, rely=0.57, relheight=0.08, relwidth=0.725)

        self.show_name = Label(self.__master,text=list[1], bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        self.show_name.place(relx=0.25, rely=0.43, relheight=0.08, relwidth=0.725)

        self.show_Email = Label(self.__master,text=list[2], bg='#f2f2f2', borderwidth=1.5, relief=RIDGE,font=("time new roman", 12))
        self.show_Email.place(relx=0.25, rely=0.71, relheight=0.08, relwidth=0.725)

    def __Title(self):
        self.__title_frame = Frame(self.__master, bg='#00b386')
        self.__title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.22)
        self.__title = Label(self.__title_frame, text="Check User", fg='#00b386', font=("time new roman", 30, 'bold'), bd=4,bg='#ffffff')
        self.__title.place(relx=0.02, rely=0.12, relwidth=0.96, relheight=0.76)

    def __backToControlUser(self):
        addUser = ControlUser(self.__master)
        addUser.mainMenu()
#-------------------------------------------------------------------------------------------------------

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
        self.__label_SID = Label(self.__master, text="Student ID: ", font=("times new roman", 12), anchor='w', bg='#ffffff')
        self.__label_SID.place(relx=0.025, rely=0.35, relheight=0.08, relwidth=0.2)

        self.__entry_SID = Entry(self.__master, bg ='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_SID.place(relx=0.25, rely=0.35, relwidth=0.7, relheight=0.1)

    def __entrypass(self):
        self.__label_pass = Label(self.__master, text="New Key: ", font=("times new roman", 12), anchor='w', bg='#ffffff')
        self.__label_pass.place(relx=0.025, rely=0.55, relheight=0.08, relwidth=0.2)

        self.__entry_pass = Entry(self.__master, bg ='#f2f2f2', borderwidth=1.5, relief=RIDGE, show="*")
        self.__entry_pass.place(relx=0.25, rely=0.55, relwidth=0.7, relheight=0.1)

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
    def mainMenu(self):
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
        self.__showTag=Label(self.__master,text="STT  SID        Name                        Email", font =("time new roman", 12), bg='#ffffff', anchor='w')
        self.__showTag.place(relx=0, rely=0, relheight=0.1, relwidth=0.9)
        #----------------------------------------------------------------
        self.__scroll_frame = Frame(self.__master, bg='#ebebe0')
        self.__scroll_frame.place(relx=0, rely=0.1, relheight=0.7, relwidth=1)

        self.__scroll_barY= Scrollbar(self.__scroll_frame, orient=VERTICAL)
        self.__scroll_barY.pack(side=RIGHT, fill=Y)

        self.__scroll_barX = Scrollbar(self.__scroll_frame, orient=HORIZONTAL)
        self.__scroll_barX.pack(side=BOTTOM, fill=X)

        self.__list_box=Listbox(self.__scroll_frame,yscrollcommand = self.__scroll_barY.set, xscrollcommand= self.__scroll_barX.set)
        list=data.getList()
        count=0
        for i in list:
            count+=1
            infor=str(count) + (" "*(6-len(str(count))))+":     "+i[0]+"  :  "+i[1]+("  "*(20-len(i[1])))+":"+("  "*4)+i[2]
            self.__list_box.insert(END, infor)
        self.__list_box.place(relx=0, rely=0, relheight=0.92, relwidth=0.95)
        # ----------------------------------------------------------------
        self.__scroll_barY.config(command= self.__list_box.yview)
        self.__scroll_barX.config(command=self.__list_box.xview)

    def __backToControlUser(self):
        addUser=ControlUser(self.__master)
        addUser.mainMenu()

    def __deleteUser(self):
        result=messagebox.askyesno("Delete User", "Are you sure to delete this user?")
        if result==1: self.__deleteConfirm()

    def __deleteConfirm(self):
        index=self.__list_box.curselection()
        if index!=():
            self.__list_box.delete(index,index)
            data.deleteUser(index[0])
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

class ControlDevices:
    def __init__(self, master):
        self.__master=master
    def mainMenu(self):
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
            name=devices.getNameWithIndex(index)
            addWin=Tk()
            addDevicesWin= AddDevicesWin(addWin,self.__master, name)
            addDevicesWin.mainMenu()
        else:
            addWin = Tk()
            addDevicesWin = AddNewDevicesWin(addWin, self.__master)
            addDevicesWin.mainMenu()

    def __deleteDevicces(self):
        index_delete = self.__list_box.curselection()
        if index_delete!=():
            deleteWin = Tk()
            index=index_delete[0]
            deleteDevicesWin= DeleteDevicesWin(deleteWin, self.__master, index)
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
            count+=1
            infor=str(count) + (" "*(6-len(str(count))))+":     "+i[0]+("  "*(16-len(i[0])))+":"+("  "*(7-len(i[1])))+i[1]+("  "*(8-len(i[1])))+":"+("  "*(8-len(i[2])))+i[2]
            self.__list_box.insert(END, infor)
        self.__list_box.place(relx=0, rely=0, relheight=0.92, relwidth=0.95)
        # ----------------------------------------------------------------
        self.__scroll_barY.config(command= self.__list_box.yview)
        self.__scroll_barX.config(command=self.__list_box.xview)



    def __backToControlDevices(self):
        devices= DevicesMenu(self.__master)
        devices.mainMenu()

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
        self.__label_amount = Label(self.__master, text="Amount: ", font=("times new roman", 13), anchor='w',bg='#ffffff')
        self.__label_amount.place(relx=0.35, rely=0.1, relheight=0.2, relwidth=0.3)

        self.__entry_amount = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_amount.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.2)

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
        self.__string_amount = self.__entry_amount.get()
        check=self.__checkValidAmount()
        if check==1:
            devices= Devices()
            devices.addDevices(self.__name, self.__string_amount)
            controlDevices = ControlDevices(self.__masterControlDevices)
            controlDevices.mainMenu()
            self.__closeAddDevicesWin()
        else:
            messagebox.showwarning("Add devices", "Invalid Amount Devices!")
            self.__closeAddDevicesWin()

    def __closeAddDevicesWin(self):
        self.__master.destroy()

    def __checkValidAmount(self):
        count=0
        for i in range(len(self.__string_amount)):
            if ord(self.__string_amount[i])>= 48 and ord(self.__string_amount[i])<=57: count+=1
        if count==len(self.__string_amount) and len(self.__string_amount)!=0: return 1
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
        self.__label_AD = Label(self.__master, text="Amount: ", font=("times new roman", 10), anchor='w',bg='#ffffff')
        self.__label_AD.place(relx=0.025, rely=0.4, relheight=0.08, relwidth=0.25)

        self.__entry_AD = Entry(self.__master, bg='#f2f2f2', borderwidth=1.5, relief=RIDGE)
        self.__entry_AD.place(relx=0.3, rely=0.4, relwidth=0.65, relheight=0.1)

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
        self.__string_AD = self.__entry_AD.get()
        check_name=self.__checkVaildName()
        if check_name==1:
            check_amount=self.__checkValidAmount()
            if check_amount==1:
                devices= Devices()
                devices.addDevices(self.__string_name, self.__string_AD)
                controlDevices = ControlDevices(self.__masterControlDevices)
                controlDevices.mainMenu()
                self.__closeAddDevicesWin()
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
        for i in range(len(self.__string_AD)):
            if ord(self.__string_AD[i])>= 48 and ord(self.__string_AD[i])<=57: count+=1
        if count==len(self.__string_AD) and len(self.__string_AD)!=0: return 1
        else: return 0

    def __checkVaildName(self):
        name=self.__entry_name.get()
        if len(name)==0: return 0
        else: return 1
#-------------------------------------------------------------------------------------------------------

class DeleteDevicesWin:
    def __init__(self, master, master_controlDevicesWin, index):
        self.__master = master
        self.__masterControlDevicesWin = master_controlDevicesWin
        self.__index_delete=index
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
        current= devices.getCurrent(self.__index_delete)
        if current==0: return 0
        elif current<amount: return 1
        else: return 2

    def __submitConfirm(self, amount):
        devices= Devices()
        devices.deteleDevices(self.__index_delete, amount)
        controlDevices = ControlDevices(self.__masterControlDevicesWin)
        controlDevices.mainMenu()
        self.__closeAddDevicesWin()
#-------------------------------------------------------------------------------------------------------

class BorrowedEquipments:
    def __init__(self, master):
        self.__master= master

    def mainMenu(self):
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
            count+=1
            infor=str(count) + (" "*(6-len(str(count))))+":     "+i[0]
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
        self.__check_button = Button(self.__master, text="Borrow", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__check_button.config(relief=RAISED)
        self.__check_button.place(relx=0.3, rely=0.85, relheight=0.1, relwidth=0.2)

    def __returnButton(self):
        self.__check_button = Button(self.__master, text="Return", bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__check_button.config(relief=RAISED)
        self.__check_button.place(relx=0.5, rely=0.85, relheight=0.1, relwidth=0.2)

    def __checkListBorrowed(self):
        index=self.__list_box.curselection()
        if index!=():
            index=index[0]
            devices=Devices()
            name=devices.getNameWithIndex(index)
            check=BorrowedList()
            if check==TRUE:
                checkBEW= Tk()
                CheckBEW= CheckBorrowedEquipmentsWin(checkBEW, name)
                CheckBEW.mainMenu()
            else:
                messagebox.showinfo("Empty","This list is empty!")
        else:
            messagebox.showwarning("ERROR","Choose one one device!")


class CheckBorrowedEquipmentsWin:
    def __init__(self, master, name):
        self.__master=master
        self.__name=name
        canvas = Canvas(self.__master, height=MENU_HEIGHT, width=MENU_WIDTH)
        canvas.pack()


    def mainMenu(self):
        self.__backButton()
        self.__scrollFrame()

    def __backButton(self):
        self.__back_button = Button(self.__master, text="Back", command=self.__backToBorrowedEquipments, bd=4,font=("time new roman", 12, 'bold'), fg='#ffffff', bg='#00b386')
        self.__back_button.config(relief=RAISED)
        self.__back_button.place(relx=0.6, rely=0.85, relheight=0.1, relwidth=0.2)



    def __backToBorrowedEquipments(self):
        self.__master.destroy()

    def __scrollFrame(self):
        self.__showTag = Label(self.__master, text="STT     SID        Borrowed Date     Return Date", font=("time new roman", 12), bg='#ffffff', anchor='w')
        self.__showTag.place(relx=0, rely=0, relheight=0.1, relwidth=0.9)
        # ----------------------------------------------------------------
        self.__scroll_frame = Frame(self.__master, bg='#ebebe0')
        self.__scroll_frame.place(relx=0, rely=0.1, relheight=0.7, relwidth=1)

        self.__scroll_barY = Scrollbar(self.__scroll_frame, orient=VERTICAL)
        self.__scroll_barY.pack(side=RIGHT, fill=Y)

        self.__scroll_barX = Scrollbar(self.__scroll_frame, orient=HORIZONTAL)
        self.__scroll_barX.pack(side=BOTTOM, fill=X)

        self.__list_box = Listbox(self.__scroll_frame, yscrollcommand=self.__scroll_barY.set,xscrollcommand=self.__scroll_barX.set)
        borrowedList= BorrowedList()
        list = borrowedList.getList(self.__name)
        count = 0
        for i in list:
            count += 1
            infor = str(count) + (" " * (6 - len(str(count)))) + ":     " + i[0]+"       :       "+i[1]+"          :          "+i[2]
            self.__list_box.insert(END, infor)
        self.__list_box.place(relx=0, rely=0, relheight=0.92, relwidth=0.95)
        # ----------------------------------------------------------------
        self.__scroll_barY.config(command=self.__list_box.yview)
        self.__scroll_barX.config(command=self.__list_box.xview)







data=Data()
root= Tk()
SignInScreen = SignIn(root)
SignInScreen.SignInScreen()
root.mainloop()