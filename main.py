import tkinter as tk 
from PIL import Image,ImageTk
import pyspeedtest 
import math
from tkinter import messagebox


root=tk.Tk()                # creates a window
root.geometry("300x450")    # defining size of the Window
root.resizable(0,0)         # fixing the size of the Window

root.title("Internet Speed Downloader")

# creating function
st=pyspeedtest.SpeedTest("www.google.com")
def SpeedTest():
    speed=str(math.floor(st.download()/1000)) + "kb/s"
    messagebox.showinfo("The Speed is ", speed)

#logo
logo=Image.open("logo.png")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.pack()

new_label=tk.Label(root, text="Test Download Speed",font=("Areal",18,"bold"), fg="green" )
new_label.pack(padx=20,pady=20)

# creating buttons

button1=tk.Button(root, text="Check",command=SpeedTest,font=("Areal",16,"bold"))
button1.pack(padx=20,pady=10)

button2=tk.Button(root, text="Exit",command=root.destroy,font=("Areal",16,"bold"))
button2.pack(padx=10,pady=10)
  
new_label2=tk.Label(root, text="Thanks !!", font=("Areal",22,"bold"),bg="black",fg="white" )
new_label2.pack(padx=10,pady=10, fill="both", expand=True)

root.mainloop()