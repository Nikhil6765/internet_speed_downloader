import tkinter as tk 
from PIL import Image,ImageTk


root=tk.Tk()
root.geometry("300x450")
root.resizable(0,0)
root.title("Internet Speed Downloader")

#logo

logo=Image.open("robot.png")
logo=ImageTk.PhotoImage(logo)
logo_label=tk.Label(image=logo)
logo_label.image=logo
logo_label.pack()

new_label=tk.Label(root, text="Test download speed",font=("Areal",18,"bold"), fg="green" )
new_label.pack(padx=20,pady=20)

# creating buttons

button1=tk.Button(root, text="check",font=("Areal",18,"bold"))
button1.pack(padx=20,pady=10)

button1=tk.Button(root, text="exit",font=("Areal",18,"bold"))
button1.pack(padx=10,pady=10)
  
new_label2=tk.Label(root, text="Thanks !!", font=("Areal",18,"bold"),bg="black",fg="white" )
new_label2.pack(padx=10,pady=10, fill="both", expand=True)



root.mainloop()