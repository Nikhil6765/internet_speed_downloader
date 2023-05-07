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
new_label.pack()


root.mainloop()