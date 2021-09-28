from tkinter import*
from tkinter import messagebox,ttk
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import *  
import pymysql
class Login_window:
    def __init__(self,root):    # This Constructor is used for working on our window
        self.root=root
        self.root.title("LOGIN FORM")  #---------Set the Title of Window.
        self.root.geometry("1400x750+0+0")   #---------Set the dimensions(size) of Window
        self.root.config(bg="#00001A")        #---------Set the Background colour of Window

        title = Label(self.root,text=" ",font=("Trebuchet",50,"bold"),fg="white",bg="#00001A").place(x=0,y=50,relwidth=1)   #----------To give the heading label to the page.

        #========BACKGROUND COLOURS========== 
        left_lbl=Label(self.root,bg="#08A3D2")
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        right_lbl=Label(self.root,bg="#031F3C")
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)
        #========FOR FRAME==========
        login_frame = Frame(self.root,bg="white")
        login_frame.place(x=260,y=140,width=900,height=550)

        title = Label(login_frame,text="LOGIN HERE",font=("Trebuchet",30,"bold"),bg="white",fg="#33002A") 
        title.place(x=250,y=50)

        #------------For Labels and Text Field-------------
        email = Label(login_frame,text="Email ID",font=("Trebuchet",20,"bold"),bg="white",fg="#001A4D") 
        email.place(x=250,y=150)
        self.txt_email =  Entry(login_frame,font = ("Trebuchet",15),bg = "lightgray")
        self.txt_email.place(x=250,y=200,height=35,width=350)
        password = Label(login_frame,text="Password",font=("Trebuchet",20,"bold"),bg="white",fg="#001A4D") 
        password.place(x=250,y=250)
        self.txt_password = Entry(login_frame,font = ("Trebuchet",15),bg = "lightgray",show="*")
        self.txt_password.place(x=250,y=300,height=35,width=350)

        #-------------For Buttons--------------
        btn_log = Button(login_frame,text="Log In",font=("Trebuchet",20,"bold"),command=self.login,bg="#B00857",fg="white",bd=1,cursor="hand2")
        btn_log.place(x=250,y=380,width=180,height=45)  #===command=self.login :-- Used for calling the function  
                                                                        # in log button,so that button will work=====
                                                                        
        btn_reg= Button(login_frame,text="New User ? Register Here",font=("Trebuchet",13,"bold"),command=self.register_window,bg="white",fg="#800000",bd=0,cursor="hand2")
        btn_reg.place(x=235,y=440,width=220)
        btn_Fpassword = Button(login_frame,text="Forgot Password ?",font=("Trebuchet",13,"bold"),command=self.forget_pass,bg="white",fg="#1919FF",bd=0,cursor="hand2")
        btn_Fpassword.place(x=230,y=340,width=180)

        #========FOR CLOCK==========
        self.lbl=Label(self.root,text=("\nWelcome User"),font=("Book Antiqua",30,"bold"),fg="white",compound=BOTTOM,bg="#00001A",bd=0)
        self.lbl.place(x=90,y=190,height=450,width=350)
        self.working()


    
        #----------------For Forget Password------------

    def forget_pass(self):
        self.root2 = Toplevel()
        self.root2.title("Forgot Password")  #---------Set the Title of Window.       
        self.root2.geometry("600x650+450+80")   #---------Set the dimensions(size) of Window
        self.root2.config(bg="#FFEECC") 
        self.root2.focus_force()    #-------- .focus_force() will keep focus on this window ..will highlight this window.over the old window root1.
        self.root2.grab_set()       #-------- .grab_set() will grab the window . Means that window will not close untill we click on CROSS button
        title_window2 = Label(self.root2,text="Forgot Password",font=("Trebuchet",25,"bold"),bg="#FFEECC",fg="#00001A")
        title_window2.place(x=-10,y=10,height=100,relwidth=1)

        self.lbl_email_id = Label(self.root2,text="Enter the Email",font=("Trebuchet",16,"bold"),bg="#FFEECC",fg="#001A4D")
        self.lbl_email_id.place(x=110,y=100,width=250)
        self.txt_email_id = Entry(self.root2,font = ("Trebuchet",14),bg = "lightgray")
        self.txt_email_id.place(x=165,y=130,height=28,width=250)

        btn_check2 = Button(self.root2,text="Check",font=("Trebuchet",17,"bold"),command=self.check,bg="#4DE1FF",fg="#001A4D",bd=1,cursor="hand2")
        btn_check2.place(x=210,y=170,width=150,height=40)
        

    def check(self):
        
        if self.txt_email_id.get() == "" :
            messagebox.showerror("Error","This Field is Required",parent=self.root2)
        else:

            try:
                
                con = pymysql.connect(host="localhost",user="root",password="root",database="employee1")
                cur = con.cursor()
                cur.execute("select * from employee_info where email=%s ",self.txt_email_id.get())
                row = cur.fetchone()

                if row == None :
                    messagebox.showerror("Error","User not Found",parent=self.root2)
                else :

                    question = Label(self.root2,text="Security Question",font=("Trebuchet",16,"bold"),bg = "#FFEECC",fg = "#001A4D")
                    question.place(x=163,y=230)
                    self.cmb_question = ttk.Combobox(self.root2,font = ("Trebuchet",14),state='readonly',justify=CENTER,cursor="hand2")
                    self.cmb_question['values']=("Select","Your First Pet Name","Your School Name","Your Birth Place","Your Best Friend's Name","Your Favourite Place to Visit")
                    self.cmb_question.place(x=165,y=260,height=28,width=250)
                    self.cmb_question.current(0)
                
                    answer = Label(self.root2,text="Answer",font=("Trebuchet",16,"bold"),bg = "#FFEECC",fg = "#001A4D")
                    answer.place(x=163,y=310)
                    self.txt_answer = Entry(self.root2,font = ("Trebuchet",14),bg = "lightgray")
                    self.txt_answer.place(x=165,y=340,height=28,width=250)

                    self.lbl_pass = Label(self.root2,text="Password",font=("Trebuchet",16,"bold"),bg = "white",fg = "#001A4D")
                    self.lbl_pass.place(x=163,y=390)
                    self.txt_pass = Entry(self.root2,font = ("Trebuchet",14),bg = "lightgray",show='*')      #====To Create Entry Field======
                    self.txt_pass.place(x=165,y=420,width=250)


                    self.lbl_cpass = Label(self.root2,text="Confirm Password",font=("Trebuchet",16,"bold"),bg = "white",fg = "#001A4D")
                    self.lbl_cpass.place(x=163,y=470)
                    self.txt_cpass =  Entry(self.root2,font = ("Trebuchet",14),bg = "lightgray",show='*')
                    self.txt_cpass.place(x=165,y=500,width=250)

                    btn_reset = Button(self.root2,text="RESET",font=("Trebuchet",20,"bold"),command=self.reset,bg="#00308F",fg="#edfaf5",bd=1,cursor="hand2")
                    btn_reset.place(x=190,y=570,width=180,height=40)
                    
                    
                con.close()
            except Exception as es :
                messagebox.showerror("Error",f"Error due to: {str(es) }",parent=self.root2)
        

    def reset(self):
        if self.txt_pass.get() != self.txt_cpass.get() :
            messagebox.showerror("Error","Password in both the Fields must be Same",parent=self.root2)
            
        else :
            try:
                con = pymysql.connect(host="localhost",user="root",password="root",database="employee1")
                cur = con.cursor()
                cur.execute("select * from employee_info where email=%s and question=%s and answer=%s",
                            (self.txt_email_id.get(),
                            self.cmb_question.get(),
                            self.txt_answer.get()))
                row = cur.fetchone()
                print(row)

                if row == None :
                    messagebox.showerror("Error","Invalid Data !! Please Enter Correct Data",parent=self.root2)
                else :
                    cur.execute("update employee_info set password=%s where email=%s",(self.txt_pass.get(),self.txt_email_id.get()))    
                    
                    messagebox.showinfo("Success","Password Changed Successfully",parent=self.root2)
                    con.commit()
                    con.close()
                    self.root2.destroy() 
            except Exception as es :
                messagebox.showerror("Error",f"Error due to: {str(es) }",parent=self.root2)
        


    def clear(self):                               #------To clear all the fields after Login Success
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        
    def register_window(self):      #===Now we will call this function in the Register Button whixh we have created above=====
        self.root.destroy()
        import REGISTRATION
        
    
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
                messagebox.showerror("Errror","All Fields are Required",parent=self.root)
        else:    
                
            try:
                con = pymysql.connect(host="localhost",user="root",password="root",database="employee1")
                cur = con.cursor()
                cur.execute("select * from employee_info where email=%s and password=%s",(self.txt_email.get() , self.txt_password.get()))
                row = cur.fetchone()
                print(row)
                if row ==None :
                    messagebox.showerror("Error","Invalid Email or Password",parent=self.root)
                    
                     

                else :
                    messagebox.showinfo("Success","Login Successful",parent=self.root)
                    
                    self.clear() #------ it will close the window

                    
                con.close()     #=======Database Connection closed here===#

            except Exception as es :
                messagebox.showerror("Error",f"Error due to: {str(es) }",parent=self.root)





        #-------Clock Coding----------

    def clock_image(self,hr,mint,sec):
        clock = Image.new("RGB",(400,400),(0,0,26))
        draw = ImageDraw.Draw(clock)

        #========For Create Clock Image 
        bg = Image.open("C://Users//Saumitra//Python//login with database//Login-Registration System//Clock File//images//Clocks.png")
        bg = bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        #---Formula to Rotate the AntiClock
        # angle_in_radians = angle_in_degrees * math.pi/180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = center_x + line_lenth * math.cos(angle_in_radians)
        # end_y = center_y -= line_lenth * math.sin(angle_in_radians)
       
        #========For Hour Hand Image
               #  x1 y1
        origin = 200,200  #x2                      y2                    
        draw.line((origin,200+70*sin(radians(hr)),200-70*cos(radians(hr))),fill="#664400",width=5)

        #========For Minute Hand Image
        draw.line((origin,200+95*sin(radians(mint)),200-95*cos(radians(mint))),fill="blue",width=4)

        #========For Seconds Hand Image
        draw.line((origin,200+110*sin(radians(sec)),200-110*cos(radians(sec))),fill="yellow",width=2)
        draw.ellipse((194,194,206,206),fill="#1AD5D5")
        clock.save("C://Users//Saumitra//Python//login with database//Login-Registration System//Clock File//images//clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second    
        hr = (h/11.9080)*360
        mint = (m/60)*360
        sec = (s/59.9)*360
        #print(h,m,s)
        #print(hr,mint,sec)
        self.clock_image(hr,mint,sec)
        self.img = ImageTk.PhotoImage(file="C://Users//Saumitra//Python//login with database//Login-Registration System//Clock File//images//clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(30,self.working)

    
root=Tk()
obj=Login_window(root)   
root.mainloop()