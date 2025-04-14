import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("tk")
window.geometry("450x110")


entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=25)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=25)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=25)
entry4 = tk.Entry(window,text="Entry widgets can be typed in", width=25)

Label1 = tk.Label(window,text="Principal", width=10)
Label2 = tk.Label(window,text="Interest Rate", width=10)
Label3 = tk.Label(window,text="Years", width=8)
Label4 = tk.Label(window,text="Amount", width=10)
combo3=ttk.Combobox(window, values=[str(i)for i in range(1,101)]).place(x=300,y=30)


Label1.place(x=0,y=10)
Label2.place(x=150,y=10)
Label3.place(x=300,y=10)
Label4.place(x=80,y=80)

entry1.place(x=0,y=30)
entry2.place(x=150,y=30)

entry4.place(x=120,y=80)

window.mainloop()