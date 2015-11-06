from tkinter import *


X1, Y1, X2, Y2 = 4, 8, 4, 0


picture_background_direction = 'floor.png'
picture_button_default_direction = 'button_default.png'
picture_button_first_direction = 'button_first.png'
picture_button_second_direction = 'button_second.png'
picture_fence_horizontal_default_direction = 'fence_horizontal_default.png'
picture_fence_horizontal_direction = 'fence_horizontal.png'
picture_fence_vertical_default_direction = 'fence_vertical_default.png'
picture_fence_vertical_direction = 'fence_vertical.png'


colour_square_default = '#A00A0A'
colour_fence_default = '#800808'


step = 1
flag_first = 1
flag_second = 1
fence_number_first = 10
fence_number_second = 10
fence_first = None
fence_second = None
information_first = 'P48'
information_second = 'P40'


def do_step(statistics_self, statistics_other, step, self):

    if statistics_self['flag'] == 1:
        if (self.widget['text'][0] == 'H' or self.widget['text'][0] == 'V') and statistics_self['fence_number'] > 0:
            statistics_self['fence'] = self.widget['text']
            statistics_self['flag'] = 2
            if self.widget['text'][0] == 'H':
                self.widget['image'] = picture_fence_horizontal
            if self.widget['text'][0] == 'V':
                self.widget['image'] = picture_fence_vertical
            self.widget['text'] = 'F' + self.widget['text'][1] + self.widget['text'][2]
            statistics_self['fence_number'] -= 1
        elif self.widget['text'][0] == 'P':
            legal = 0
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == -1 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == 0):
                if fences_vertical[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['text'][0] == 'V':
                    legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == 0 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == -1):
                if fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['text'][0] == 'H':
                    legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == 1 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == 0):
                if fences_vertical[int(statistics_self['text'][1])+1][int(statistics_self['text'][2])]['text'][0] == 'V':
                    legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == 0 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == 1):
                if fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])+1]['text'][0] == 'H':
                    legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == -2 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == 0):
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == -1 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 0):
                    if (fences_vertical[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['text'][0] == 'V' and
                        fences_vertical[int(statistics_self['text'][1])-1][int(statistics_self['text'][2])]['text'][0] == 'V'):
                        legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == 0 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == -2):
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 0 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == -1):
                    if (fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['text'][0] == 'H' and
                        fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])-1]['text'][0] == 'H'):
                        legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == 2 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == 0):
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 1 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 0):
                    if (fences_vertical[int(statistics_self['text'][1])+1][int(statistics_self['text'][2])]['text'][0] == 'V' and
                        fences_vertical[int(statistics_self['text'][1])+2][int(statistics_self['text'][2])]['text'][0] == 'V'):
                        legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == 0 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == 2):
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 0 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 1):
                    if (fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])+1]['text'][0] == 'H' and
                        fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])+2]['text'][0] == 'H'):
                        legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == -1 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == -1):
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 0 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == -1):
                    if (fences_vertical[int(statistics_self['text'][1])-1][int(statistics_self['text'][2])]['text'][0] == 'F' and
                        fences_vertical[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['text'][0] == 'V' and
                        fences_horizontal[int(statistics_self['text'][1])-1][int(statistics_self['text'][2])]['text'][0] == 'H'):
                        legal = 1
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == -1 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 0):
                    if (fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])-1]['text'][0] == 'F' and
                        fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['text'][0] == 'H' and
                        fences_vertical[int(statistics_self['text'][1])][int(statistics_self['text'][2])-1]['text'][0] == 'V'):
                        legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == 1 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == -1):
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 1 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 0):
                    if (fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])-1]['text'][0] == 'F' and
                        fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['text'][0] == 'H' and
                        fences_vertical[int(statistics_self['text'][1])+1][int(statistics_self['text'][2])-1]['text'][0] == 'V'):
                        legal = 1
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 0 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == -1):
                    if (fences_vertical[int(statistics_self['text'][1])+2][int(statistics_self['text'][2])]['text'][0] == 'F' and
                        fences_vertical[int(statistics_self['text'][1])+1][int(statistics_self['text'][2])]['text'][0] == 'V' and
                        fences_horizontal[int(statistics_self['text'][1])+1][int(statistics_self['text'][2])]['text'][0] == 'H'):
                        legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == 1 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == 1):
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 0 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 1):
                    if (fences_vertical[int(statistics_self['text'][1])+2][int(statistics_self['text'][2])]['text'][0] == 'F' and
                        fences_vertical[int(statistics_self['text'][1])+1][int(statistics_self['text'][2])]['text'][0] == 'V' and
                        fences_horizontal[int(statistics_self['text'][1])+1][int(statistics_self['text'][2])+1]['text'][0] == 'H'):
                        legal = 1
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 1 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 0):
                    if (fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])+2]['text'][0] == 'F' and
                        fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])+1]['text'][0] == 'H' and
                        fences_vertical[int(statistics_self['text'][1])+1][int(statistics_self['text'][2])+1]['text'][0] == 'V'):
                        legal = 1
            if (int(self.widget['text'][1]) - int(statistics_self['text'][1]) == -1 and
                int(self.widget['text'][2]) - int(statistics_self['text'][2]) == 1):
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == -1 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 0):
                    if (fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])+2]['text'][0] == 'F' and
                        fences_horizontal[int(statistics_self['text'][1])][int(statistics_self['text'][2])+1]['text'][0] == 'H' and
                        fences_vertical[int(statistics_self['text'][1])][int(statistics_self['text'][2])+1]['text'][0] == 'V'):
                        legal = 1
                if (int(self.widget['text'][1]) - int(statistics_other['text'][1]) == 0 and
                    int(self.widget['text'][2]) - int(statistics_other['text'][2]) == 1):
                    if (fences_vertical[int(statistics_self['text'][1])-1][int(statistics_self['text'][2])]['text'][0] == 'F' and
                        fences_vertical[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['text'][0] == 'V' and
                        fences_horizontal[int(statistics_self['text'][1])-1][int(statistics_self['text'][2])+1]['text'][0] == 'H'):
                        legal = 1
            if legal == 1:
                matrix[int(statistics_self['text'][1])][int(statistics_self['text'][2])]['image'] = picture_button_default
                statistics_self['text'] = self.widget['text']
                self.widget['text'] = self.widget['text']
                self.widget['image'] = statistics_self['picture']
                step += 1
    elif statistics_self['flag'] == 2:
        if self.widget['text'][0] == statistics_self['fence'][0] == 'H':
            if (abs(int(self.widget['text'][1]) - int(statistics_self['fence'][1])) == 1 and
                abs(int(self.widget['text'][2]) - int(statistics_self['fence'][2])) == 0):
                if self.widget['text'][0] == 'H':
                    self.widget['image'] = picture_fence_horizontal
                    self.widget['text'] = 'F' + self.widget['text'][1] + self.widget['text'][2]
                    statistics_self['flag'] = 1
                    step += 1
        elif self.widget['text'][0] == statistics_self['fence'][0] == 'V':
            if (abs(int(self.widget['text'][2]) - int(statistics_self['fence'][2])) == 1 and
                abs(int(self.widget['text'][1]) - int(statistics_self['fence'][1])) == 0):
                if self.widget['text'][0] == 'V':
                    self.widget['image'] = picture_fence_vertical
                    self.widget['text'] = 'F' + self.widget['text'][1] + self.widget['text'][2]
                    statistics_self['flag'] = 1
                    step += 1

    return statistics_self, step


def button_clicked(self):

    global statistics_first, statistics_second, step

    if step % 2 == 1:
        statistics_first, step = do_step(statistics_first, statistics_second, step, self)
    elif step % 2 == 0:
        statistics_second, step = do_step(statistics_second, statistics_first, step, self)


root = Tk()
root.title("Quoridor")
root.wm_geometry("+%d+%d" % (0, 0))
can = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())


picture_background = PhotoImage(file=picture_background_direction)
picture_button_default = PhotoImage(file=picture_button_default_direction)
picture_button_first = PhotoImage(file=picture_button_first_direction)
picture_button_second = PhotoImage(file=picture_button_second_direction)
picture_fence_horizontal_default = PhotoImage(file=picture_fence_horizontal_default_direction)
picture_fence_horizontal = PhotoImage(file=picture_fence_horizontal_direction)
picture_fence_vertical_default = PhotoImage(file=picture_fence_vertical_default_direction)
picture_fence_vertical = PhotoImage(file=picture_fence_vertical_direction)
statistics_first = {'flag': flag_first,
                    'fence_number': fence_number_first,
                    'fence': fence_first,
                    'text': information_first,
                    'picture': picture_button_first}
statistics_second = {'flag': flag_second,
                     'fence_number': fence_number_second,
                     'fence': fence_second,
                     'text': information_second,
                     'picture': picture_button_second}
Label(root, image=picture_background).pack()


matrix = [[None for i in range(9)] for j in range(9)]
fences_horizontal = [[None for i in range(10)] for j in range(9)]
fences_vertical = [[None for i in range(9)] for j in range(10)]
for i in range(9):
    for j in range(9):
        picture = picture_button_default
        if i == X1 and j == Y1:
            picture = picture_button_first
        if i == X2 and j == Y2:
            picture = picture_button_second
        matrix[i][j] = Button(root,
                              bg=colour_square_default,
                              fg=colour_square_default,
                              image=picture,
                              text='P'+str(i)+str(j))
        matrix[i][j].place(x=470+75*i,
                           y=120+75*j,
                           width=60,
                           height=60)
for i in range(9):
    for j in range(10):
        picture = picture_fence_horizontal_default
        name = 'H'
        if j == 0 or j == 9:
            picture = picture_fence_horizontal
            name = 'F'
        fences_horizontal[i][j] = Button(root,
                                         bg=colour_fence_default,
                                         fg=colour_fence_default,
                                         image=picture,
                                         text=name+str(i)+str(j))
        fences_horizontal[i][j].place(x=470+75*i,
                                      y=105+75*j,
                                      width=60,
                                      height=15)
for i in range(10):
    for j in range(9):
        picture = picture_fence_vertical_default
        name = 'V'
        if i == 0 or i == 9:
            picture = picture_fence_vertical
            name = 'F'
        fences_vertical[i][j] = Button(root,
                                       bg=colour_fence_default,
                                       fg=colour_fence_default,
                                       image=picture,
                                       text=name+str(i)+str(j))
        fences_vertical[i][j].place(x=455+75*i,
                                    y=120+75*j,
                                    width=15,
                                    height=60)


can.pack()
root.bind_class('Button', '<1>', button_clicked)
root.mainloop()
