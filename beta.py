from tkinter import *


X1, Y1, X2, Y2 = 4, 8, 4, 0
picture_background_direction = 'floor.png'
picture_button_direction = 'button.png'
picture_first_direction = 'first_player.png'
picture_second_direction = 'second_player.png'
colour_square_defolt = '#A00A0A'
colour_fence_defolt = '#800808'
colour_fence = '#00A0A0'
colour_first = '#00A000'
colour_second = '#A0A000'
step_first = 1
step_second = 1
flag_first = 1
flag_second = 1
fence_number_first = 10
fence_number_second = 10
fence_first = 'F00'
fence_second = 'F00'
information_first = 'P48'
information_second = 'P40'


matrix = [[None for i in range(9)] for j in range(9)]

def button_clicked(self):

    global colour_fence
    global colour_first, colour_second
    global step_first, step_second
    global flag_first, flag_second
    global fence_number_first, fence_number_second
    global fence_first, fence_second
    global information_first, information_second
    information_self = self.widget['text'][0:3]

    if step_first == step_second:
        if flag_first == 1:
            if (information_self[0] == 'H' or information_self[0] == 'V') and fence_number_first > 0:
                fence_first = self.widget['text']
                flag_first = 2
                self.widget['text'] = str(step_first)
                self.widget['bg'] = colour_fence
                self.widget['fg'] = colour_fence
                fence_number_first -= 1
            elif information_self[0] == 'P':
                if (information_self != information_second and
                    abs(int(information_self[1]) - int(information_first[1])) <= 1 and
                    abs(int(information_self[2]) - int(information_first[2])) <= 1 and
                    abs(int(information_self[1]) - int(information_first[1])) != abs(int(information_self[2]) - int(information_first[2]))):
                    matrix[int(information_first[1])][int(information_first[2])]['image'] = picture_button
                    information_first = information_self
                    self.widget['text'] = information_self + ' ' + str(step_first)
                    self.widget['bg'] = colour_first
                    self.widget['fg'] = 'white'
                    self.widget['image'] = picture_first
                    self.widget['activebackground'] = colour_first
                    step_first += 1
        elif flag_first == 2:
            if information_self[0] == fence_first[0] == 'H':
                    if abs(int(information_self[1]) - int(fence_first[1])) == 1:
                        self.widget['text'] = str(step_first)
                        self.widget['bg'] = colour_fence
                        self.widget['fg'] = colour_fence
                        flag_first = 1
                        step_first += 1
            elif information_self[0] == fence_first[0] == 'V':
                    if abs(int(information_self[2]) - int(fence_first[2])) == 1:
                        self.widget['text'] = str(step_first)
                        self.widget['bg'] = colour_fence
                        self.widget['fg'] = colour_fence
                        flag_first = 1
                        step_first += 1

    elif step_first != step_second:
        if flag_second == 1:
            if (information_self[0] == 'H' or information_self[0] == 'V') and fence_number_second > 0:
                fence_second = self.widget['text']
                flag_second = 2
                self.widget['text'] = str(step_second)
                self.widget['bg'] = colour_fence
                self.widget['fg'] = colour_fence
                fence_number_second -= 1
            elif information_self[0] == 'P':
                if (information_self != information_first and
                    abs(int(information_self[1]) - int(information_second[1])) <= 1 and
                    abs(int(information_self[2]) - int(information_second[2])) <= 1 and
                    abs(int(information_self[1]) - int(information_second[1])) != abs(int(information_self[2]) - int(information_second[2]))):
                    matrix[int(information_second[1])][int(information_second[2])]['image'] = picture_button
                    information_second = information_self
                    self.widget['text'] = information_self + ' ' + str(step_second)
                    self.widget['bg'] = colour_second
                    self.widget['fg'] = 'white'
                    self.widget['image'] = picture_second
                    self.widget['activebackground'] = colour_second
                    step_second += 1
        elif flag_second == 2:
            if information_self[0] == fence_second[0] == information_self[0] == 'H':
                if abs(int(information_self[1]) - int(fence_second[1])) == 1:
                    self.widget['text'] = str(step_second)
                    self.widget['bg'] = colour_fence
                    self.widget['fg'] = colour_fence
                    flag_second = 1
                    step_second += 1
            elif information_self[0] == fence_second[0] == 'V':
                if abs(int(information_self[2]) - int(fence_second[2])) == 1:
                    self.widget['text'] = str(step_second)
                    self.widget['bg'] = colour_fence
                    self.widget['fg'] = colour_fence
                    flag_second = 1
                    step_second += 1


root = Tk()
root.title("Quoridor")
root.wm_geometry("+%d+%d" % (0, 0))
can = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
picture_background = PhotoImage(file=picture_background_direction)
picture_button = PhotoImage(file=picture_button_direction)
picture_first = PhotoImage(file=picture_first_direction)
picture_second = PhotoImage(file=picture_second_direction)
Label(root, image=picture_background).pack()
for i in range(9):
    for j in range(9):
        colour = colour_square_defolt
        if i == X1 and j == Y1:
            colour = colour_first
        if i == X2 and j == Y2:
            colour = colour_second
        matrix[i][j] = Button(root,
                              bg=colour,
                              fg=colour,
                              image=picture_button,
                              text='P'+str(i)+str(j))
        matrix[i][j].place(x=470+75*i,
                           y=120+75*j,
                           width=60,
                           height=60)
for i in range(9):
    for j in range(8):
        Button(root,
               bg=colour_fence_defolt,
               fg=colour_fence_defolt,
               text='H'+str(i)+str(j)).place(x=470+75*i,
                                             y=180+75*j,
                                             width=60,
                                             height=15)
for i in range(8):
    for j in range(9):
        Button(root,
               bg=colour_fence_defolt,
               fg=colour_fence_defolt,
               text='V'+str(i)+str(j)).place(x=530+75*i,
                                             y=120+75*j,
                                             width=15,
                                             height=60)
can.pack()
root.bind_class('Button', '<1>', button_clicked)
root.mainloop()
