from tkinter import *
from tkinter import messagebox

def get_y():
    y = float(ENTRY1.get())
    return y

def get_bending_moment():
    m = float(ENTRY2.get())
    return m

def get_depth():
    d = float(ENTRY3.get())
    return d

def get_breath():
    b = float(ENTRY4.get())
    return b


def inertia(a=" "):
    d = get_depth()
    b = get_breath()
    i = (b * pow(d, 3)) / 12
    return i


def bending_stress():
    try:
        y = get_y()
        m = get_bending_moment()
        i = inertia()

        stress = (m * y / i)
    except ValueError:
        messagebox.showinfo("Result", "please enter valid data")
    else:
        messagebox.showinfo("Result", stress)


if __name__ == '__main__':
    TOP = Tk()
    TOP.bind("<Return>", bending_stress)
    TOP.geometry("520x400")
    TOP.configure(background="#00ffff")
    TOP.title("Bending stress Calculator for Rectangle")
    TOP.resizable(width=True, height=True)
    LABLE = Label(TOP, bg="#00ff00", text="Welcome to Bending stress Calculator", font=("Courier", 15, "bold"),
                  pady=10)
    LABLE.place(x=60, y=0)
    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter y:", bd=6,
                   font=("Courier", 10, "bold"), pady=5)
    LABLE1.place(x=60, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter bending moment:", bd=6,
                   font=("Courier", 10, "bold"), pady=5)
    LABLE2.place(x=60, y=120)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=240, y=120)
    LABLE3 = Label(TOP, bg="#cef0f1", text="Enter depth:", bd=6,
                   font=("Courier", 10, "bold"), pady=5)
    LABLE3.place(x=60, y=180)
    ENTRY3 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY3.place(x=240, y=180)
    LABLE4 = Label(TOP, bg="#cef0f1", text="Enter breath:", bd=6,
                   font=("Courier", 10, "bold"), pady=5)
    LABLE4.place(x=60, y=240)
    ENTRY4 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY4.place(x=240, y=240)
    BUTTON = Button(bg="#2187e7", bd=12, text="Bending stress", padx=33, pady=15,
                    command=bending_stress,
                    font=("Courier", 20, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=115, y=300)
    TOP.mainloop()
