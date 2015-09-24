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

figure_white = Figure(4, 0)
figure_black = Figure(4, 8)
step_number = 1
while True:
    if step_number % 2 == 1:
        print('1 - move a figure, 2 - put a fance')
        step = int(input())
        if step == 1:
            print('1 - right, 2 - up, 3 - left, 4 - down')
            direction = int(input())
            figure_white.move(direction)
            print('white', figure_white.x, figure_white.y)
    if step_number % 2 == 0:
        print('1 - move a figure, 2 - put a fance')
        step = int(input())
        if step == 1:
            print('1 - right, 2 - up, 3 - left, 4 - down')
            direction = int(input())
            figure_black.move(direction)
            print('black', figure_black.x, figure_black.y)
    step_number += 1
