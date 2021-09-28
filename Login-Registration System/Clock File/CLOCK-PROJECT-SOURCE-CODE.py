from tkinter import*
from PIL import Image,ImageTk,ImageDraw
from datetime import*
import time
from math import *
class Clock:
    def __init__(self,root):    # This Constructor is used for working on our window
        self.root=root
        self.root.title("GUI Analog Clock")  #---------Set the Title of Window.
        self.root.geometry("1350x700+0+0")   #---------Set the dimensions(size) of Window
        self.root.config(bg="#00001A")        #---------Set the Background colour of Window

        title = Label(self.root,text="** Analog Clock **",font=("times new roman",50,"bold"),fg="white",bg="#04444a").place(x=0,y=50,relwidth=1)   #----------To give the heading label to the page.
        self.lbl=Label(self.root,bg="#00001A",bd=20,relief=RAISED)
        self.lbl.place(x=540,y=150,height=400,width=400)
        self.working()

    def clock_image(self,hr,mint,sec):
        clock = Image.new("RGB",(400,400),(255,255,255))
        draw = ImageDraw.Draw(clock)

        #========For Create Clock Image 
        bg = Image.open("C://Users//Saumitra//Python//login with database//Clock project//clock2.jpeg")
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
        draw.line((origin,200+60*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=6)

        #========For Minute Hand Image
        draw.line((origin,200+90*sin(radians(mint)),200-80*cos(radians(mint))),fill="blue",width=5)

        #========For Seconds Hand Image
        draw.line((origin,200+110*sin(radians(sec)),200-100*cos(radians(sec))),fill="green",width=4)
        draw.ellipse((194,194,206,206),fill="black")
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
        self.lbl.after(10,self.working)

    
root=Tk()
obj=Clock(root)   
root.mainloop()