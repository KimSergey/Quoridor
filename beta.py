from tkinter import *


CELL_LENGTH = 60
CELL_WIDTH = 60
FENCE_LENGTH = 60
FENCE_WIDTH = 15
TABLE_LENGTH = 9
TABLE_WIDTH = 9
NAME_CELL = 'C'
NAME_FENCE = 'F'
NAME_HORIZONTAL = 'H'
NAME_VERTICAL = 'V'
X1, Y1, X2, Y2 = 4, 8, 4, 0


colour_default = 'brown'
picture_background_direction = 'floor.png'
picture_button_default_direction = 'button_default.png'
picture_button_first_direction = 'button_first.png'
picture_button_second_direction = 'button_second.png'
picture_fence_horizontal_default_direction = 'fence_horizontal_default.png'
picture_fence_horizontal_direction = 'fence_horizontal.png'
picture_fence_vertical_default_direction = 'fence_vertical_default.png'
picture_fence_vertical_direction = 'fence_vertical.png'


step_number = 1
flag_first = 1
flag_second = 1
fence_number_first = 10
fence_number_second = 10
fence_first = None
fence_second = None
text_first = NAME_CELL + str(X1) + str(Y1)
text_second = NAME_CELL + str(X2) + str(Y2)


def step(info_self, info_other, step_number, self):

    info_click = self.widget
    if info_self['flag'] == 1:
        if (info_click['text'][0] == NAME_HORIZONTAL or info_click['text'][0] == NAME_VERTICAL) and info_self['fence_number'] > 0:
            info_self['fence_click'] = info_click['text']
            info_self['flag'] = 2
            if info_click['text'][0] == NAME_HORIZONTAL:
                info_click['image'] = picture_fence_horizontal
            if info_click['text'][0] == NAME_VERTICAL:
                info_click['image'] = picture_fence_vertical
            info_click['text'] = NAME_FENCE + info_click['text'][1] + info_click['text'][2]
            info_self['fence_number'] -= 1
        elif info_click['text'][0] == NAME_CELL:
            legal = 0
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == -1 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == 0):
                if fences_vertical[int(info_self['text'][1])][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL:
                    legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == 0 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == -1):
                if fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])]['text'][0] == NAME_HORIZONTAL:
                    legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == 1 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == 0):
                if fences_vertical[int(info_self['text'][1])+1][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL:
                    legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == 0 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == 1):
                if fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])+1]['text'][0] == NAME_HORIZONTAL:
                    legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == -2 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == 0):
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == -1 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 0):
                    if (fences_vertical[int(info_self['text'][1])][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL and
                        fences_vertical[int(info_self['text'][1])-1][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL):
                        legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == 0 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == -2):
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 0 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == -1):
                    if (fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])]['text'][0] == NAME_HORIZONTAL and
                        fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])-1]['text'][0] == NAME_HORIZONTAL):
                        legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == 2 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == 0):
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 1 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 0):
                    if (fences_vertical[int(info_self['text'][1])+1][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL and
                        fences_vertical[int(info_self['text'][1])+2][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL):
                        legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == 0 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == 2):
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 0 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 1):
                    if (fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])+1]['text'][0] == NAME_HORIZONTAL and
                        fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])+2]['text'][0] == NAME_HORIZONTAL):
                        legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == -1 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == -1):
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 0 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == -1):
                    if (fences_vertical[int(info_self['text'][1])-1][int(info_self['text'][2])]['text'][0] == NAME_FENCE and
                        fences_vertical[int(info_self['text'][1])][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL and
                        fences_horizontal[int(info_self['text'][1])-1][int(info_self['text'][2])]['text'][0] == NAME_HORIZONTAL):
                        legal = 1
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == -1 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 0):
                    if (fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])-1]['text'][0] == NAME_FENCE and
                        fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])]['text'][0] == NAME_HORIZONTAL and
                        fences_vertical[int(info_self['text'][1])][int(info_self['text'][2])-1]['text'][0] == NAME_VERTICAL):
                        legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == 1 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == -1):
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 1 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 0):
                    if (fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])-1]['text'][0] == NAME_FENCE and
                        fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])]['text'][0] == NAME_HORIZONTAL and
                        fences_vertical[int(info_self['text'][1])+1][int(info_self['text'][2])-1]['text'][0] == NAME_VERTICAL):
                        legal = 1
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 0 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == -1):
                    if (fences_vertical[int(info_self['text'][1])+2][int(info_self['text'][2])]['text'][0] == NAME_FENCE and
                        fences_vertical[int(info_self['text'][1])+1][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL and
                        fences_horizontal[int(info_self['text'][1])+1][int(info_self['text'][2])]['text'][0] == NAME_HORIZONTAL):
                        legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == 1 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == 1):
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 0 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 1):
                    if (fences_vertical[int(info_self['text'][1])+2][int(info_self['text'][2])]['text'][0] == NAME_FENCE and
                        fences_vertical[int(info_self['text'][1])+1][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL and
                        fences_horizontal[int(info_self['text'][1])+1][int(info_self['text'][2])+1]['text'][0] == NAME_HORIZONTAL):
                        legal = 1
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 1 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 0):
                    if (fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])+2]['text'][0] == NAME_FENCE and
                        fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])+1]['text'][0] == NAME_HORIZONTAL and
                        fences_vertical[int(info_self['text'][1])+1][int(info_self['text'][2])+1]['text'][0] == NAME_VERTICAL):
                        legal = 1
            if (int(info_click['text'][1]) - int(info_self['text'][1]) == -1 and
                int(info_click['text'][2]) - int(info_self['text'][2]) == 1):
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == -1 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 0):
                    if (fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])+2]['text'][0] == NAME_FENCE and
                        fences_horizontal[int(info_self['text'][1])][int(info_self['text'][2])+1]['text'][0] == NAME_HORIZONTAL and
                        fences_vertical[int(info_self['text'][1])][int(info_self['text'][2])+1]['text'][0] == NAME_VERTICAL):
                        legal = 1
                if (int(info_click['text'][1]) - int(info_other['text'][1]) == 0 and
                    int(info_click['text'][2]) - int(info_other['text'][2]) == 1):
                    if (fences_vertical[int(info_self['text'][1])-1][int(info_self['text'][2])]['text'][0] == NAME_FENCE and
                        fences_vertical[int(info_self['text'][1])][int(info_self['text'][2])]['text'][0] == NAME_VERTICAL and
                        fences_horizontal[int(info_self['text'][1])-1][int(info_self['text'][2])+1]['text'][0] == NAME_HORIZONTAL):
                        legal = 1
            if legal == 1:
                cells[int(info_self['text'][1])][int(info_self['text'][2])]['image'] = picture_button_default
                info_self['text'] = info_click['text']
                info_click['text'] = info_click['text']
                info_click['image'] = info_self['picture']
                step_number += 1
    elif info_self['flag'] == 2:
        if info_click['text'][0] == info_self['fence_click'][0] == NAME_HORIZONTAL:
            if (abs(int(info_click['text'][1]) - int(info_self['fence_click'][1])) == 1 and
                abs(int(info_click['text'][2]) - int(info_self['fence_click'][2])) == 0):
                if info_click['text'][0] == NAME_HORIZONTAL:
                    info_click['image'] = picture_fence_horizontal
                    info_click['text'] = NAME_FENCE + info_click['text'][1] + info_click['text'][2]
                    info_self['flag'] = 1
                    step_number += 1
        elif info_click['text'][0] == info_self['fence_click'][0] == NAME_VERTICAL:
            if (abs(int(info_click['text'][2]) - int(info_self['fence_click'][2])) == 1 and
                abs(int(info_click['text'][1]) - int(info_self['fence_click'][1])) == 0):
                if info_click['text'][0] == NAME_VERTICAL:
                    info_click['image'] = picture_fence_vertical
                    info_click['text'] = NAME_FENCE + info_click['text'][1] + info_click['text'][2]
                    info_self['flag'] = 1
                    step_number += 1
    return info_self, step_number


def button_click(self):

    global info_first, info_second, step_number
    if step_number % 2 == 1:
        info_first, step_number = step(info_first, info_second, step_number, self)
    elif step_number % 2 == 0:
        info_second, step_number = step(info_second, info_first, step_number, self)


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
info_first = {'flag': flag_first,
              'fence_click': fence_first,
              'fence_number': fence_number_first,
              'picture': picture_button_first,
              'text': text_first}
info_second = {'flag': flag_second,
               'fence_click': fence_second,
               'fence_number': fence_number_second,
               'picture': picture_button_second,
               'text': text_second}


Label(root, image=picture_background).pack()
cells = [[None for i in range(TABLE_WIDTH)] for j in range(TABLE_LENGTH)]
fences_horizontal = [[None for i in range(TABLE_WIDTH + 1)] for j in range(TABLE_LENGTH)]
fences_vertical = [[None for i in range(TABLE_WIDTH)] for j in range(TABLE_LENGTH + 1)]
for i in range(TABLE_LENGTH):
    for j in range(TABLE_WIDTH):
        picture = picture_button_default
        if i == X1 and j == Y1:
            picture = picture_button_first
        if i == X2 and j == Y2:
            picture = picture_button_second
        cells[i][j] = Button(root,
                              bg=colour_default,
                              image=picture,
                              text=NAME_CELL+str(i)+str(j))
        cells[i][j].place(x=470+(CELL_WIDTH+FENCE_WIDTH)*i,
                           y=120+(CELL_LENGTH+FENCE_WIDTH)*j,
                           width=CELL_WIDTH,
                           height=CELL_LENGTH)
for i in range(TABLE_LENGTH):
    for j in range(TABLE_WIDTH + 1):
        picture = picture_fence_horizontal_default
        name = NAME_HORIZONTAL
        if j == 0 or j == TABLE_WIDTH:
            picture = picture_fence_horizontal
            name = NAME_FENCE
        fences_horizontal[i][j] = Button(root,
                                         bg=colour_default,
                                         image=picture,
                                         text=name+str(i)+str(j))
        fences_horizontal[i][j].place(x=470+(CELL_WIDTH+FENCE_WIDTH)*i,
                                      y=105+(CELL_LENGTH+FENCE_WIDTH)*j,
                                      width=FENCE_LENGTH,
                                      height=FENCE_WIDTH)
for i in range(TABLE_LENGTH + 1):
    for j in range(TABLE_WIDTH):
        picture = picture_fence_vertical_default
        name = NAME_VERTICAL
        if i == 0 or i == TABLE_LENGTH:
            picture = picture_fence_vertical
            name = NAME_FENCE
        fences_vertical[i][j] = Button(root,
                                       bg=colour_default,
                                       image=picture,
                                       text=name+str(i)+str(j))
        fences_vertical[i][j].place(x=455+(CELL_WIDTH+FENCE_WIDTH)*i,
                                    y=120+(CELL_LENGTH+FENCE_WIDTH)*j,
                                    width=FENCE_WIDTH,
                                    height=FENCE_LENGTH)


can.pack()
root.bind_class('Button', '<1>', button_click)
root.mainloop()
