import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import KeyGeneration
import EncryptDecrypt
LARGE_FONT= ("Verdana", 12)
parent_dir=os.getcwd()+"/Database/"
s="This is a Deffie Hellman key exchange based AES 32bit Encryption and Decryption program\n\n\n\n Made by Ashutosh Rawat"
def mk():
    if(not(os.path.isdir("Database"))):
        os.mkdir("Database")
mk()
def frame():
    class TextEncrpytion(tk.Tk):

        def __init__(self, *args, **kwargs):
        
            tk.Tk.__init__(self, *args, **kwargs)
            container = tk.Frame(self)
            container.pack(side="top", fill="both", expand = True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)
            self.frames = {}
            for F in (main_screen, register_screen, login_screen,main):
                frame = F(container, self)
                self.frames[F] = frame
                self.geometry("700x400")
                frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(main_screen)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

    class main_screen(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)
            label = tk.Label(self, text="Select Your Choice",bg="light green", font=LARGE_FONT,width=680,height=2)
            label.pack(pady=10,padx=10)

            button = tk.Button(self, text="Login",command=lambda: controller.show_frame(login_screen),height="2", width="30")
            button.place(anchor="c",relx=.5, rely=.3)

            button2 = tk.Button(self, text="Register",command=lambda: controller.show_frame(register_screen),height="2", width="30")
            button2.place(anchor="c",relx=.5, rely=.5)

            button3 = tk.Button(self, text="Exit",bg="red",command=self.e,height="2", width="30")
            button3.place(anchor="c",relx=.5, rely=.7)
    
        def e(self):
            exit()

    class main(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self,parent)
            labelframe1=tk.LabelFrame(self,text="About ",height=380,width=200).place(x=10,y=10)
            labelframe2=tk.LabelFrame(self,text="File Encryption: ",height=175,width=470).place(x=220,y=10)
            labelframe3=tk.LabelFrame(self,text="File Decryption: ",height=185,width=470).place(x=220,y=205)

            self.galf=0
            self.flag=0
            self.i=tk.StringVar(self)
            self.file1=tk.StringVar(self)
            self.v1=tk.StringVar(self)
            self.user=tk.StringVar(self)
            self.key1=tk.StringVar(self)
            self.getuser()
            self.listus=[]
            self.listus.append(self.user)
            if (os.listdir(parent_dir))==0:
                pass
            else:
                for x in os.listdir(parent_dir):
                    if x is not self.user:
                        self.listus.append(x)
            self.v1.set(self.listus[0])
       

            inputEncFile = tk.Label(self, text="1. Select the File:").place(x=230,y=50)
            inputEncFileEntry = tk.Entry(self,width=44,textvariable=self.i).place(x=325,y=50)
            inputEncBtn = tk.Button(self, text="Browse ...",width=10, height=1,command=self.openfileEnc).place(x=600,y=46)
            recEncFile = tk.Label(self, text="2. Select the Reciver:").place(x=230,y=90)
            reclistBtn=tk.OptionMenu(self,self.v1,*self.listus).place(x=340,y=87,width=100)
            keyEncFile = tk.Label(self, text="3. Generate secret:").place(x=230,y=130)
            keyBtn=tk.Button(self,text="Input Key", height=1,command=self.keygenerator).place(x=340,y=130,width=100)
            EncryptBTN=tk.Button(self,text="Encrypt",width=20, height=3,bg="green",command=self.encrypt).place(anchor="c",relx=.85,rely=.35)
        
            self.v2=tk.StringVar(self)
            self.file2=tk.StringVar(self)
            self.j=tk.StringVar(self)
            self.v2.set(self.listus[0])
            self.key2=tk.StringVar(self)

            inputDencFile1 = tk.Label(self, text="1. Select the File:").place(x=230,y=250)
            inputDencFileEntry1 = tk.Entry(self,width=45,textvariable=self.j).place(x=325,y=250)
            inputDencBtn = tk.Button(self, text="Browse ...",width=10, height=1,command=self.openfileDec).place(x=600,y=246)
            inputDencFile = tk.Label(self, text="2. Select the Sender:").place(x=230,y=290)
            listBtn=tk.OptionMenu(self,self.v2,*self.listus).place(x=350,y=286,width=100)
            keyEncFile = tk.Label(self, text="3. Generate secret:").place(x=230,y=330)
            keyBtn=tk.Button(self,text="Input Key", height=1,command=self.keygeneratorD).place(x=350,y=326,width=100)
            keyBtn2=tk.Button(self,text="Decrypt",width=20, height=3,bg="red",command=self.decrypt).place(anchor="c",relx=.85,rely=.85)
    
            keyBtn3=tk.Button(self,text="Log out",width=10, height=2,command=lambda: controller.show_frame(main_screen)).place(x=20,y=330)
            keyBtn4=tk.Button(self,text="Exit",width=10,height=2,command=self.e,bg="red").place(x=120,y=330)
            message=tk.Message(self,text=s,width=180).place(x=20,y=30)
        def keygenerator(self):
            y=self.v1.get()
            self.key1=KeyGeneration.generate_partial_key(parent_dir,self.user,y)
            messagebox.showinfo("Success", self.key1)
       
        def keygeneratorD(self):
            y=self.v2.get()
            self.key2=KeyGeneration.generate_partial_key(parent_dir,self.user,y)
            messagebox.showinfo("Success", self.key2)

        def e(self): 
            exit()
   
        def openfileEnc(self):
            filename=filedialog.askopenfile(initialdir=os.path.join(parent_dir,self.user),title="Select file",filetype=(("text files",".txt"),("all files","*.*")))
            if filename is None:
                self.flag=0
                self.file1=""
                self.i.set("No File Selected")
            else:
                self.flag=1
                self.file1= filename.name
                self.i.set(self.file1)
    
        def openfileDec(self):
            filename=filedialog.askopenfile(initialdir=os.path.join(parent_dir,self.user),title="Select file",filetype=(("text files",".txt"),("all files","*.*")))
            if filename is None:
                self.galf=0
                self.file2=""
                self.j.set("No File Selected")
            else:
                self.galf=1
                self.file2= filename.name
                self.j.set(self.file2)
   
        def getuser(self):
            file=open("user","r")
            user=file.read()
            file.close()
            self.user= user 

        def encrypt(self):
            if self.flag==1:
                EncryptDecrypt.encrypt_message(parent_dir,self.key1,self.file1,self.v1.get())
                messagebox.showinfo("Success","Encrption Complete")
            else:
                messagebox.showwarning("Error","Complete all Steps First")

        def decrypt(self):
            if self.galf==1:
                text=EncryptDecrypt.decrypt_message(parent_dir,self.key2,self.file2,self.user)
                messagebox.showinfo("Succes",text)
            else:
                messagebox.showwarning("Error","Complete all Steps First")

    class login_screen(tk.Frame):

        def __init__(self, parent, controller):
            self.controller=controller
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Login", font=LARGE_FONT,bg="blue",width=680,height=2)
            label.pack(pady=10,padx=10)

            tk.Label(self, text="Please Enter details below to login",bg="blue").place(anchor="c",relx=.5,rely=.2)
 
            global username_verify
            global password_verify
            username_verify = tk.StringVar()
            password_verify = tk.StringVar()
            global username_login_entry
            global password_login_entry
 
            tk.Label(self, text="Username * ").place(anchor="c",relx=.4,rely=.3)
            username_login_entry = tk.Entry(self, textvariable=username_verify).place(anchor="c",relx=.55,rely=.3)
            tk.Label(self, text="Password * ").place(anchor="c",relx=.4,rely=.4)
            password_login_entry = tk.Entry(self, textvariable=password_verify, show= '*').place(anchor="c",relx=.55,rely=.4)

            tk.Button(self, text="Login", width=10, height=1,bg="blue", command =self.login_verify).place(anchor="c",relx=.4,rely=.5)
            tk.Button(self, text="Back",width=10, height=1,bg="red",command=lambda: controller.show_frame(main_screen)).place(anchor="c",relx=.6,rely=.5)

        def login_verify(self):
            username1 = username_verify.get()
            password1 = password_verify.get()
            path=os.path.join(parent_dir,username1)
            list_of_files = os.listdir(parent_dir)
            if username1 in list_of_files:
                file1 = open(os.path.join(path,username1), "r")
                verify = file1.read().splitlines()
                file1.close()
                if password1 in verify:
                    self.login_sucess()
                else:
                    self.password_not_recognised()
            else:
                self.user_not_found()

        def login_sucess(self):
            global login_success_screen
            login_success_screen = tk.Tk()
            login_success_screen.title("Success")
            login_success_screen.geometry("150x100")
            tk.Label(login_success_screen, text="Login Success",fg="green").pack()
            tk.Button(login_success_screen, text="OK", command=self.two).pack()
    
        def two(self):
            user=username_verify.get()
            file=open("user","w")
            file.write(user)
            file.close()
            self.controller.show_frame(main)
            login_success_screen.destroy()
 
        def password_not_recognised(self):
            messagebox.showwarning("Log In"," Invalid Password ")
        
        def user_not_found(self):
            messagebox.showwarning("Log In","User Not Found")
 
    class register_screen(tk.Frame):

        def __init__(self, parent, controller):
            self.controller=controller
            tk.Frame.__init__(self, parent)
            label = tk.Label(self, text="Register",bg="blue" ,font=LARGE_FONT,width=680,height=2)
            label.pack(pady=10,padx=10)
 
            global username
            global password
            username = tk.StringVar()
            password = tk.StringVar()

            tk.Label(self, text="Please enter details below", bg="blue").place(anchor="c",relx=.5, rely=.2)
            username_lable = tk.Label(self, text="Username * ").place(anchor="c",relx=.4, rely=.3)
            username_entry = tk.Entry(self,textvariable=username).place(anchor="c",relx=.55, rely=.3)
            password_lable = tk.Label(self, text="Password * ").place(anchor="c",relx=.4, rely=.4)
            password_entry = tk.Entry(self,textvariable=password, show='*').place(anchor="c",relx=.55, rely=.4)
            tk.Button(self, text="Register", width=10, height=1, bg="blue", command=self.register_verify).place(anchor="c",relx=.4, rely=.5)
            tk.Button(self, text="Back",bg="red", width=10, height=1,command=lambda: controller.show_frame(main_screen)).place(anchor="c",relx=.6, rely=.5)
    
        def register_verify(self):
            username1 = username.get()
            password1 = password.get()
            list_of_files = os.listdir(parent_dir)
            if username1 in list_of_files:
                self.username_exist()
            else:
                if not username1 or not password1:
                    self.enter_username()
                else:
                    self.register_success()

        def username_exist(self):
            messagebox.showwarning("Register","User Name Exits")

        def enter_username(self):
            messagebox.showwarning("Register","Enter username and password")

        def register_success(self):
            username_info = username.get()
            password_info = password.get()
            path = os.path.join(parent_dir, username_info)
            os.mkdir(path)
            file = open(os.path.join(path, username_info),"w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()
            KeyGeneration.generate_private_key(path)

            global register_success_screen
            register_success_screen = tk.Tk()
            register_success_screen.title("Success")
            register_success_screen.geometry("150x100")
            tk.Label(register_success_screen, text="Successfuly Registered",fg="green").pack()
            tk.Button(register_success_screen, text="OK", command=self.one).pack()

        def one(self):
            register_success_screen.destroy()
            self.controller.show_frame(main_screen)
 
        def delete_register_success(self):
            regcceister_suss_screen.destroy()

    app=TextEncrpytion()
    app.update()
    app.mainloop()
frame()
