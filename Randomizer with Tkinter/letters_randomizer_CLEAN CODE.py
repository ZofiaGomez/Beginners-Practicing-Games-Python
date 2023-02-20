# "CLEAN CODE" (you can copy any of these codes into your code editor 
# and run it to see how it works. Copy only one method at a time)

# Be sure to check the README file for this program

from tkinter import *
import random as r

root=Tk()
root.title("Letters Randomizer")
root.geometry('400x300')
root.config(bg='#856ff8')


# METHOD Nº 1:

def randomize_method1():
    letter_rand = r.choice(rand1.split(','))
    mylabel.config(text=letter_rand)

rand1 = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
letter_rand = r.choice(rand1.split(','))

mylabel = Label(root, text=letter_rand, bg='#856ff8', font=('Helvetica 75 bold'), justify='center')
mylabel.grid(row=1, column=1, pady=25, padx=150)

regenerate_button = Button(root, text="Regenerate", command=randomize_method1).grid(column=1, row=3, padx=150)
quit_button = Button(root, text="Quit", command=root.destroy).grid(column=1, row=4, padx=150, pady=5)

root.mainloop()


# METHOD Nº 2:

def randomize_method2():
    rand2 = chr(r.randint(ord('A'), ord('Z')))
    mylabel.config(text=rand2)

rand2 = chr(r.randint(ord('A'), ord('Z')))

mylabel = Label(root, text=rand2, bg='#856ff8', font=('Helvetica 75 bold'), justify='center')
mylabel.grid(row=1, column=1, pady=25, padx=150)

regenerate_button = Button(root, text="Regenerate", command=randomize_method2).grid(column=1, row=3, padx=150)
quit_button = Button(root, text="Quit", command=root.destroy).grid(column=1, row=4, padx=150, pady=5)

root.mainloop()