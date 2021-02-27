# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import * 
from tkinter.ttk import *
import serial

numofstud=3 #Students here are 3 ie, Yash, Tushar and Vibhav
listofSRN=['PES1UG20EC231','PES1UG20EC214','PES1UG20EC221'] #Creates an Empty List
ser=serial.Serial("COM3",baudrate=9600) #Establish the Serial Comm+Python Network
P="PRESENT"
A="ABSENT"
def getData():#Function to get the data from the Arduino Serial port
    arduinoData=ser.readline().decode("ascii")
    return arduinoData
def scanProcess():
    scannedData=getData()#Data that gets scanned by the RFID i.e the SRN, now we need to check if this SRN is present within the list of SRNS ie listofSRN
    for i in listofSRN :#Number of Students
        if i in scannedData:
            #print(P)
            return P
        else:
            continue
def close():
    newWindow.destroy()
master = Tk()   
master.geometry("500x400") 
master.title("PES University")

def textscan():
    t.insert(END,scanProcess())
    
t=Text(master,height=5,width=20)
btn_clr=Button(master,text="Click to clear",command=lambda: t.delete(1.0,END))
t.pack()
btn_clr.pack()
btn_scan=Button(master,text="Click here for Scanning!",command=textscan)
btn_scan.pack()    
label1=Label(master,text="Welcome to PES University")
label1.pack()
#b1=Button(master,text="Click Here to Initiate the Scanning Procedure!",command=openNew)
#b1.grid(row=3,column=2)

mainloop() 
