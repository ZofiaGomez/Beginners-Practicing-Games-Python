# First we will import the Tkinter library and the Random module

from tkinter import *
import random as r


# Then we will create the Tkinter window stablishing a root that will 
# return a new Toplevel widget on the screen. A new Tcl interpreter 
# will be created. And 'root' will be used for the identification 
# of the profile file

root=Tk()
root.title("Letters Randomizer") # We give it a title name
root.geometry('400x300') # We set the dimensions
root.config(bg='#856ff8') # We set the backround color


# Then we will create a function that will give us the possibility of
# restart the game and will return a new random letter

# We create a variable and call the random module with its alias 'r'
# and 'choice' will give us a random letter between A and Z inclusive

# Then we change the text in the variable 'mylabel' 
# to a different letter 'letter_rand'

def randomize_method1():
    letter_rand = r.choice(rand1.split(','))
    mylabel.config(text=letter_rand)

# We'll talk about this later:

def randomize_method2():
    rand2 = chr(r.randint(ord('A'), ord('Z')))
    mylabel.config(text=rand2)

# Now we create what will be inside of our window: a random letter, 
# a label with a text, a backround color, and a place in the grid

# I tried to write a code with my existing knowledge before doing
# a little research, so I ended up with two methods (and two functions)


# Method Nº 1: the long one

# I wrote by hand every letter of the English Alphabet and used the
# 'split' method to make every single one of them an item on a list
# Then the variable 'choice' from the random method returns one of them

rand1 = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
letter_rand = r.choice(rand1.split(','))


# Method Nº 2: the better and more accurate one

# I set a variable that returns a random integer element from a list
# contained by the 'chr' function, which turns it into a string

rand2 = chr(r.randint(ord('A'), ord('Z')))


# We continue adding wwhat will be inside of our window: the label

mylabel = Label(root, text=letter_rand, bg='#856ff8', font=('Helvetica 75 bold'), justify='center')
mylabel.grid(row=1, column=1, pady=25, padx=150)


# Finally we create to buttons: one that regenerates the random number
# and one that closes the window

regenerate_button = Button(root, text="Regenerate", command=randomize_method1).grid(column=1, row=3, padx=150)
quit_button = Button(root, text="Quit", command=root.destroy).grid(column=1, row=4, padx=150, pady=5)

# Note: if we use the variable 'grid' in the same line as the object
# we are positioning it will be not able to be changed inside a function
# so, with 'mylabel' we rather do it in separated lines, and we save
# some code spaces only with the button


# Don't forget to close the mainloop

root.mainloop()