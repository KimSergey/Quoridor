from tkinter import *


X1, Y1, X2, Y2 = 4, 8, 4, 0


picture_background_direction = 'floor.png'
picture_button_defolt_direction = 'button_defolt.png'
picture_fence_horizontal_defolt_direction = 'fence_horizontal_defolt.png'
picture_fence_vertical_defolt_direction = 'fence_vertical_defolt.png'
picture_fence_horizontal_direction = 'fence_horizontal.png'
picture_fence_vertical_direction = 'fence_vertical.png'
picture_button_first_direction = 'button_first.png'
picture_button_second_direction = 'button_second.png'


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
statistics_first = {'step': step_first,
                    'flag': flag_first,
                    'fence_number': fence_number_first,
                    'fence': fence_first,
                    'information': information_first}
statistics_second = {'step': step_second,
                     'flag': flag_second,
                     'fence_number': fence_number_second,
                     'fence': fence_second,
                     'information': information_second}


matrix = [[None for i in range(9)] for j in range(9)]
fences_horizontal = [[None for i in range(9)] for j in range(9)]
fences_vertical = [[None for i in range(9)] for j in range(9)]


def button_clicked(self):
    
    global statistics_first, statistics_second
    information_self = self.widget['text'][0:3]

    if statistics_first['step'] == statistics_second['step']:
        if statistics_first['flag'] == 1:
            if (information_self[0] == 'H' or information_self[0] == 'V') and statistics_first['fence_number'] > 0:
                statistics_first['fence'] = self.widget['text']
                statistics_first['flag'] = 2
                self.widget['bg'] = colour_fence
                self.widget['fg'] = colour_fence
                if information_self[0] == 'H':
                    self.widget['image'] = picture_fence_horizontal
                if information_self[0] == 'V':
                    self.widget['image'] = picture_fence_vertical
                self.widget['text'] = str(statistics_first['step'])
                statistics_first['fence_number'] -= 1
            elif information_self[0] == 'P':
                if (information_self != statistics_second['information'] and
                    abs(int(information_self[1]) - int(statistics_first['information'][1])) <= 1 and
                    abs(int(information_self[2]) - int(statistics_first['information'][2])) <= 1 and
                    abs(int(information_self[1]) - int(statistics_first['information'][1])) != abs(int(information_self[2]) - int(statistics_first['information'][2]))):
                    matrix[int(statistics_first['information'][1])][int(statistics_first['information'][2])]['image'] = picture_button_defolt
                    statistics_first['information'] = information_self
                    self.widget['text'] = information_self + ' ' + str(statistics_first['step'])
                    self.widget['bg'] = colour_first
                    self.widget['fg'] = 'white'
                    self.widget['image'] = picture_button_first
                    self.widget['activebackground'] = colour_first
                    statistics_first['step'] += 1
        elif statistics_first['flag'] == 2:
            if information_self[0] == statistics_first['fence'][0] == 'H':
                    if (abs(int(information_self[1]) - int(statistics_first['fence'][1])) == 1 and
                        abs(int(information_self[2]) - int(statistics_first['fence'][2])) == 0):
                        self.widget['bg'] = colour_fence
                        self.widget['fg'] = colour_fence
                        if information_self[0] == 'H':
                            self.widget['image'] = picture_fence_horizontal
                        self.widget['text'] = str(statistics_first['step'])
                        statistics_first['flag'] = 1
                        statistics_first['step'] += 1
            elif information_self[0] == statistics_first['fence'][0] == 'V':
                    if (abs(int(information_self[2]) - int(statistics_first['fence'][2])) == 1 and
                        abs(int(information_self[1]) - int(statistics_first['fence'][1])) == 0):
                        self.widget['bg'] = colour_fence
                        self.widget['fg'] = colour_fence
                        if information_self[0] == 'V':
                            self.widget['image'] = picture_fence_vertical
                        self.widget['text'] = str(statistics_first['step'])
                        statistics_first['flag'] = 1
                        statistics_first['step'] += 1

    elif statistics_first['step'] != statistics_second['step']:
        if statistics_second['flag'] == 1:
            if (information_self[0] == 'H' or information_self[0] == 'V') and statistics_second['fence_number'] > 0:
                statistics_second['fence'] = self.widget['text']
                statistics_second['flag'] = 2
                self.widget['bg'] = colour_fence
                self.widget['fg'] = colour_fence
                if information_self[0] == 'H':
                    self.widget['image'] = picture_fence_horizontal
                if information_self[0] == 'V':
                    self.widget['image'] = picture_fence_vertical
                self.widget['text'] = str(statistics_second['step'])
                statistics_second['fence_number'] -= 1
            elif information_self[0] == 'P':
                if (information_self != statistics_first['information'] and
                    abs(int(information_self[1]) - int(statistics_second['information'][1])) <= 1 and
                    abs(int(information_self[2]) - int(statistics_second['information'][2])) <= 1 and
                    abs(int(information_self[1]) - int(statistics_second['information'][1])) != abs(int(information_self[2]) - int(statistics_second['information'][2]))):
                    matrix[int(statistics_second['information'][1])][int(statistics_second['information'][2])]['image'] = picture_button_defolt
                    statistics_second['information'] = information_self
                    self.widget['text'] = information_self + ' ' + str(statistics_second['step'])
                    self.widget['bg'] = colour_second
                    self.widget['fg'] = 'white'
                    self.widget['image'] = picture_button_second
                    self.widget['activebackground'] = colour_second
                    statistics_second['step'] += 1
        elif statistics_second['flag'] == 2:
            if information_self[0] == statistics_second['fence'][0] == information_self[0] == 'H':
                if (abs(int(information_self[1]) - int(statistics_second['fence'][1])) == 1 and
                    abs(int(information_self[2]) - int(statistics_second['fence'][2])) == 0):
                    self.widget['bg'] = colour_fence
                    self.widget['fg'] = colour_fence
                    if information_self[0] == 'H':
                        self.widget['image'] = picture_fence_horizontal
                    self.widget['text'] = str(statistics_second['step'])
                    statistics_second['flag'] = 1
                    statistics_second['step'] += 1
            elif information_self[0] == statistics_second['fence'][0] == 'V':
                if (abs(int(information_self[2]) - int(statistics_second['fence'][2])) == 1 and
                    abs(int(information_self[1]) - int(statistics_second['fence'][1])) == 0):
                    self.widget['bg'] = colour_fence
                    self.widget['fg'] = colour_fence
                    if information_self[0] == 'V':
                        self.widget['image'] = picture_fence_vertical
                    self.widget['text'] = str(statistics_second['step'])
                    statistics_second['flag'] = 1
                    statistics_second['step'] += 1


root = Tk()
root.title("Quoridor")
root.wm_geometry("+%d+%d" % (0, 0))
can = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
picture_background = PhotoImage(file=picture_background_direction)
picture_button_defolt = PhotoImage(file=picture_button_defolt_direction)
picture_fence_horizontal_defolt = PhotoImage(file=picture_fence_horizontal_defolt_direction)
picture_fence_vertical_defolt = PhotoImage(file=picture_fence_vertical_defolt_direction)
picture_fence_horizontal = PhotoImage(file=picture_fence_horizontal_direction)
picture_fence_vertical = PhotoImage(file=picture_fence_vertical_direction)
picture_button_first = PhotoImage(file=picture_button_first_direction)
picture_button_second = PhotoImage(file=picture_button_second_direction)
Label(root, image=picture_background).pack()
for i in range(9):
    for j in range(9):
        colour = colour_square_defolt
        picture = picture_button_defolt
        if i == X1 and j == Y1:
            colour = colour_first
            picture = picture_button_first
        if i == X2 and j == Y2:
            colour = colour_second
            picture = picture_button_second
        matrix[i][j] = Button(root,
                              bg=colour,
                              fg=colour,
                              image=picture,
                              text='P'+str(i)+str(j))
        matrix[i][j].place(x=470+75*i,
                           y=120+75*j,
                           width=60,
                           height=60)
for i in range(9):
    for j in range(-1, 9):
        picture = picture_fence_horizontal_defolt
        if j == -1 or j == 8:
            picture = picture_fence_horizontal
        Button(root,
               bg=colour_fence_defolt,
               fg=colour_fence_defolt,
               image=picture,
               text='H'+str(i)+str(j)).place(x=470+75*i,
                                             y=180+75*j,
                                             width=60,
                                             height=15)
for i in range(-1, 9):
    for j in range(9):
        picture = picture_fence_vertical_defolt
        if i == -1 or i == 8:
            picture = picture_fence_vertical
        Button(root,
               bg=colour_fence_defolt,
               fg=colour_fence_defolt,
               image=picture,
               text='V'+str(i)+str(j)).place(x=530+75*i,
                                             y=120+75*j,
                                             width=15,
                                             height=60)
can.pack()
root.bind_class('Button', '<1>', button_clicked)
root.mainloop()
