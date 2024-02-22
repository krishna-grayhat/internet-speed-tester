from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download()/(10**6),3))+" Mbps"
    upload = str(round(sp.upload()/(10**6),3))+" Mbps"
    lb_down.config(text=download)
    lb_up.config(text=upload)




sp = Tk()

sp.title(" Internet Speed Check ")
sp.geometry("500x530")
sp.config(bg="blue")

lb = Label(sp,text="Internet Speed check",font=("Time New Roman",30,"bold"),fg="orange")
lb.place(x=42,y=40,width=420,height=50)

lb = Label(sp,text="Downloading Speed",font=("Time New Roman",30,"bold"),fg="black")
lb.place(x=42,y=130,width=420,height=50)

lb_down = Label(sp,text="00",font=("Time New Roman",30,"bold"),fg="black")
lb_down.place(x=42,y=200,width=420,height=50)

lb = Label(sp,text="Uploading Speed",font=("Time New Roman",30,"bold"),fg="black")
lb.place(x=42,y=290,width=420,height=50)

lb_up = Label(sp,text="00",font=("Time New Roman",30,"bold"),fg="black")
lb_up.place(x=42,y=360,width=420,height=50)

bt = Button(sp,text="CHECK",relief=RAISED,bg="red",fg="black",font=("Time New Roman",25,"bold"),command=speedcheck)
bt.place(x=42,y=440,width=420,height=50)



sp.mainloop()