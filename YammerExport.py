# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 08:13:32 2019

@author: Prathamesh
"""
import tkinter
import tkinter.messagebox
import datetime
import os
from tkinter.filedialog import askdirectory
import webbrowser
import threading

top = tkinter.Tk()
top.wm_title("Yammer Data Export")
os.chdir("C:/")
token=""

def firstSetupDownload():
    url="https://sourceforge.net/projects/gnuwin32/files/wget/1.11.4-1/wget-1.11.4-1-setup.exe/download"
    webbrowser.open_new(url)
             
def browse():
    path= askdirectory()
    seltext.set(path)
    os.chdir(path)
    
def limitSizeShort(var):
    value = var.get();
    if len(value) > 2: var.set(value[:2]);

def limitSizeLong(var):
    value = var.get();
    if len(value) > 4: var.set(value[:4]);
          
def onClick(event):
    event.widget.delete(0, "end")
    return None

def error():
    tkinter.messagebox.showwarning(
            "Export",
            "Please enter valid date/s  !")
    reset()
    return

def reset():
    mone.insert(0, "mm")
    daye.insert(0, "dd")
    yeare.insert(0, "yyyy")
    mon1e.insert(0, "mm")
    day1e.insert(0, "dd")
    year1e.insert(0, "yyyy")
    mon2e.insert(0, "mm")
    day2e.insert(0, "dd")
    year2e.insert(0, "yyyy")

def defaultDate():
    def callback1():
        reqDate= datetime.date.today()
        reqDate= reqDate.replace(day=1)
        reqDate= reqDate- datetime.timedelta(days=1)
        date= str(reqDate.year) + "-" + str(reqDate.month) + "-" + str(reqDate.day)
        date2= str(datetime.date.today().year) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().day)
        dates= date + "--" + date2
        print(dates)
        os.system("@ECHO OFF")
        os.system("SETLOCAL EnableDelayedExpansion")
        os.system('''IF NOT EXIST cacert.pem ("C:/Program Files (x86)/GnuWin32/bin/wget.exe" http://curl.haxx.se/ca/cacert.pem --no-check-certificate)''')
        os.system("ECHO Downloading..")
        os.system('''"C:/Program Files (x86)/GnuWin32/bin/wget.exe" -O "Export-''' + dates + '''.zip" -t 1 --header "Authorization: Bearer 47353-eybVTJAD8NarlNWtEi73A" --no-check-certificate "https://www.yammer.com/api/v1/export?since=''' + date + '''"''')
        os.system("ECHO Finish Download")
    thr1= threading.Thread(target= callback1)
    thr1.start()

def manualSinceDate():
    def callback2():
        try:
            datetime.datetime(year= int(myear.get()), month= int(mmon.get()), day= int(mday.get()))
        except ValueError:
            error()
            return
        if datetime.date(year= 2005, month= 1, day= 1) > datetime.date(year= int(myear.get()), month= int(mmon.get()), day= int(mday.get())):
            error()
            return
        if datetime.date(year= int(myear.get()), month= int(mmon.get()), day= int(mday.get())) > datetime.date.today():
            error()
            return
        date= str(myear.get()) + "-" + str(mmon.get()) + "-" + str(mday.get())
        date2= str(datetime.date.today().year) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().day)
        dates= date + "--" + date2
        os.system("@ECHO OFF")
        os.system("SETLOCAL EnableDelayedExpansion")
        os.system('''IF NOT EXIST cacert.pem ("C:/Program Files (x86)/GnuWin32/bin/wget.exe" http://curl.haxx.se/ca/cacert.pem --no-check-certificate)''')
        os.system("ECHO Downloading..")
        os.system('''"C:/Program Files (x86)/GnuWin32/bin/wget.exe" -O "Export-''' + dates +'''.zip" -t 1 --header "Authorization: Bearer 47353-eybVTJAD8NarlNWtEi73A" --no-check-certificate "https://www.yammer.com/api/v1/export?since=''' + date + '''"''')
        os.system("ECHO Finish Download")
    thr2= threading.Thread(target= callback2)
    thr2.start()

def manualDates():
    def callback3():
        date1= str(myear1.get()) + "-" + str(mmon1.get()) + "-" + str(mday1.get())
        date2= str(myear2.get()) + "-" + str(mmon2.get()) + "-" + str(mday2.get())
        try:
            datetime.datetime(year= int(myear1.get()), month= int(mmon1.get()), day= int(mday1.get()))
        except ValueError:
            error()
            return
        try:
            datetime.datetime(year= int(myear2.get()), month= int(mmon2.get()), day= int(mday2.get()))
        except ValueError:
            error()
            return
        if datetime.date(year= 2005, month= 1, day= 1) > datetime.date(year= int(myear1.get()), month= int(mmon1.get()), day= int(mday1.get())):
            error()
            return
        if datetime.date(year= int(myear2.get()), month= int(mmon2.get()), day= int(mday2.get())) > datetime.date.today():
            error()
            return
        if datetime.date(year= int(myear1.get()), month= int(mmon1.get()), day= int(mday1.get())) > datetime.date(year= int(myear2.get()), month= int(mmon2.get()), day= int(mday2.get())):
            error()
            return
        dates= date1 + "--" + date2
        os.system("@ECHO OFF")
        os.system("SETLOCAL EnableDelayedExpansion")
        os.system('''IF NOT EXIST cacert.pem ("C:/Program Files (x86)/GnuWin32/bin/wget.exe" http://curl.haxx.se/ca/cacert.pem --no-check-certificate)''')
        os.system("ECHO Downloading..")
        os.system('''"C:/Program Files (x86)/GnuWin32/bin/wget.exe" -O "Export-''' + dates +'''.zip" -t 1 --header "Authorization: Bearer 47353-eybVTJAD8NarlNWtEi73A" --no-check-certificate "https://www.yammer.com/api/v1/export?since=''' + date1 + '''&until=''' + date2 + '''"''')
        os.system("ECHO Finish Download")
    thr3= threading.Thread(target= callback3)
    thr3.start()

head= tkinter.Label(top, text="Yammer Data Export App", fg="red",   font=("Verdana 10 bold",25))
head.pack()
head.place(x= 75, y= 10)

s1= tkinter.Label(top, text="------------------------------------------------------------------------------------------------------------------------")
s1.pack()
s1.place(x= 0, y= 50)

s2= tkinter.Label(top, text="------------------------------------------------------------------------------------------------------------------------")
s2.pack()
s2.place(x= 0, y= 65)

firstl= tkinter.Label(top, text="First time Setup    --- >> ")
firstl.config(font=("Times New Roman", 13))
firstl.pack()
firstl.place(x= 70, y= 90)

firstb1= tkinter.Button(top, text=" Download ", command= firstSetupDownload)
firstb1.pack()
firstb1.place(x= 260, y= 88)

s3= tkinter.Label(top, text="------------------------------------------------------------------------------------------------------------------------")
s3.pack()
s3.place(x= 0, y= 120)

expl= tkinter.Label(top, text="Select a directory to save the data (default directory is C:\)")
expl.config(font=("Times New Roman", 13))
expl.pack()
expl.place(x= 50, y= 150)

bdir= tkinter.Button(top, text="Browse", command= browse)
bdir.pack()
bdir.place(x= 470, y= 149)

selected= tkinter.Label(top, text="Current directory: ")
selected.config(font=("Times New Roman", 12))
selected.pack()
selected.place(x= 100, y= 190)

seltext= tkinter.StringVar()
seltext.set("C:/")
dirtext= tkinter.Label(top, textvariable= seltext)
dirtext.config(font=("Times New Roman", 11))
dirtext.pack()
dirtext.place(x= 215, y= 193)

s4= tkinter.Label(top, text="------------------------------------------------------------------------------------------------------------------------")
s4.pack()
s4.place(x= 0, y= 220)
    
reqDate= datetime.date.today()
reqDate= reqDate.replace(day=1)
reqDate= reqDate- datetime.timedelta(days=1)
    
t1= tkinter.Label(top, text="1) Export the data since "+reqDate.strftime('%m/%d/%Y'))
t1.config(font=("Times New Roman", 12))
t1.pack()
t1.place(x= 185, y= 250)

b1 = tkinter.Button(top, text = "Option 1", command = defaultDate)
b1.pack(pady=20, padx = 20)
b1.place(x=275, y=290)

s5= tkinter.Label(top, text="------------------------------------------------------------------------------------------------------------------------")
s5.pack()
s5.place(x= 0, y= 320)
    
t21= tkinter.Label(top, text="2) Export the data since ")
t21.config(font=("Times New Roman", 12))
t21.pack()
t21.place(x= 135, y= 350)

mmon= tkinter.StringVar()
mmon.trace("w",lambda name, index, mode, mmon= mmon: limitSizeShort(mmon))
mone= tkinter.Entry(top, width= 4, textvariable= mmon)
mone.bind("<Button-1>", onClick)
mone.pack()
mone.insert(0, "mm")
mone.place(x= 300, y= 355)

t22= tkinter.Label(top, text=" / ")
t22.config(font=("Times New Roman", 18))
t22.pack()
t22.place(x= 330, y= 350)

mday= tkinter.StringVar()
mday.trace("w", lambda name, index, mode, mday= mday: limitSizeShort(mday))
daye= tkinter.Entry(top, width= 4, textvariable= mday)
daye.bind("<Button-1>", onClick)
daye.pack()
daye.insert(0, "dd")
daye.place(x= 355, y= 355)

t23= tkinter.Label(top, text=" / ")
t23.config(font=("Times New Roman", 18))
t23.pack()
t23.place(x= 385, y= 350)

myear= tkinter.StringVar()
myear.trace("w", lambda name, index, mode, myear= myear: limitSizeLong(myear))
yeare= tkinter.Entry(top, width= 6, textvariable= myear)
yeare.bind("<Button-1>", onClick)
yeare.pack()
yeare.insert(0, "yyyy")
yeare.place(x= 410, y= 355)

b2 = tkinter.Button(top, text = "Option 2", command= manualSinceDate)
b2.pack(pady=20, padx = 20)
b2.place(x=275, y=400)

s6= tkinter.Label(top, text="------------------------------------------------------------------------------------------------------------------------")
s6.pack()
s6.place(x= 0, y= 430)

t31= tkinter.Label(top, text="3) Export the data from ")
t31.config(font=("Times New Roman", 12))
t31.pack()
t31.place(x= 10, y= 460)

mmon1= tkinter.StringVar()
mmon1.trace("w", lambda name, index, mode, mmon1= mmon1: limitSizeShort(mmon1))
mon1e= tkinter.Entry(top, width= 4, textvariable= mmon1)
mon1e.bind("<Button-1>", onClick)
mon1e.pack()
mon1e.insert(0, "mm")
mon1e.place(x= 165, y= 465)

t32= tkinter.Label(top, text=" / ")
t32.config(font=("Times New Roman", 18))
t32.pack()
t32.place(x= 195, y= 460)

mday1= tkinter.StringVar()
mday1.trace("w", lambda name, index, mode, mday1= mday1: limitSizeShort(mday1))
day1e= tkinter.Entry(top, width= 4, textvariable= mday1)
day1e.bind("<Button-1>", onClick)
day1e.pack()
day1e.insert(0, "dd")
day1e.place(x= 220, y= 465)

t33= tkinter.Label(top, text=" / ")
t33.config(font=("Times New Roman", 18))
t33.pack()
t33.place(x= 250, y= 460)

myear1= tkinter.StringVar()
myear1.trace("w", lambda name, index, mode, myear1= myear1: limitSizeLong(myear1))
year1e= tkinter.Entry(top, width= 6, textvariable= myear1)
year1e.bind("<Button-1>", onClick)
year1e.pack()
year1e.insert(0, "yyyy")
year1e.place(x= 275, y= 465)

t34= tkinter.Label(top, text=" until ")
t34.config(font=("Times New Roman", 12))
t34.pack()
t34.place(x= 335, y= 460)

mmon2= tkinter.StringVar()
mmon2.trace("w", lambda name, index, mode, mmon2= mmon2: limitSizeShort(mmon2))
mon2e= tkinter.Entry(top, width= 4, textvariable= mmon2)
mon2e.bind("<Button-1>", onClick)
mon2e.pack()
mon2e.insert(0, "mm")
mon2e.place(x= 395, y= 465)

t35= tkinter.Label(top, text=" / ")
t35.config(font=("Times New Roman", 18))
t35.pack()
t35.place(x= 425, y= 460)

mday2= tkinter.StringVar()
mday2.trace("w", lambda name, index, mode, mday2= mday2: limitSizeShort(mday2))
day2e= tkinter.Entry(top, width= 4, textvariable= mday2)
day2e.bind("<Button-1>", onClick)
day2e.pack()
day2e.insert(0, "dd")
day2e.place(x= 450, y= 465)

t36= tkinter.Label(top, text=" / ")
t36.config(font=("Times New Roman", 18))
t36.pack()
t36.place(x= 480, y= 460)

myear2= tkinter.StringVar()
myear2.trace("w", lambda name, index, mode, myear2= myear2: limitSizeLong(myear2))
year2e= tkinter.Entry(top, width= 6, textvariable= myear2)
year2e.bind("<Button-1>", onClick)
year2e.pack()
year2e.insert(0, "yyyy")
year2e.place(x= 505, y= 465)

b3 = tkinter.Button(top, text = "Option 3", command= manualDates)
b3.pack(pady=20, padx = 20)
b3.place(x=275, y=510)

s7= tkinter.Label(top, text="------------------------------------------------------------------------------------------------------------------------")
s7.pack()
s7.place(x= 0, y= 545)

s8= tkinter.Label(top, text="------------------------------------------------------------------------------------------------------------------------")
s8.pack()
s8.place(x= 0, y= 560)

top.geometry('{}x{}'.format(600, 600))
top.resizable(width=False, height=False)
top.mainloop()