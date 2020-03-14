import pygame
import random

pygame.init()

screen_size = (200, 400)
playing_field = (200, 400)
# shapes = ("S - shape", "Z - shape", "T - shape", "L - shape",
#           "Line - shape", "MirroredL - shape", "Square - shape")

shapes = ("L shape", "Square", "Line", "L shape reversed", "T shape")

SHADOW = (192, 192, 192)

WHITE = (255, 255, 255)

LIGHTGREEN = (0, 255, 0 )

GREEN = (0, 200, 0 )

BLUE = (0, 0, 128)

LIGHTBLUE= (0, 0, 255)

RED= (200, 0, 0 )

LIGHTRED= (255, 100, 100)

PURPLE = (102, 0, 102)

LIGHTPURPLE= (153, 0, 153)

YELLOW = (250, 250, 0)


full_line_1 = [[0, 380, 20, 20], [20, 380, 20, 20], [40, 380, 20, 20], [60, 380, 20, 20], [80, 380, 20, 20], [100, 380, 20, 20], [120, 380, 20, 20], [140, 380, 20, 20], [160, 380, 20, 20], [180, 380, 20, 20]]
full_line_2 = [[0, 360, 20, 20], [20, 360, 20, 20], [40, 360, 20, 20], [60, 360, 20, 20], [80, 360, 20, 20], [100, 360, 20, 20], [120, 360, 20, 20], [140, 360, 20, 20], [160, 360, 20, 20], [180, 360, 20, 20]]
full_line_3 = [[0, 340, 20, 20], [20, 340, 20, 20], [40, 340, 20, 20], [60, 340, 20, 20], [80, 340, 20, 20], [100, 340, 20, 20], [120, 340, 20, 20], [140, 340, 20, 20], [160, 340, 20, 20], [180, 340, 20, 20]]
full_line_4 = [[0, 320, 20, 20], [20, 320, 20, 20], [40, 320, 20, 20], [60, 320, 20, 20], [80, 320, 20, 20], [100, 320, 20, 20], [120, 320, 20, 20], [140, 320, 20, 20], [160, 320, 20, 20], [180, 320, 20, 20]]
full_line_5 = [[0, 300, 20, 20], [20, 300, 20, 20], [40, 300, 20, 20], [60, 300, 20, 20], [80, 300, 20, 20], [100, 300, 20, 20], [120, 300, 20, 20], [140, 300, 20, 20], [160, 300, 20, 20], [180, 300, 20, 20]]
full_line_6 = [[0, 280, 20, 20], [20, 280, 20, 20], [40, 280, 20, 20], [60, 280, 20, 20], [80, 280, 20, 20], [100, 280, 20, 20], [120, 280, 20, 20], [140, 280, 20, 20], [160, 280, 20, 20], [180, 280, 20, 20]]
full_line_7 = [[0, 260, 20, 20], [20, 260, 20, 20], [40, 260, 20, 20], [60, 260, 20, 20], [80, 260, 20, 20], [100, 260, 20, 20], [120, 260, 20, 20], [140, 260, 20, 20], [160, 260, 20, 20], [180, 260, 20, 20]]
full_line_8 = [[0, 240, 20, 20], [20, 240, 20, 20], [40, 240, 20, 20], [60, 240, 20, 20], [80, 240, 20, 20], [100, 240, 20, 20], [120, 240, 20, 20], [140, 240, 20, 20], [160, 240, 20, 20], [180, 240, 20, 20]]
full_line_9 = [[0, 220, 20, 20], [20, 220, 20, 20], [40, 220, 20, 20], [60, 220, 20, 20], [80, 220, 20, 20], [100, 220, 20, 20], [120, 220, 20, 20], [140, 220, 20, 20], [160, 220, 20, 20], [180, 220, 20, 20]]
full_line_10 = [[0, 200, 20, 20], [20, 200, 20, 20], [40, 200, 20, 20], [60, 200, 20, 20], [80, 200, 20, 20], [100, 200, 20, 20], [120, 200, 20, 20], [140, 200, 20, 20], [160, 200, 20, 20], [180, 200, 20, 20]]
full_line_11 = [[0, 180, 20, 20], [20, 180, 20, 20], [40, 180, 20, 20], [60, 180, 20, 20], [80, 180, 20, 20], [100, 180, 20, 20], [120, 180, 20, 20], [140, 180, 20, 20], [160, 180, 20, 20], [180, 180, 20, 20]]
full_line_12 = [[0, 160, 20, 20], [20, 160, 20, 20], [40, 160, 20, 20], [60, 160, 20, 20], [80, 160, 20, 20], [100, 160, 20, 20], [120, 160, 20, 20], [140, 160, 20, 20], [160, 160, 20, 20], [180, 160, 20, 20]]
full_line_13 = [[0, 140, 20, 20], [20, 140, 20, 20], [40, 140, 20, 20], [60, 140, 20, 20], [80, 140, 20, 20], [100, 140, 20, 20], [120, 140, 20, 20], [140, 140, 20, 20], [160, 140, 20, 20], [180, 140, 20, 20]]
full_line_14 = [[0, 120, 20, 20], [20, 120, 20, 20], [40, 120, 20, 20], [60, 120, 20, 20], [80, 120, 20, 20], [100, 120, 20, 20], [120, 120, 20, 20], [140, 120, 20, 20], [160, 120, 20, 20], [180, 120, 20, 20]]
full_line_15 = [[0, 100, 20, 20], [20, 100, 20, 20], [40, 100, 20, 20], [60, 100, 20, 20], [80, 100, 20, 20], [100, 100, 20, 20], [120, 100, 20, 20], [140, 100, 20, 20], [160, 100, 20, 20], [180, 100, 20, 20]]
full_line_16 = [[0, 80, 20, 20], [20, 80, 20, 20], [40, 80, 20, 20], [60, 80, 20, 20], [80, 80, 20, 20], [100, 80, 20, 20], [120, 80, 20, 20], [140, 80, 20, 20], [160, 80, 20, 20], [180, 80, 20, 20]]
full_line_17 = [[0, 60, 20, 20], [20, 60, 20, 20], [40, 60, 20, 20], [60, 60, 20, 20], [80, 60, 20, 20], [100, 60, 20, 20], [120, 60, 20, 20], [140, 60, 20, 20], [160, 60, 20, 20], [180, 60, 20, 20]]
full_line_18 = [[0, 40, 20, 20], [20, 40, 20, 20], [40, 40, 20, 20], [60, 40, 20, 20], [80, 40, 20, 20], [100, 40, 20, 20], [120, 40, 20, 20], [140, 40, 20, 20], [160, 40, 20, 20], [180, 40, 20, 20]]
full_line_19 = [[0, 20, 20, 20], [20, 20, 20, 20], [40, 20, 20, 20], [60, 20, 20, 20], [80, 20, 20, 20], [100, 20, 20, 20], [120, 20, 20, 20], [140, 20, 20, 20], [160, 20, 20, 20], [180, 20, 20, 20]]
full_line_20 = [[0, 0, 20, 20], [20, 0, 20, 20], [40, 0, 20, 20], [60, 0, 20, 20], [80, 0, 20, 20], [100, 0, 20, 20], [120, 0, 20, 20], [140, 0, 20, 20], [160, 0, 20, 20], [180, 0, 20, 20]]

full_line_list = [full_line_1, full_line_2, full_line_3, full_line_4, full_line_5, full_line_6, full_line_7, full_line_8, full_line_9, full_line_10, full_line_11, full_line_12, full_line_13, full_line_14, full_line_15, full_line_16, full_line_17, full_line_18, full_line_19, full_line_20]


screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Tetris")

run = True

clock = pygame.time.Clock()
existing_pieces = []

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


class Square(object):
    def __init__(self, tl, tr, bl, br):

        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.bl)
        pygame.draw.rect(screen, RED, self.br)
        pygame.draw.rect(screen, RED, self.tl)
        pygame.draw.rect(screen, RED, self.tr)

class Line(object):
    def __init__(self, one, two, three, four, facing):

        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.facing = facing

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.one)
        pygame.draw.rect(screen, WHITE, self.two)
        pygame.draw.rect(screen, WHITE, self.three)
        pygame.draw.rect(screen, WHITE, self.four)

class L_shape(object):
    def __init__(self, one, two, three, tail, facing):

        self.one = one
        self.two = two
        self.three = three
        self.tail = tail
        self.facing = facing

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.one)
        pygame.draw.rect(screen, YELLOW, self.two)
        pygame.draw.rect(screen, YELLOW, self.three)
        pygame.draw.rect(screen, YELLOW, self.tail)

class L_shape_rev(object):
    def __init__(self, one, two, three, tail, facing):

        self.one = one
        self.two = two
        self.three = three
        self.tail = tail
        self.facing = facing

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.one)
        pygame.draw.rect(screen, YELLOW, self.two)
        pygame.draw.rect(screen, YELLOW, self.three)
        pygame.draw.rect(screen, YELLOW, self.tail)

class T_shape(object):
    def __init__(self, one, two, three, tail, facing):

        self.one = one
        self.two = two
        self.three = three
        self.tail = tail
        self.facing = facing

    def draw(self, screen):
        pygame.draw.rect(screen, PURPLE, self.one)
        pygame.draw.rect(screen, PURPLE, self.two)
        pygame.draw.rect(screen, PURPLE, self.three)
        pygame.draw.rect(screen, PURPLE, self.tail)

def redraw_game_window():
    screen.fill((0, 0, 0))

    square.draw(screen)
    line.draw(screen)
    l_shape.draw(screen)
    l_shape_rev.draw(screen)
    t_shape.draw(screen)

    for item in existing_pieces:
        pygame.draw.rect(screen, SHADOW, item)

    pygame.display.update()


def generate_new_piece():
    new_piece = random.choice(shapes)
    return new_piece



time_speed = 5

one_step = 20

def get_new_line():
    line = Line([60, -20, 20, 20], [80, -20, 20, 20], [100, -20, 20, 20], [120, -20, 20, 20], "horizontal")
    return line

def get_new_square():
    square = Square([80, -40, 20, 20], [100, -40, 20, 20],
                [80, -20, 20, 20], [100, -20, 20, 20])
    return square

def get_new_l_shape():
    l_shape = L_shape([60, -20, 20, 20], [80, -20, 20, 20], [100, -20, 20, 20], [100, -40, 20, 20], "horizontal_up")
    return l_shape

def get_new_l_shape_rev():
    l_shape_rev = L_shape_rev([100, -20, 20, 20], [80, -20, 20, 20], [60, -20, 20, 20], [60, -40, 20, 20], "horizontal_up")
    return l_shape_rev

def get_new_t_shape():
    t_shape = T_shape([60, -20, 20, 20], [80, -20, 20, 20], [100, -20, 20, 20], [80, -40, 20, 20], "horizontal_up")
    return t_shape

t_shape = get_new_t_shape()
l_shape_rev = get_new_l_shape_rev()
l_shape = get_new_l_shape()
line = get_new_line()
square = get_new_square()
new_piece = generate_new_piece()
while run:
    keys = pygame.key.get_pressed()
    clock.tick(time_speed)

    new_piece = "T shape"

    if new_piece == "Square":

        index = 0
        for item in existing_pieces:
            if square.bl[1] + one_step == item[1]  and square.bl[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(square.bl)
                existing_pieces.append(square.br)
                existing_pieces.append(square.tl)
                existing_pieces.append(square.tr)
                square = get_new_square()
                index = 1
                break
            elif square.br[1] + one_step == item[1] and square.br[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(square.bl)
                existing_pieces.append(square.br)
                existing_pieces.append(square.tl)
                existing_pieces.append(square.tr)
                square = get_new_square()
                index = 1
                break
            # check down left
            elif item[0] == square.bl[0] - one_step and item[1] == square.bl[1] + one_step:
                index = 3
            # check down right
            elif item[0] == square.br[0] + one_step and item[1] == square.br[1] + one_step:
                index = 4
        if index != 1:
            if square.bl[1] < screen_size[1] - square.bl[2]:
                square.bl[1] += one_step
                square.br[1] += one_step
                square.tl[1] += one_step
                square.tr[1] += one_step
            elif square.bl[1] == screen_size[1] - square.bl[2]:
                new_piece = generate_new_piece()
                existing_pieces.append(square.bl)
                existing_pieces.append(square.br)
                existing_pieces.append(square.tl)
                existing_pieces.append(square.tr)


                square = get_new_square()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and square.bl[1] < screen_size[1] - square.bl[2] and square.bl[0] > 0 and index != 3:
                    square.bl[0] -= one_step
                    square.br[0] -= one_step
                    square.tl[0] -= one_step
                    square.tr[0] -= one_step

                if event.key == pygame.K_RIGHT and square.bl[1] < screen_size[1] - square.bl[2] and square.br[0] < screen_size[0] - one_step and index != 4:
                    square.bl[0] += one_step
                    square.br[0] += one_step
                    square.tl[0] += one_step
                    square.tr[0] += one_step

    elif new_piece == "Line":
        index = 0
        for item in existing_pieces:
            if line.one[1] + one_step == item[1]  and line.one[0] == item[0]:

                new_piece = generate_new_piece()
                existing_pieces.append(line.one)
                existing_pieces.append(line.two)
                existing_pieces.append(line.three)
                existing_pieces.append(line.four)

                line = get_new_line()
                index = 1
                break
            elif line.four[1] + one_step == item[1] and line.four[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(line.one)
                existing_pieces.append(line.two)
                existing_pieces.append(line.three)
                existing_pieces.append(line.four)

                line = get_new_line()
                index = 1
                break
            elif line.three[1] + one_step == item[1] and line.three[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(line.one)
                existing_pieces.append(line.two)
                existing_pieces.append(line.three)
                existing_pieces.append(line.four)
                index = 1
                line = get_new_line()
                break
            elif line.two[1] + one_step == item[1] and line.two[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(line.one)
                existing_pieces.append(line.two)
                existing_pieces.append(line.three)
                existing_pieces.append(line.four)

                line = get_new_line()
                index = 1
                break
            # check to the down left
            elif item[0] == line.one[0] - one_step and item[1] == line.one[1] + one_step:
                index = 2
            # check to the down right
            elif item[0] == line.one[0] + one_step and item[1] == line.one[1] + one_step:
                index = 3
            elif item[0] == line.four[0] + one_step and item[1] == line.four[1] + one_step:
                index = 3
            # check if can rotate on the left side
            elif item[0] == line.two[0] - one_step and item[1] == line.two[1]:
                index = 4
            # check if can rotate on the right side
            elif item[0] == line.two[0] + one_step and item[1] == line.two[1]:
                index = 4
            elif item[0] == line.two[0] + one_step * 2 and item[1] == line.two[1]:
                index = 4

        if index != 1:
            if line.facing == "horizontal":
                if line.one[1] < screen_size[1] - line.one[3] or line.four[1] < screen_size[1] - line.one[3]:
                    line.one[1] += one_step
                    line.two[1] += one_step
                    line.three[1] += one_step
                    line.four[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(line.one)
                    existing_pieces.append(line.two)
                    existing_pieces.append(line.three)
                    existing_pieces.append(line.four)

                    line = get_new_line()
            if line.facing == "vertical":
                if line.one[1] < screen_size[1] - line.one[3]:
                    line.one[1] += one_step
                    line.two[1] += one_step
                    line.three[1] += one_step
                    line.four[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(line.one)
                    existing_pieces.append(line.two)
                    existing_pieces.append(line.three)
                    existing_pieces.append(line.four)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and line.one[1] < screen_size[1] - line.one[2] and line.one[0] > 0 and index != 2:
                    line.one[0] -= one_step
                    line.two[0] -= one_step
                    line.three[0] -= one_step
                    line.four[0] -= one_step

                if event.key == pygame.K_RIGHT and line.four[1] < screen_size[1] - line.four[2] and line.four[0] < screen_size[0] - one_step and index != 3:
                    line.one[0] += one_step
                    line.two[0] += one_step
                    line.three[0] += one_step
                    line.four[0] += one_step

                if event.key == pygame.K_SPACE and line.facing == "horizontal":

                        line.facing = "vertical"
                        line.one[0] = line.two[0]
                        line.one[1] = line.two[1]
                        line.two[1] -= one_step
                        line.three[1] -= one_step*2
                        line.four[1]-= one_step*3
                        line.three[0] -= one_step
                        line.four[0] -= one_step*2

                elif event.key == pygame.K_SPACE and line.facing ==  "vertical" and line.one[0] < screen_size[0] - one_step*2 and line.one[0] > one_step*2 and index !=4 and index != 2 and index != 3:

                        line.facing = "horizontal"
                        line.one[0] -= one_step
                        line.one[1] -= one_step
                        line.three[0] += one_step
                        line.three[1] += one_step
                        line.four[0] += one_step*2
                        line.four[1] += one_step*2

    elif new_piece == "L shape":

        no_left = False
        no_right = False
        no_down = False
        no_rotate = False

        for item in existing_pieces:
            if l_shape.one[1] + one_step == item[1]  and l_shape.one[0] == item[0]:

                new_piece = generate_new_piece()
                existing_pieces.append(l_shape.one)
                existing_pieces.append(l_shape.two)
                existing_pieces.append(l_shape.three)
                existing_pieces.append(l_shape.tail)

                l_shape = get_new_l_shape()
                no_down = True
                break
            elif l_shape.tail[1] + one_step == item[1] and l_shape.tail[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(l_shape.one)
                existing_pieces.append(l_shape.two)
                existing_pieces.append(l_shape.three)
                existing_pieces.append(l_shape.tail)

                l_shape = get_new_l_shape()
                no_down = True
                break
            elif l_shape.three[1] + one_step == item[1] and l_shape.three[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(l_shape.one)
                existing_pieces.append(l_shape.two)
                existing_pieces.append(l_shape.three)
                existing_pieces.append(l_shape.tail)

                l_shape = get_new_l_shape()
                no_down = True
                break
            elif l_shape.two[1] + one_step == item[1] and l_shape.two[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(l_shape.one)
                existing_pieces.append(l_shape.two)
                existing_pieces.append(l_shape.three)
                existing_pieces.append(l_shape.tail)

                l_shape = get_new_l_shape()
                no_down = True
                break
            if l_shape.facing == "horizontal_up" or l_shape.facing == "vertical_left":
                # check to the down left
                if item[0] == l_shape.one[0] - one_step and item[1] == l_shape.one[1] + one_step:
                    no_left = True
                # check to the down right
                elif l_shape.facing == "vertical_left" and item[0] == l_shape.one[0] + one_step and item[1] == l_shape.one[1] + one_step:
                    no_right = True
                elif l_shape.facing == "horizontal_up" and item[0] == l_shape.three[0] + one_step and item[1] == l_shape.three[1] + one_step:
                    no_right = True

            # check for obstruction bottom left and right
            elif l_shape.facing == "horizontal_down" or l_shape.facing == "vertical_right":
                # check to the down left
                if l_shape.facing == "vertical_right" and item[0] == l_shape.three[0] - one_step and item[1] == l_shape.three[1] + one_step:
                    no_left = True
                elif l_shape.facing == "horizontal_down" and item[0] == l_shape.tail[0] - one_step and item[1] == l_shape.tail[1] + one_step:
                    no_left = True
                # check to the down right
                elif item[0] == l_shape.tail[0] + one_step and item[1] == l_shape.tail[1] + one_step:
                    no_right = True

            # check for obstructions to rotate
            if l_shape.facing == "vertical_right":
                if item[0] == l_shape.one[0] + one_step and item[1] == l_shape.one[1] + one_step:
                    no_rotate = True
                elif item[0] == l_shape.one[0] + one_step*2 and item[1] == l_shape.one[1] + one_step:
                    no_rotate = True
            elif l_shape.facing == "horizontal_down":
                if item[0] == l_shape.one[0] and item[1] == l_shape.one[1] + one_step * 3:
                    no_rotate = True
                elif item[0] == l_shape.one[0] and item[1] == l_shape.one[1] + one_step*2:
                    no_rotate = True
            elif l_shape.facing == "vertical_left":
                if item[0] == l_shape.two[0] - one_step and item[1] == l_shape.two[1] + one_step:
                    no_rotate = True
                elif item[0] == l_shape.two[0] - one_step*2 and item[1] == l_shape.two[1] + one_step:
                    no_rotate = True
            elif l_shape.facing == "horizontal_up":
                if item[0] == l_shape.one[0] and item[1] == l_shape.one[1]:
                    no_rotate = True
                elif item[0] == l_shape.one[0] and item[1] == l_shape.one[1] + one_step*2:
                    no_rotate = True
                elif item[0] == l_shape.two[0] and item[1] == l_shape.two[1] + one_step*2:
                    no_rotate = True


        if no_down == False:
            if l_shape.facing == "horizontal_up" or l_shape.facing == "vertical_left":
                if l_shape.one[1] < screen_size[1] - l_shape.one[3]:
                    l_shape.one[1] += one_step
                    l_shape.two[1] += one_step
                    l_shape.three[1] += one_step
                    l_shape.tail[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(l_shape.one)
                    existing_pieces.append(l_shape.two)
                    existing_pieces.append(l_shape.three)
                    existing_pieces.append(l_shape.tail)

                    l_shape = get_new_l_shape()
            elif l_shape.facing == "horizontal_down" or l_shape.facing == "vertical_right":
                if l_shape.tail[1] < screen_size[1] - l_shape.tail[3]:
                    l_shape.one[1] += one_step
                    l_shape.two[1] += one_step
                    l_shape.three[1] += one_step
                    l_shape.tail[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(l_shape.one)
                    existing_pieces.append(l_shape.two)
                    existing_pieces.append(l_shape.three)
                    existing_pieces.append(l_shape.tail)

                    l_shape = get_new_l_shape()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and l_shape.one[1] < screen_size[1] - l_shape.one[2] and l_shape.one[0] > 0 and l_shape.tail[0] > 0 and no_left == False :
                    l_shape.one[0] -= one_step
                    l_shape.two[0] -= one_step
                    l_shape.three[0] -= one_step
                    l_shape.tail[0] -= one_step

                if event.key == pygame.K_RIGHT and l_shape.tail[1] < screen_size[1] - l_shape.tail[2] and l_shape.tail[0] < screen_size[0] - one_step and l_shape.one[0] < screen_size[0] - one_step and no_right == False:
                    l_shape.one[0] += one_step
                    l_shape.two[0] += one_step
                    l_shape.three[0] += one_step
                    l_shape.tail[0] += one_step

                if event.key == pygame.K_SPACE and l_shape.facing == "horizontal_up" and no_rotate == False:

                        l_shape.facing = "vertical_right"
                        l_shape.one[1] -= one_step
                        l_shape.two[0] -= one_step
                        l_shape.three[0] -= one_step*2
                        l_shape.three[1] += one_step
                        l_shape.tail[0] -= one_step
                        l_shape.tail[1] += one_step*2

                elif event.key == pygame.K_SPACE and l_shape.facing ==  "vertical_left" and l_shape.tail[0] > one_step and no_rotate == False:

                        l_shape.facing = "horizontal_up"
                        l_shape.one[0] -= one_step*2
                        l_shape.one[1] -= one_step
                        l_shape.two[0] -= one_step
                        l_shape.three[1] += one_step
                        l_shape.tail[0] += one_step

                elif event.key == pygame.K_SPACE and l_shape.facing == "horizontal_down" and no_rotate == False:

                        l_shape.facing = "vertical_left"
                        l_shape.one[1] += one_step*2
                        l_shape.two[0] += one_step
                        l_shape.two[1] += one_step
                        l_shape.three[0] += one_step*2
                        l_shape.tail[0] += one_step
                        l_shape.tail[1] -= one_step

                elif event.key == pygame.K_SPACE and l_shape.facing ==  "vertical_right" and l_shape.tail[0] < screen_size[0] - one_step and no_rotate == False:

                        l_shape.facing = "horizontal_down"
                        l_shape.one[0] += one_step*2
                        l_shape.two[0] += one_step
                        l_shape.two[1] -= one_step
                        l_shape.three[1] -= one_step*2
                        l_shape.tail[0] -= one_step
                        l_shape.tail[1] -= one_step

    elif new_piece == "L shape reversed":

        no_left = False
        no_right = False
        no_down = False
        no_rotate = False
        for item in existing_pieces:
            if l_shape_rev.one[1] + one_step == item[1]  and l_shape_rev.one[0] == item[0]:

                new_piece = generate_new_piece()
                existing_pieces.append(l_shape_rev.one)
                existing_pieces.append(l_shape_rev.two)
                existing_pieces.append(l_shape_rev.three)
                existing_pieces.append(l_shape_rev.tail)

                l_shape_rev = get_new_l_shape_rev()
                no_down = True
                break
            elif l_shape_rev.tail[1] + one_step == item[1] and l_shape_rev.tail[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(l_shape_rev.one)
                existing_pieces.append(l_shape_rev.two)
                existing_pieces.append(l_shape_rev.three)
                existing_pieces.append(l_shape_rev.tail)

                l_shape_rev = get_new_l_shape_rev()
                no_down = True
                break
            elif l_shape_rev.three[1] + one_step == item[1] and l_shape_rev.three[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(l_shape_rev.one)
                existing_pieces.append(l_shape_rev.two)
                existing_pieces.append(l_shape_rev.three)
                existing_pieces.append(l_shape_rev.tail)

                l_shape_rev = get_new_l_shape_rev()
                no_down = True
                break
            elif l_shape_rev.two[1] + one_step == item[1] and l_shape_rev.two[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(l_shape_rev.one)
                existing_pieces.append(l_shape_rev.two)
                existing_pieces.append(l_shape_rev.three)
                existing_pieces.append(l_shape_rev.tail)

                l_shape_rev = get_new_l_shape_rev()
                no_down = True
                break

            if l_shape_rev.facing == "horizontal_up" or l_shape_rev.facing == "vertical_right":
                # check to the down left
                if l_shape_rev.facing == "horizontal_up" and item[0] == l_shape_rev.three[0] - one_step and item[1] == l_shape_rev.three[1] + one_step:
                    no_left = True
                elif l_shape_rev.facing == "vertical_right" and item[0] == l_shape_rev.one[0] - one_step and item[1] == l_shape_rev.one[1] + one_step:
                    no_left = True
                # check to the down right
                elif item[0] == l_shape_rev.one[0] + one_step and item[1] == l_shape_rev.one[1] + one_step:
                    no_right = True

            # check for obstruction bottom left and right
            elif l_shape_rev.facing == "horizontal_down" or l_shape_rev.facing == "vertical_left":
                # check to the down left
                if item[0] == l_shape_rev.tail[0] - one_step and item[1] == l_shape_rev.tail[1] + one_step:
                    no_left = True
                # check to the down right
                elif l_shape_rev.facing == "horizontal_down" and item[0] == l_shape_rev.tail[0] + one_step and item[1] == l_shape_rev.tail[1] + one_step:
                    no_right = True
                elif l_shape_rev.facing == "vertical_left" and item[0] == l_shape_rev.three[0] + one_step and item[1] == l_shape_rev.three[1] + one_step:
                    no_right = True

            # check for obstructions to rotate
            if l_shape_rev.facing == "vertical_right":
                if item[0] == l_shape_rev.tail[0] + one_step and item[1] == l_shape_rev.tail[1] + one_step:
                    no_rotate = True
                elif item[0] == l_shape_rev.tail[0] + one_step and item[1] == l_shape_rev.tail[1] + one_step*2:
                    no_rotate = True
            elif l_shape_rev.facing == "horizontal_down":
                if item[0] == l_shape_rev.tail[0] - one_step and item[1] == l_shape_rev.tail[1] + one_step*2:
                    no_rotate = True
                elif item[0] == l_shape_rev.tail[0] and item[1] == l_shape_rev.tail[1] + one_step*2:
                    no_rotate = True
            elif l_shape_rev.facing == "vertical_left":
                if item[0] == l_shape_rev.tail[0] - one_step and item[1] == l_shape_rev.tail[1] - one_step:
                    no_rotate = True
                elif item[0] == l_shape_rev.tail[0] - one_step and item[1] == l_shape_rev.tail[1]:
                    no_rotate = True
                elif item[0] == l_shape_rev.tail[0] and item[1] == l_shape_rev.tail[1]:
                    no_rotate = True
            elif l_shape_rev.facing == "horizontal_up":
                if item[0] == l_shape_rev.tail[0] + one_step and item[1] == l_shape_rev.tail[1] + one_step:
                    no_rotate = True
                elif item[0] == l_shape_rev.three[0] and item[1] == l_shape_rev.three[1] + one_step*2:
                    no_rotate = True

        if no_down == False:
            if l_shape_rev.facing == "horizontal_up" or l_shape_rev.facing == "vertical_right":
                if l_shape_rev.one[1] < screen_size[1] - l_shape_rev.one[3]:
                    l_shape_rev.one[1] += one_step
                    l_shape_rev.two[1] += one_step
                    l_shape_rev.three[1] += one_step
                    l_shape_rev.tail[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(l_shape_rev.one)
                    existing_pieces.append(l_shape_rev.two)
                    existing_pieces.append(l_shape_rev.three)
                    existing_pieces.append(l_shape_rev.tail)

                    l_shape_rev = get_new_l_shape_rev()
            elif l_shape_rev.facing == "horizontal_down" or l_shape_rev.facing == "vertical_left":
                if l_shape_rev.tail[1] < screen_size[1] - l_shape_rev.tail[3]:
                    l_shape_rev.one[1] += one_step
                    l_shape_rev.two[1] += one_step
                    l_shape_rev.three[1] += one_step
                    l_shape_rev.tail[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(l_shape_rev.one)
                    existing_pieces.append(l_shape_rev.two)
                    existing_pieces.append(l_shape_rev.three)
                    existing_pieces.append(l_shape_rev.tail)

                    l_shape_rev = get_new_l_shape_rev()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and l_shape_rev.one[1] < screen_size[1] - l_shape_rev.one[2] and l_shape_rev.one[0] > 0 and l_shape_rev.tail[0] > 0 and no_left == False:
                    l_shape_rev.one[0] -= one_step
                    l_shape_rev.two[0] -= one_step
                    l_shape_rev.three[0] -= one_step
                    l_shape_rev.tail[0] -= one_step

                if event.key == pygame.K_RIGHT and l_shape_rev.tail[1] < screen_size[1] - l_shape_rev.tail[2] and l_shape_rev.tail[0] < screen_size[0] - one_step and l_shape_rev.one[0] < screen_size[0] - one_step and no_right == False:
                    l_shape_rev.one[0] += one_step
                    l_shape_rev.two[0] += one_step
                    l_shape_rev.three[0] += one_step
                    l_shape_rev.tail[0] += one_step

                if event.key == pygame.K_SPACE and l_shape_rev.facing == "horizontal_up" and l_shape_rev.one[1] < screen_size[1] - one_step and no_rotate == False:

                        l_shape_rev.facing = "vertical_right"
                        l_shape_rev.one[0] -= one_step*2
                        l_shape_rev.one[1] += one_step
                        l_shape_rev.two[0] -= one_step
                        l_shape_rev.three[1] -= one_step
                        l_shape_rev.tail[0] += one_step

                elif event.key == pygame.K_SPACE and l_shape_rev.facing ==  "vertical_left" and l_shape_rev.tail[0] and no_rotate == False:

                        l_shape_rev.facing = "horizontal_up"
                        l_shape_rev.one[1] += one_step
                        l_shape_rev.two[0] -= one_step
                        l_shape_rev.three[0] -= one_step*2
                        l_shape_rev.three[1] -= one_step
                        l_shape_rev.tail[0] -= one_step
                        l_shape_rev.tail[1] -= one_step*2
                elif event.key == pygame.K_SPACE and l_shape_rev.facing == "horizontal_down" and l_shape_rev.tail[1] < screen_size[1] - one_step and no_rotate == False:

                        l_shape_rev.facing = "vertical_left"
                        l_shape_rev.one[0] += one_step*2
                        l_shape_rev.two[0] += one_step
                        l_shape_rev.two[1] += one_step
                        l_shape_rev.three[1] += one_step*2
                        l_shape_rev.tail[0] -= one_step
                        l_shape_rev.tail[1] += one_step

                elif event.key == pygame.K_SPACE and l_shape_rev.facing ==  "vertical_right" and l_shape_rev.tail[0] < screen_size[0] - one_step and no_rotate == False:

                        l_shape_rev.facing = "horizontal_down"
                        l_shape_rev.one[1] -= one_step*2
                        l_shape_rev.two[0] += one_step
                        l_shape_rev.two[1] -= one_step
                        l_shape_rev.three[0] += one_step*2
                        l_shape_rev.tail[0] += one_step
                        l_shape_rev.tail[1] += one_step

    elif new_piece == "T shape":

        no_left = False
        no_right = False
        no_down = False
        no_rotate = False

        for item in existing_pieces:
            if t_shape.one[1] + one_step == item[1]  and t_shape.one[0] == item[0]:

                new_piece = generate_new_piece()
                existing_pieces.append(t_shape.one)
                existing_pieces.append(t_shape.two)
                existing_pieces.append(t_shape.three)
                existing_pieces.append(t_shape.tail)

                t_shape = get_new_t_shape()
                no_down = True
                break
            elif t_shape.tail[1] + one_step == item[1] and t_shape.tail[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(t_shape.one)
                existing_pieces.append(t_shape.two)
                existing_pieces.append(t_shape.three)
                existing_pieces.append(t_shape.tail)

                t_shape = get_new_t_shape()
                no_down = True
                break
            elif t_shape.three[1] + one_step == item[1] and t_shape.three[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(t_shape.one)
                existing_pieces.append(t_shape.two)
                existing_pieces.append(t_shape.three)
                existing_pieces.append(t_shape.tail)

                t_shape = get_new_t_shape()
                no_down = True
                break
            elif t_shape.two[1] + one_step == item[1] and t_shape.two[0] == item[0]:
                new_piece = generate_new_piece()
                existing_pieces.append(t_shape.one)
                existing_pieces.append(t_shape.two)
                existing_pieces.append(t_shape.three)
                existing_pieces.append(t_shape.tail)

                t_shape = get_new_t_shape()
                no_down = True
                break
            if t_shape.facing == "horizontal_up" or t_shape.facing == "vertical_left":
                # check to the down left
                if item[0] == t_shape.one[0] - one_step and item[1] == t_shape.one[1] + one_step:
                    no_left = True
                elif t_shape.facing == "vertical_left" and item[0] == t_shape.tail[0] - one_step and item[1] == t_shape.tail[1] + one_step:
                    no_left = True
                # check to the down right
                elif t_shape.facing == "vertical_left" and item[0] == t_shape.one[0] + one_step and item[1] == t_shape.one[1] + one_step:
                    no_right = True
                elif t_shape.facing == "horizontal_up" and item[0] == t_shape.three[0] + one_step and item[1] == t_shape.three[1] + one_step:
                    no_right = True

            # check for obstruction bottom left and right
            elif t_shape.facing == "horizontal_down" or t_shape.facing == "vertical_right":
                # check to the down left
                if item[0] == t_shape.three[0] - one_step and item[1] == t_shape.three[1] + one_step:
                    no_left = True
                elif t_shape.facing == "horizontal_down" and item[0] == t_shape.tail[0] - one_step and item[1] == t_shape.tail[1] + one_step:
                    no_left = True
                # check to the down right
                elif item[0] == t_shape.tail[0] + one_step and item[1] == t_shape.tail[1] + one_step:
                    no_right = True
                elif t_shape.facing == "vertical_right" and item[0] == t_shape.three[0] + one_step and item[1] == t_shape.three[1] + one_step:
                    no_right = True
                elif t_shape.facing == "horizontal_down" and item[0] == t_shape.one[0] + one_step and item[1] == t_shape.one[1] + one_step:
                    no_right = True

            # check for obstructions to rotate
            if t_shape.facing == "vertical_right":
                if item[0] == t_shape.one[0] + one_step and item[1] == t_shape.one[1] + one_step:
                    no_rotate = True
                elif item[0] == t_shape.one[0] + one_step*2 and item[1] == t_shape.one[1] + one_step:
                    no_rotate = True
            elif t_shape.facing == "horizontal_down":
                if item[0] == t_shape.one[0] and item[1] == t_shape.one[1] + one_step * 3:
                    no_rotate = True
                elif item[0] == t_shape.one[0] and item[1] == t_shape.one[1] + one_step*2:
                    no_rotate = True
            elif t_shape.facing == "vertical_left":
                if item[0] == t_shape.two[0] - one_step and item[1] == t_shape.two[1] + one_step*2:
                    no_rotate = True
                elif item[0] == t_shape.two[0] - one_step*2 and item[1] == t_shape.two[1] + one_step*2:
                    no_rotate = True
            elif t_shape.facing == "horizontal_up":
                if item[0] == t_shape.one[0] and item[1] == t_shape.one[1] - one_step*3:
                    no_rotate = True
                elif item[0] == t_shape.one[0] and item[1] == t_shape.one[1] - one_step*2:
                    no_rotate = True

        # check for going out of bounds

        if t_shape.facing == "vertical_right":
            if t_shape.tail[0] > screen_size[0] - one_step:
                no_right = True
            elif t_shape.three[0] < one_step:
                no_left = True
        elif t_shape.facing == "vertical_left":
            if t_shape.tail[0] < one_step:
                no_left = True
            elif t_shape.three[0] > screen_size[0] - one_step:
                no_right = True
        elif t_shape.facing == "horizontal_down":
            if t_shape.one[0] > screen_size[0] - one_step:
                no_right = True
            elif t_shape.three[0] < one_step:
                no_left = True
        elif t_shape.facing == "horizontal_up":
            if t_shape.three[0] >= screen_size[0] - one_step:
                no_right = True
            elif t_shape.one[0] < one_step:
                no_left = True

        if no_down == False:
            if t_shape.facing == "horizontal_up" or t_shape.facing == "vertical_left":
                if t_shape.one[1] < screen_size[1] - t_shape.one[3]:
                    t_shape.one[1] += one_step
                    t_shape.two[1] += one_step
                    t_shape.three[1] += one_step
                    t_shape.tail[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(t_shape.one)
                    existing_pieces.append(t_shape.two)
                    existing_pieces.append(t_shape.three)
                    existing_pieces.append(t_shape.tail)

                    t_shape = get_new_t_shape()
            elif t_shape.facing == "horizontal_down":
                if t_shape.tail[1] < screen_size[1] - t_shape.tail[3]:
                    t_shape.one[1] += one_step
                    t_shape.two[1] += one_step
                    t_shape.three[1] += one_step
                    t_shape.tail[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(t_shape.one)
                    existing_pieces.append(t_shape.two)
                    existing_pieces.append(t_shape.three)
                    existing_pieces.append(t_shape.tail)

                    t_shape = get_new_t_shape()
            elif t_shape.facing == "vertical_right":
                if t_shape.three[1] < screen_size[1] - t_shape.three[3]:
                    t_shape.one[1] += one_step
                    t_shape.two[1] += one_step
                    t_shape.three[1] += one_step
                    t_shape.tail[1] += one_step
                else:
                    new_piece = generate_new_piece()
                    existing_pieces.append(t_shape.one)
                    existing_pieces.append(t_shape.two)
                    existing_pieces.append(t_shape.three)
                    existing_pieces.append(t_shape.tail)

                    t_shape = get_new_t_shape()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                print(no_right)
                print("T: ", t_shape.three[0])
                print(t_shape.facing)

                if event.key == pygame.K_LEFT and no_left == False :
                    t_shape.one[0] -= one_step
                    t_shape.two[0] -= one_step
                    t_shape.three[0] -= one_step
                    t_shape.tail[0] -= one_step

                if event.key == pygame.K_RIGHT and no_right == False:
                    t_shape.one[0] += one_step
                    t_shape.two[0] += one_step
                    t_shape.three[0] += one_step
                    t_shape.tail[0] += one_step

                if event.key == pygame.K_SPACE and t_shape.facing == "horizontal_up" and no_rotate == False:

                        t_shape.facing = "vertical_right"
                        t_shape.one[1] -= one_step
                        t_shape.two[0] -= one_step
                        t_shape.three[0] -= one_step*2
                        t_shape.three[1] += one_step
                        t_shape.tail[0] -= one_step
                        t_shape.tail[1] += one_step*2

                elif event.key == pygame.K_SPACE and t_shape.facing ==  "vertical_left" and t_shape.tail[0] > one_step and no_rotate == False:

                        t_shape.facing = "horizontal_up"
                        t_shape.one[0] -= one_step*2
                        t_shape.one[1] -= one_step
                        t_shape.two[0] -= one_step
                        t_shape.three[1] += one_step
                        t_shape.tail[0] += one_step

                elif event.key == pygame.K_SPACE and t_shape.facing == "horizontal_down" and no_rotate == False:

                        t_shape.facing = "vertical_left"
                        t_shape.one[1] += one_step*2
                        t_shape.two[0] += one_step
                        t_shape.two[1] += one_step
                        t_shape.three[0] += one_step*2
                        t_shape.tail[0] += one_step
                        t_shape.tail[1] -= one_step

                elif event.key == pygame.K_SPACE and t_shape.facing ==  "vertical_right" and t_shape.tail[0] < screen_size[0] - one_step and no_rotate == False:

                        t_shape.facing = "horizontal_down"
                        t_shape.one[0] += one_step*2
                        t_shape.two[0] += one_step
                        t_shape.two[1] -= one_step
                        t_shape.three[1] -= one_step*2
                        t_shape.tail[0] -= one_step
                        t_shape.tail[1] -= one_step



    for full_line in full_line_list:

        if sorted(intersection(full_line, existing_pieces)) == sorted(full_line):
            for item in full_line:
                existing_pieces.remove(item)
            for item in existing_pieces:
                if item[1] < full_line[0][1]:
                    item[1] += one_step






    redraw_game_window()

pygame.quit()
