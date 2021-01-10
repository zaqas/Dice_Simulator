from tkinter import *
import tkinter as tk
import random as rand
from PIL import ImageTk, Image

white_dices = ['wd1.gif', 'wd2.gif', 'wd3.gif', 'wd4.gif', 'wd5.gif', 'wd6.gif']
red_dices = ['rd1.gif', 'rd2.gif', 'rd3.gif', 'rd4.gif', 'rd5.gif', 'rd6.gif']

root = Tk()


def main():
    # Main window
    root.geometry('700x600')
    root.configure(background='#E3E3E3')
    root.resizable(0, 0)
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='image/dice.gif'))
    root.title('Dice Simulator')

    # Roll Button
    Button(root, text='Roll', height=2, width=20, bg='#E3E3E3', font=('helvetica', 12, 'normal'),
           command=btnClickFunction).place(x=145, y=400)

    load = Image.open('image/wd1.gif')
    render = ImageTk.PhotoImage(load)

    img = Label(root, image=render)
    img.image = render
    img.place(x=85, y=47)

    load_red = Image.open('image/rd2.gif')
    render_red = ImageTk.PhotoImage(load_red)

    img = Label(root, image=render_red)
    img.image = render_red
    img.place(x=405, y=47)

    root.mainloop()


# this is the function called when the button is clicked
def btnClickFunction():
    random1 = rand.randint(0, 5)
    random2 = rand.randint(0, 5)

    wd = white_dices[random2]
    rd = red_dices[random1]

    load_new = Image.open('image/'+wd)
    render_new = ImageTk.PhotoImage(load_new)
    img = Label(root, image=render_new)
    img.image = render_new
    img.place(x=85, y=47)

    load_new_red = Image.open('image/'+rd)
    render_new_red = ImageTk.PhotoImage(load_new_red)
    img = Label(root, image=render_new_red)
    img.image = render_new_red
    img.place(x=405, y=47)


if __name__ == '__main__':
    main()
