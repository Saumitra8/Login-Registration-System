from tkinter import*  
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  # pip install pillow
import pymysql
from pymysql.cursors import Cursor

class Registration :
    def __init__(self,root):
        self.root = root 
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg = "#08A3D2")
       
        # root.title("Registration Form")
        # # root.geometry("300x200+10+20")

        # == Bg Image ==
        self.bg=ImageTk.PhotoImage(file = "C:\\Users\\Saumitra\\Python\\login with database\\images\\Avengers.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # == LEFT Image ==
        self.left=ImageTk.PhotoImage(file = "C:\\Users\\Saumitra\\Python\\login with database\\images\sideImage3.png")
        left=Label(self.root,image=self.left).place(x=80,y=170,width=400,height=500)


        #======= Register Frame ======

        frame1 = Frame(self.root,bg = "white")
        frame1.place(x=480,y=170,width=700,height=500)
        title = Label(frame1,text="REGISTER HERE",font=("Trebuchet",20,"bold"),bg = "white",fg = "green").place(x=50,y=30)
        
        #-------------------Row 1 : To Create First Name and Last Name 

        f_name = Label(frame1,text="First Name",font=("Trebuchet",15,"bold"),bg = "white",fg = "#001A4D").place(x=50,y=100)
        self.txt_fname = Entry(frame1,font = ("Trebuchet",15),bg = "lightgray")      #====To Create Entry Field======
        self.txt_fname.place(x=50,y=130,width=250) 
        
        
        l_name = Label(frame1,text="Last Name",font=("Trebuchet",15,"bold"),bg = "white",fg = "#001A4D").place(x=370,y=100)
        self.txt_lname =  Entry(frame1,font = ("Trebuchet",15),bg = "lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        #-------------------Row 2 : To Create Contact Number and Email

        contact = Label(frame1,text="Contact Number",font=("Trebuchet",15,"bold"),bg = "white",fg = "#001A4D").place(x=50,y=170)
        self.txt_contact =  Entry(frame1,font = ("Trebuchet",15),bg = "lightgray")      #====To Create Entry Field======
        self.txt_contact.place(x=50,y=200,width=250)
        # Contact : y = 170 ==>> We add 40 to the y = 130 of f_name Text Field to keep it in proper distance  <<=====
        
        email = Label(frame1,text="Email",font=("Trebuchet",15,"bold"),bg = "white",fg = "#001A4D").place(x=370,y=170)
        self.txt_email =  Entry(frame1,font = ("Trebuchet",15),bg = "lightgray")
        self.txt_email.place(x=370,y=200,width=250)


        # Same in the email text filed too....like Contact 

         #-------------------Row 3 : To Create Security Question and its Answer

        question = Label(frame1,text="Security Question",font=("Trebuchet",15,"bold"),bg = "white",fg = "#001A4D")
        question.place(x=50,y=240)
        self.cmb_question = ttk.Combobox(frame1,font = ("Trebuchet",12),state='readonly',justify=CENTER)
        self.cmb_question['values']=("Select","Your First Pet Name","Your School Name","Your Birth Place","Your Best Friend's Name","Your Favourite Place to Visit")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)
       
        answer = Label(frame1,text="Answer",font=("Trebuchet",15,"bold"),bg = "white",fg = "#001A4D").place(x=370,y=240)
        self.txt_answer = Entry(frame1,font = ("Trebuchet",15),bg = "lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        
       
        #-------------------Row 4 : To Create Password and Confirm Password

        password= Label(frame1,text="Password",font=("Trebuchet",15,"bold"),bg = "white",fg = "#001A4D").place(x=50,y=310)
        self.txt_password =  Entry(frame1,font = ("Trebuchet",15),bg = "lightgray",show='*')      #====To Create Entry Field======
        self.txt_password.place(x=50,y=340,width=250)


        cpassword = Label(frame1,text="Confirm Password",font=("Trebuchet",15,"bold"),bg = "white",fg = "#001A4D").place(x=370,y=310)
        self.txt_cpassword =  Entry(frame1,font = ("Trebuchet",15),bg = "lightgray",show='*')
        self.txt_cpassword.place(x=370,y=340,width=250)


        #----------------Terms and condition Checkbox

        self.var_chk=IntVar()
        chk = Checkbutton(frame1,text="I Accept all the Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",fg="#26004D",font=("Trebuchet",11,"bold"),cursor="hand2")
        chk.place(x=50,y=380)
        
    
        #-------------For Register Button


        #----this is for create button using Text

        # btn = Button(frame1,text="Register Now",bg="orange",font=("Trebuchet",20)).place(x=50,y=420)

        #----this is for create button using Image

        self.btn_img=ImageTk.PhotoImage(file="C:\\Users\\Saumitra\\Python\\login with database\\images\\RButton1.png")
        btn_register = Button(frame1,image=self.btn_img,bd=1,cursor="hand2",command=self.register_data)
        btn_register.place(x=50,y=420,width=200)
        btn_login = Button(self.root,text="Sign In",fg="green",font=("Trebuchet",23,"bold"),command=self.login_window,bd=0,cursor="hand2")
        btn_login.place(x=185,y=540,width=200)


    def login_window(self):
        self.root.destroy()
        import LOGIN

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)        #-----------------To clear all the fields after Registered successfully
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_question.current(0)

    def register_data(self):
        if(self.txt_fname.get()=="" or  self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()==""): 
            messagebox.showerror("Errror","All Fields are Required",parent=self.root)

        elif self.txt_password.get() != self.txt_cpassword.get() :
            messagebox.showerror("Error","Password in both the Fields must be Same",parent=self.root)

        elif self.var_chk.get()==0 :
            messagebox.showerror("Error","Please Accept Terms and Conditions",parent=self.root)

        else :
            
            try :
                con = pymysql.connect(host="localhost",user="root",password="root",database="employee1")
                cur = con.cursor() 
                cur.execute("select * from employee_info where email = %s",self.txt_email.get())
                row = cur.fetchone()
                #print(row)
                #                 
                if row != None :
                    messagebox.showerror("Error"," User Already Exist. Please try with another Email  ",parent=self.root)
                else :
                    cur.execute("insert into employee_info (f_name,l_name,contact,email,question,answer,password)values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_question.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                                ))
                    messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                    self.clear()        #--------To clear all the fields after Registered successfully
                con.commit()
                con.close()
            except Exception as es :
                messagebox.showerror("Error",f"Error due to: {str(es) }",parent=self.root)





                


root=Tk()
obj = Registration(root)
root.mainloop()