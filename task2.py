import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
window.title("POKEMON ADVENTURE")
window.geometry("700x600")
window.configure(bg="white")
photo1 = PhotoImage(file="main.png")
label1 = tk.Label(window, image=photo1)
label1.place(x=0,y=50)


photo2 = PhotoImage(file="minimap.png")
label2 = tk.Label(window, image=photo2)
label2.place(x=520,y=100)
label2 = tk.Label(window,text="MINI MAP",bg="white")
label2.place(x=520,y=70)

buttons=["MAP","INVENTORY","POKEDEX","ROSTER","JOURNAL","HELP","SHOP"]
for i,name in enumerate(buttons):
    label3=tk.Button(window, text=name, width=13,height=2,borderwidth=2)
    label3.place(x=520,y=195+i*40)

photo4 = PhotoImage(file="logo.png")
label4 = tk.Label(window, image=photo4,anchor="center")
label4.place(x=260,y=520)

label5=tk.Frame(window)
label5.place(x=0,y=500)
buttons1=[
    ["NW","N","NE"],
    ["W"," ","E"],
    ["SW","S","SE"]
]
for r,row in enumerate(buttons1):
    for c,label in enumerate(row):
        if label:
            tk.Button(label5, text=label,width=4).grid(row=r,column=c,padx=2,pady=2)

window.mainloop()