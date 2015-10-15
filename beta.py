#coding:utf-8
# -*- coding: utf-8 -*-

from tkinter import *

X1, Y1, X2, Y2, X3, Y3, X4, Y4 = 4, 0, 4, 8, 0, 4, 8, 4
step_first = 1
step_second = 1
places_squares = [[None for i in range(9)] for j in range(9)]
spaces_horizontal = [[None for i in range(8)] for j in range(9)]
spaces_vertical = [[None for i in range(9)] for j in range(8)]

def button_clicked(self):
    global step_first
    global step_second
    global button_first
    global button_second
    if step_first == step_second:
        bg = '#%0x%0x%0x' % (1, 8, 1)
        self.widget['text'] = step_first
        step_first += 1
    else:
        bg = '#%0x%0x%0x' % (8, 8, 1)
        self.widget['text'] = step_second
        step_second += 1
    self.widget['bg'] = bg
    self.widget['activebackground'] = bg

root = Tk()
root.title("Game")
root.wm_geometry("+%d+%d" % (0, 0))
can = Canvas(root, width = root.winfo_screenwidth() - 18, height = root.winfo_screenheight())
can.create_rectangle(445-1, 85-1, 1115-1, 755-1, fill="black") #one pixel is very important
can.create_rectangle(450-1, 90-1, 1110-1, 750-1, fill="#AA0A0A")
for i in range(9):
    for j in range(9):
        if i == X1 and j == Y1 or i == X2 and j == Y2 or i == X3 and j == Y3 or i == X4 and j == Y4:
            places_squares[i][j] = Button(root, bg='#804020', text='0')
            places_squares[i][j].place(x=450+75*i, 
                                       y=90+75*j, 
                                       width=60, 
                                       height=60)

        else:
            places_squares[i][j] = Button(root, bg='#A00A0A')
            places_squares[i][j].place(x=450+75*i, 
                                       y=90+75*j, 
                                       width=60, 
                                       height=60)
button_first = [places_squares[4][0], 4, 0]
button_second = [places_squares[4][8], 4, 8]
for i in range(9):
    for j in range(8):
        spaces_horizontal[i][j] = Button(root, bg='#800808')
        spaces_horizontal[i][j].place(x=450+75*i, 
                                      y=150+75*j, 
                                      width=60, 
                                      height=15)
for i in range(8):
    for j in range(9):
        spaces_vertical[i][j] = Button(root, bg='#800808')
        spaces_vertical[i][j].place(x=510+75*i, 
                                    y=90+75*j, 
                                    width=15, 
                                    height=60)
can.pack()
root.bind_class('Button', '<1>', button_clicked)
root.mainloop()
