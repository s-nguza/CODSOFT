
from tkinter import Tk, Entry, Button
import logic_Cal as calc

root = Tk()
root.title("CALCULATOR")

space = Entry(root, width=35, borderwidth=5)
space.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = space.get()
    space.delete(0, "end")
    space.insert(0, str(current) + str(number))

def button_adding(sign):
    """This function is when a user uses a addition sign"""
    first_number = space.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    space.delete(0, "end")

def button_minus(sign):
    """This function is when a user uses a substractions sign"""
    first_number = space.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    space.delete(0, "end")

def button_times(sign):
    """This function is when a user uses a multiplication sign"""
    first_number = space.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    space.delete(0, "end")

def button_division(sign):
    """This function is when a user uses a divison sign"""
    first_number = space.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    space.delete(0, "end")

def equal_too():
    """This function is when a user uses a equal to sign"""
    second_number = space.get()
    space.delete(0, "end")

    if math == "addition":
        space.insert(0, f_num + int(second_number))
    if math == "subtraction":
        space.insert(0, f_num - int(second_number))
    if math == "multiplication":
        space.insert(0, f_num * int(second_number))
    if math == "division":
        space.insert(0, f_num // int(second_number))

def button_clear():
    space.delete(0, "end")

button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_plus = Button(root, text='+', padx=41, pady=20, command=lambda: button_adding("+"))
button_difference = Button(root, text='-', padx=41, pady=20, command=lambda: button_minus("-"))
button_equal = Button(root, text='=', padx=41, pady=60, command=lambda: equal_too())
button_time = Button(root, text='*', padx=41, pady=20, command=lambda: button_times("*"))
button_divisions = Button(root, text='/', padx=41, pady=20, command=lambda: button_division("/"))
button_clears = Button(root, text="C", padx=90, pady=30, command=lambda: button_clear())

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0)
button_plus.grid(row=4, column=2)
button_difference.grid(row=4, column=1)
button_equal.grid(row=5, column=2, rowspan=2)
button_divisions.grid(row=5, column=1)
button_time.grid(row=5, column=0)
button_clears.grid(row=6, column=0, columnspan=2)

root.mainloop()
