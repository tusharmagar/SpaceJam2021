# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import * 
##from tkinter.ttk import *
import serial
numofstud=3 #Students here are 3 ie, Yash, Tushar and Vibhav
listofSRN=['PES1UG20EC231','PES1UG20EC214','PES1UG20EC221']#Creates an Empty List
ser=serial.Serial("COM3",baudrate=9600)#Establish the Serial Comm+Python Network
P="Access Granted"
def getData():#Function to get the data from the Arduino Serial port
    arduinoData=ser.readline().decode("ascii")
    return arduinoData
def scanProcess():
    scannedData=getData()#Data that gets scanned by the RFID i.e the SRN, now we need to check if this SRN is present within the list of SRNS ie listofSRN
    for i in listofSRN :#Number of Students
        if i in scannedData:
            if(i=="PES1UG20EC231"):
                txt_name.insert(END,"Yash")
                txt_number.insert(END,"282382093")
                txt_sem.insert(END,"1")
                txt_sec.insert(END,"R2")
                txt_email.insert(END,"shdahdq@gmail.com")
            elif(i=="PES1UG20EC214"):
                txt_name.insert(END,"Tushar")
                txt_number.insert(END,"294124812")
                txt_sem.insert(END,"1")
                txt_sec.insert(END,"R2")
                txt_email.insert(END,"ajenfewuf@gmail.com")
            else:
                txt_name.insert(END,"Vibhav")
                txt_number.insert(END,"148238712")
                txt_sem.insert(END,"1")
                txt_sec.insert(END,"R2")
                txt_email.insert(END,"bsdhf@gmail.com")
            return P
        else:
            continue
master = Tk()   
master.title("WELCOME TO PES UNIVERSITY")
master.geometry("600x400")
master.configure(bg="thistle1")
def textscan():
    t.insert(END,scanProcess())
def clrscr():
    t.delete(1.0,END)
    txt_name.delete(1.0,END)
    txt_number.delete(1.0,END)
    txt_sem.delete(1.0,END)
    txt_sec.delete(1.0,END)
    txt_email.delete(1.0,END)
    
#GUI   
t=Text(master,height=5,width=25)
btn_clr=Button(master,text="Click to clear",font=("Arial"),bg="thistle2",command=clrscr)
t.grid(row=0,column=1)
btn_clr.grid(row=2,column=1)
btn_scan=Button(master,text="Click here for Scanning!",font=("Arial"),bg="thistle2",command=textscan)
btn_scan.grid(row=1,column=1)     
labelname=Label(master,text="NAME:",padx=1,pady=1,bg="thistle1",font=("Arial"))
labelnumber=Label(master,text="NUMBER:",padx=1,pady=1,bg="thistle1",font=("Arial"))
labelsem=Label(master,text="SEMESTER:",padx=1,pady=1,bg="thistle1",font=("Arial"))
labelsec=Label(master,text="SECTION:",padx=1,pady=1,bg="thistle1",font=("Arial"))
labelemail=Label(master,text="EMAIL:",padx=1,pady=1,bg="thistle1",font=("Arial"))
labelname.grid(row=0,column=5)
labelnumber.grid(row=1,column=5)
labelsem.grid(row=2,column=5)
labelsec.grid(row=3,column=5)
labelemail.grid(row=4,column=5)
txt_name=Text(master,height=2,width=16,padx=1,pady=1,font=("Arial"),bg="light blue",fg="black")
txt_number=Text(master,height=2,width=16,padx=1,pady=1,font=("Arial"),bg="light blue",fg="black")
txt_sem=Text(master,height=2,width=16,padx=1,pady=1,font=("Arial"),bg="light blue",fg="black")
txt_sec=Text(master,height=2,width=16,padx=1,pady=1,font=("Arial"),bg="light blue",fg="black")
txt_email=Text(master,height=2,width=16,padx=1,pady=1,font=("Arial"),bg="light blue",fg="black")
txt_name.grid(row=0,column=6)
txt_number.grid(row=1,column=6)
txt_sem.grid(row=2,column=6)
txt_sec.grid(row=3,column=6)
txt_email.grid(row=4,column=6)
mainloop() 
