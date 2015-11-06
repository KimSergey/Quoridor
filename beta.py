from tkinter import *


X1, Y1, X2, Y2 = 4, 8, 4, 0


picture_background_direction = 'floor.png'
picture_button_defolt_direction = 'button_defolt.png'
picture_button_first_direction = 'button_first.png'
picture_button_second_direction = 'button_second.png'
picture_fence_horizontal_defolt_direction = 'fence_horizontal_defolt.png'
picture_fence_horizontal_direction = 'fence_horizontal.png'
picture_fence_vertical_defolt_direction = 'fence_vertical_defolt.png'
picture_fence_vertical_direction = 'fence_vertical.png'


colour_square_defolt = '#A00A0A'
colour_fence_defolt = '#800808'


step = 1
flag_first = 1
flag_second = 1
fence_number_first = 10
fence_number_second = 10
fence_first = None
fence_second = None
information_first = 'P48'
information_second = 'P40'


matrix = [[None for i in range(9)] for j in range(9)]
fences_horizontal = [[None for i in range(9)] for j in range(9)]
fences_vertical = [[None for i in range(9)] for j in range(9)]


def do_step(statistics_self, statistics_other, step, self):

    if statistics_self['flag'] == 1:
        if (self.widget['text'][0:3][0] == 'H' or self.widget['text'][0:3][0] == 'V') and statistics_self['fence_number'] > 0:
            statistics_self['fence'] = self.widget['text']
            statistics_self['flag'] = 2
            if self.widget['text'][0:3][0] == 'H':
                self.widget['image'] = picture_fence_horizontal
            if self.widget['text'][0:3][0] == 'V':
                self.widget['image'] = picture_fence_vertical
            self.widget['text'] = str(step)
            statistics_self['fence_number'] -= 1
        elif self.widget['text'][0:3][0] == 'P':
            legal = 0
            if (int(self.widget['text'][0:3][1]) - int(statistics_self['information'][1]) == -1 and
                int(self.widget['text'][0:3][2]) - int(statistics_self['information'][2]) == 0):
                if fences_vertical[int(self.widget['text'][0:3][1])][int(self.widget['text'][0:3][2])]['text'][0] == 'V':
                    legal = 1
            if (int(self.widget['text'][0:3][1]) - int(statistics_self['information'][1]) == 1 and
                int(self.widget['text'][0:3][2]) - int(statistics_self['information'][2]) == 0):
                if fences_vertical[int(statistics_self['information'][1])][int(statistics_self['information'][2])]['text'][0] == 'V':
                    legal = 1
            if (int(self.widget['text'][0:3][1]) - int(statistics_self['information'][1]) == 0 and
                int(self.widget['text'][0:3][2]) - int(statistics_self['information'][2]) == -1):
                if fences_horizontal[int(self.widget['text'][0:3][1])][int(self.widget['text'][0:3][2])]['text'][0] == 'H':
                    legal = 1
            if (int(self.widget['text'][0:3][1]) - int(statistics_self['information'][1]) == 0 and
                int(self.widget['text'][0:3][2]) - int(statistics_self['information'][2]) == 1):
                if fences_horizontal[int(statistics_self['information'][1])][int(statistics_self['information'][2])]['text'][0] == 'H':
                    legal = 1
            if legal == 1:
                matrix[int(statistics_self['information'][1])][int(statistics_self['information'][2])]['image'] = picture_button_defolt
                statistics_self['information'] = self.widget['text'][0:3]
                self.widget['text'] = self.widget['text'][0:3] + ' ' + str(step)
                self.widget['image'] = statistics_self['picture']
                step += 1
    elif statistics_self['flag'] == 2:
        if self.widget['text'][0:3][0] == statistics_self['fence'][0] == 'H':
            if (abs(int(self.widget['text'][0:3][1]) - int(statistics_self['fence'][1])) == 1 and
                abs(int(self.widget['text'][0:3][2]) - int(statistics_self['fence'][2])) == 0):
                if self.widget['text'][0:3][0] == 'H':
                    self.widget['image'] = picture_fence_horizontal
                    self.widget['text'] = str(step)
                    statistics_self['flag'] = 1
                    step += 1
        elif self.widget['text'][0:3][0] == statistics_self['fence'][0] == 'V':
            if (abs(int(self.widget['text'][0:3][2]) - int(statistics_self['fence'][2])) == 1 and
                abs(int(self.widget['text'][0:3][1]) - int(statistics_self['fence'][1])) == 0):
                if self.widget['text'][0:3][0] == 'V':
                    self.widget['image'] = picture_fence_vertical
                    self.widget['text'] = str(step)
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
picture_button_defolt = PhotoImage(file=picture_button_defolt_direction)
picture_button_first = PhotoImage(file=picture_button_first_direction)
picture_button_second = PhotoImage(file=picture_button_second_direction)
picture_fence_horizontal_defolt = PhotoImage(file=picture_fence_horizontal_defolt_direction)
picture_fence_horizontal = PhotoImage(file=picture_fence_horizontal_direction)
picture_fence_vertical_defolt = PhotoImage(file=picture_fence_vertical_defolt_direction)
picture_fence_vertical = PhotoImage(file=picture_fence_vertical_direction)


statistics_first = {'flag': flag_first,
                    'fence_number': fence_number_first,
                    'fence': fence_first,
                    'information': information_first,
                    'picture': picture_button_first}
statistics_second = {'flag': flag_second,
                     'fence_number': fence_number_second,
                     'fence': fence_second,
                     'information': information_second,
                     'picture': picture_button_second}


Label(root, image=picture_background).pack()
for i in range(9):
    for j in range(9):
        picture = picture_button_defolt
        if i == X1 and j == Y1:
            picture = picture_button_first
        if i == X2 and j == Y2:
            picture = picture_button_second
        matrix[i][j] = Button(root,
                              bg=colour_square_defolt,
                              fg=colour_square_defolt,
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
        fences_horizontal[i][j] = Button(root,
                                         bg=colour_fence_defolt,
                                         fg=colour_fence_defolt,
                                         image=picture,
                                         text='H'+str(i)+str(j))
        fences_horizontal[i][j].place(x=470+75*i,
                                      y=180+75*j,
                                      width=60,
                                      height=15)        
for i in range(-1, 9):
    for j in range(9):
        picture = picture_fence_vertical_defolt
        if i == -1 or i == 8:
            picture = picture_fence_vertical
        fences_vertical[i][j] = Button(root,
                                       bg=colour_fence_defolt,
                                       fg=colour_fence_defolt,
                                       image=picture,
                                       text='V'+str(i)+str(j))
        fences_vertical[i][j].place(x=530+75*i,
                                    y=120+75*j,
                                    width=15,
                                    height=60)
can.pack()
root.bind_class('Button', '<1>', button_clicked)
root.mainloop()
