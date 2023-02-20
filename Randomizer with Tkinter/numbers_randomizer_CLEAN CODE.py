# "CLEAN CODE" (you can copy any of these codes into your code editor 
# and run it to see how it works)

# Be sure to check the README file for this program

from tkinter import *
import random as r

root=Tk()
root.title("Numbers Randomizer")
root.geometry('400x300')
root.config(bg='#856ff8')

def randomize():
    rand = r.randint(1,12)
    mylabel.config(text=rand)
    
rand = r.randint(1,12)
mylabel = Label(root, text=rand, bg='#856ff8', font=('Helvetica 75 bold'), justify='center')
mylabel.grid(row=1, column=1, pady=25, padx=150)

# ttk.Label(root, text="Hello World!").grid(column=0, row=0)
regenerate_button = Button(root, text="Regenerate", command=randomize).grid(column=1, row=3, padx=150)
quit_button = Button(root, text="Quit", command=root.destroy).grid(column=1, row=4, padx=150, pady=5)

root.mainloop()