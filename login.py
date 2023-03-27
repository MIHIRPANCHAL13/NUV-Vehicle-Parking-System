from subprocess import call
from tkinter import *
from tkinter import messagebox
from front import Smart_Parking_System
from tkinter.messagebox import askyesno
from PIL import ImageTk
import cv2
import pickle
import cvzone
import numpy as np

from tkinter import *
from tkinter import messagebox

import PIL.Image


import mysql.connector


def Ok():
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="login")
    mycursor = mysqldb.cursor()
    uname =e1.get()
    password =e2.get()


    sql="select * from login where username=%s and password=%s"

    mycursor.execute(sql,[(uname),(password)])
    results=mycursor.fetchall()
    if results:
        messagebox.showinfo("","login success:")
        root.destroy()
        #call(["python","front.py"])
        #exec(open('front.py').read())
        rootx = Tk()
        sps = Smart_Parking_System(rootx)
        rootx.mainloop()
        return True
    else:
        messagebox.showinfo("","incorrect uname and password")
        return False
root=Tk()
root.title("login")
root.geometry("300x200")
global e1
global e2

Label(root,text="username").place(x=10,y=10)
Label(root,text="password").place(x=10,y=40)

e1 = Entry(root)
e1.place(x=140,y=10)
e2=Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")
Button(root,text="login",command=Ok,height=3,width=13).place(x=10,y=100)
root.mainloop()
