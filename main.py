import tkinter as tk 
from PIL import Image,ImageTk
import pyspeedtest 
import math
from tkinter import messagebox



root=tk.Tk()
root.geometry("300x450")
root.resizable(0,0)
root.title("Internet Speed Downloader")
# creating function

st=pyspeedtest.SpeedTest("www.google.com")
def SpeedTest():
    speed=str(math.floor(st.download()/1000)) + "kb/s"
    messagebox.showinfo("The Sspeed is ", speed)

#logo

logo=Image.open("robot.png")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.pack()

new_label=tk.Label(root, text="Test download speed",font=("Areal",18,"bold"), fg="green" )
new_label.pack(padx=20,pady=20)

# creating buttons

button1=tk.Button(root, text="check",command=SpeedTest,font=("Areal",16,"bold"))
button1.pack(padx=20,pady=10)

button1=tk.Button(root, text="exit",command=root.destroy,font=("Areal",16,"bold"))
button1.pack(padx=10,pady=10)
  
new_label2=tk.Label(root, text="Thanks !!", font=("Areal",16,"bold"),bg="black",fg="white" )
new_label2.pack(padx=10,pady=10, fill="both", expand=True)



root.mainloop()