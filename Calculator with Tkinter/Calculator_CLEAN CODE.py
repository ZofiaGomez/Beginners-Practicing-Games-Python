# First we import the tkinter library

from tkinter import *


# Then we create the window and give it a name, an identity and an entry

root=Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# We start defining the buttons and their functionalities

# We need a button to get a number inside the entry and we make sure
# that the entry is clear with the 'delete' method

# The 'current' variable will give us the chance to pass numbers with
# more than one figure

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


# We define a clear button to erase everything that is inside the entry

def button_clear():
    e.delete(0, END)


# Then we create the operation buttons by creating global variables
# that is a variable inside a function that is able to be use outside

# We set two different global variables for every button that will be 
# useful later in the 'equal' button 

# The variable 'f_num' will turn the string inside 'first_number' 
# and will turn it into an integer

# The variable 'first_number' will contain the number the user enters

# The method 'delete' will erase the number inside the entry (this method
# does not erase the value held by the variable 'first_number', it only
# clears the entry view)

def button_add():
    first_number = e.get() #You shall declare the () 
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_substract():
    first_number = e.get() 
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get() 
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get() 
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

# The last button we create will be 'equal' which will take every
# variable we previously set and do the operations

# We use the 'if', 'elif', and 'else' statements to get it
# We declare another variable that will hold the second number
# and with the 'delete' method we clear that number to pass the result

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition": # == conditional
        e.insert(0, f_num + int(second_number))
    elif math == "substraction":
        e.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        e.insert(0, f_num * int(second_number))
    elif math == "division":
        e.insert(0, f_num / int(second_number))
    return

# We use 'elif' instead of 'if' because if we state an 'if' and we
# click on every operation button, then the computer will go through
# every line and, if they are correct, it will print everything (or
# most likely return an error) so, if we state an 'elif' it will
# choose from the most recent button and do its job


# Now we will declare the buttons identities and functionalities

button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_click(2)) 
button_3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_click(4)) 
button_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_click(7)) 
button_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_click(0))

button__add= Button(root, text="+", padx=39, pady=20, command=button_add)
button__equal= Button(root, text="=", padx=87, pady=20, command=button_equal)
button__clear= Button(root, text="Clear", padx=77, pady=20, command=button_clear)

button__substract= Button(root, text="-", padx=41, pady=20, command=button_substract)
button__multiply= Button(root, text="*", padx=40, pady=20, command=button_multiply)
button__divide= Button(root, text="/", padx=41, pady=20, command=button_divide)


# Finally we give the buttons a place

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button__add.grid(row=5, column=0)
button__clear.grid(row=4, column=1, columnspan=2)
button__equal.grid(row=5, column=1, columnspan=2)

button__substract.grid(row=6, column=0)
button__multiply.grid(row=6, column=1)
button__divide.grid(row=6, column=2)

# Don't forget to close the mainloop
root.mainloop()