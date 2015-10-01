X1, Y1, X2, Y2 = 4, 0, 4, 8

from tkinter import *
import sys
import time 

class Figure:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, direct):
        if direct == 1:
            self.x += 1
        if direct == 2:
            self.y += 1
        if direct == 3:
            self.x -= 1
        if direct == 4:
            self.y -= 1
            


squares = []
def create_table(x1, y1, x2, y2):
    
    root = Tk()
    root.title("Game")
    root.wm_geometry("+%d+%d" % (0, 0))
    can = Canvas(root, width = root.winfo_screenwidth() - 18, height = root.winfo_screenheight())
    can.create_rectangle(480, 47, 1120, 677, fill = "black")
    can.create_rectangle(485, 52, 1115, 672, fill = "brown")

    for i in range(9):
        for j in range(9):
            if i == x1 and j == y1:
                but = Button(root, bg = 'red')
            elif i == x2 and j == y2:
                but = Button(root, bg = 'yellow')
            else:
                but = Button(root, bg = 'orange')
            but.place(relx = 0.3135 + i / 23, rely = 0.688 - j / 13, width = 55, height = 55)
            squares.append(but)
                
    
    for i in range(9):
        for j in range(8):
            but = Button(root, bg='brown')
            but.place(x=497 + 69 * i, y=118 + 67.5 * j, width=54, height=12)
    
    for i in range(8):
        for j in range(9):
            but = Button(root, bg='brown')
            but.place(x=552 + 69 * i, y=64 + 67.5 * j, width=13, height=54)
    can.pack()
    root.mainloop()
create_table(X1, Y1, X2, Y2)




figure_white = Figure(4, 0)
figure_black = Figure(4, 8)
step_number = 1
while True:
    if step_number % 2 == 1:
        for but in squares:
            but.bind('<Button-1>', create_table(1, 1, 3, 3))
    if step_number % 2 == 0:
        for but in squares:
            but.bind('<Button-1>', create_table(2, 2, 4, 4))
    step_number += 1
