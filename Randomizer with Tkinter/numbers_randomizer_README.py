# First we will import the Tkinter library and the Random module

from tkinter import *
import random as r


# Then we will create the Tkinter window stablishing a root that will 
# return a new Toplevel widget on the screen. A new Tcl interpreter 
# will be created. And 'root' will be used for the identification 
# of the profile file

root=Tk()
root.title("Numbers Randomizer") # We give it a title name
root.geometry('400x300') # We set the dimensions
root.config(bg='#856ff8') # We set the backround color


# Then we will create a function that will give us the possibility of
# restart the game and will return a new random number

# We create a variable and call the random module with its alias 'r'
# 'randint' will give us a random number between 1 and 12 inclusive

# Note: 'randrange' will give us a number between 1 and 12 
# without counting the last number (12)

# Then we change the text in the variable 'mylabel' 
# to a different number 'rand'

def randomize():
    rand = r.randint(1,12) 
    mylabel.config(text=rand)


# Now we create wwhat will be inside of our window: a random number, 
# a label with a text, a backround color, and a place in the grid

rand = r.randint(1,12)
mylabel = Label(root, text=rand, bg='#856ff8', font=('Helvetica 75 bold'), justify='center')
mylabel.grid(row=1, column=1, pady=25, padx=150)


# Finally we create to buttons: one that regenerates the random number
# and one that closes the window

regenerate_button = Button(root, text="Regenerate", command=randomize).grid(column=1, row=3, padx=150)
quit_button = Button(root, text="Quit", command=root.destroy).grid(column=1, row=4, padx=150, pady=5)

# Note: if we use the variable 'grid' in the same line as the object
# we are positioning it will be not able to be changed inside a function
# so, with 'mylabel' we rather do it in separated lines, and we save
# some code spaces only with the button


# Don't forget to close the mainloop

root.mainloop()