import numpy as np
import matplotlib.pyplot as plt
import Point as P
import csv
import Robot as rob
import Arena as are
import Air as ai
import os.path
import random
import Simulator as Sim

from Tkinter import *


def Inter_Face_To_Function(Func_Name,Id):
    
    T.delete("1.0",INSERT)

    if Func_Name=="Battery":
        T.insert(INSERT,"Battery: " + str(callback.robots[Id].battery))
    elif Func_Name=="Place":
        T.insert(INSERT,"Place: " + str(callback.arena.Get_Robot_Place(Id)))
    elif Func_Name=="Neightbors":
        T.insert(INSERT,"Neightbors: " + callback.arena.Get_Neightbors(Id))
    elif Func_Name=="All_Points":
        T.insert(INSERT,"All_Points: " + callback.arena.Get_All_Points(Id))
    

callback = Sim.Simulator("Robot.csv")


root = Tk()
root.title('GUI')





ider = StringVar()
Mov=StringVar()
Result = StringVar()




frame = Frame(root, width=800, height=1000, bd=1)
frame.pack()
iframe2 = Frame(frame, bd=10, relief=RIDGE)
Label(iframe2, fg="red",width=25,text='Robot Id To Command:').pack(side=LEFT, padx=0)
Entry(iframe2,width=10,textvariable=ider, fg="brown", bg='white').pack(side=LEFT, padx=0)
Button(iframe2,text="Move",background="red",relief=SOLID,command = lambda:callback.arena.Move_Robot(ider.get(),Mov.get())).pack(side=LEFT,padx=0)
Entry(iframe2,width=10,textvariable=Mov, fg="brown", bg='white').pack(side=LEFT, padx=0)
Button(iframe2,text="Battery",background="TEAL",relief=SOLID,command = lambda:Inter_Face_To_Function("Battery",ider.get())).pack(side=LEFT,padx=0)
Button(iframe2,text="All_Message",background="Green",relief=SOLID,command =lambda:Set_To_Text()).pack(side=LEFT,padx=0)
Button(iframe2,text="Recharge Battery",background="YELLOW",relief=SOLID,command = lambda:callback.robots[ider.get()].Recharge()).pack(side=LEFT,padx=0)




ider.set('')
Mov.set('')



iframe2.pack(expand=3, fill=X, pady=0, padx=30)

frame = Frame(root, width=800, height=1000, bd=1)
frame.pack()
iframe2 = Frame(frame, bd=10, relief=RIDGE)
Button(iframe2,text="All Points That He Was There",background="Orange",relief=SOLID,command = lambda:Inter_Face_To_Function("All_Points",ider.get())).pack(side=LEFT,padx=0)
Button(iframe2,text="Place",background="Orange",relief=SOLID,command = lambda:Inter_Face_To_Function("Place",ider.get())).pack(side=LEFT,padx=0)
Button(iframe2,text="Neightbors",background="BROWN",relief=SOLID,command = lambda:Inter_Face_To_Function("Neightbors",ider.get())).pack(side=LEFT,padx=0)



iframe2.pack(expand=3, fill=X, pady=0, padx=0)



frame = Frame(root, width=500, height=400, bd=1)
frame.pack()

iframe2 = Frame(frame, bd=2, relief=RIDGE)


Label(iframe2, text='Sender Message Source Id').pack(side=LEFT,padx=0)
Entry(iframe2, textvariable='', bg='white',width=5).pack(side=LEFT,padx=0)





Label(iframe2, fg="black",text='Getter Message Destenation Id').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable='', fg="black", bg='white',width=5).pack(side=LEFT,padx=0)
Button(iframe2,text="Get_Distance",background="BROWN",relief=SOLID,command = lambda:Nmea_To_Csv.create_csv(t.get())).pack(side=LEFT,padx=0)








iframe2.pack(expand=1, fill=X, pady=0, padx=0)

frame = Frame(root, width=250, height=400, bd=1)
frame.pack()

iframe2 = Frame(frame, bd=2, relief=RIDGE)

Label(iframe2, text='Distance From Source Id').pack(side=LEFT,padx=0)
Entry(iframe2, textvariable='', bg='white',width=5).pack(side=LEFT,padx=0)






Label(iframe2, fg="black",text='To Destenation Id:').pack(side=LEFT,padx=0)
Entry(iframe2,textvariable='', fg="black", bg='white',width=5).pack(side=LEFT,padx=0)
Button(iframe2,text="Send Message",background="ORange",relief=SOLID,command = lambda:Nmea_To_Csv.create_csv(t.get())).pack(side=LEFT,padx=0)

iframe2.pack(expand=1, fill=X, pady=0, padx=0)

frame = Frame(root, width=250, height=400, bd=1)
frame.pack()

iframe2 = Frame(frame, bd=5, relief=RIDGE)

Label(iframe2, text='Result Of Active Robot').pack(side=LEFT,padx=0)
T = Text(iframe2, height=5, width=100)
T.pack()

#T.insert(INSERT, "Hello.....")
T.delete("1.0",INSERT)


iframe2.pack(expand=1, fill=X, pady=10, padx=5)
mainloop()