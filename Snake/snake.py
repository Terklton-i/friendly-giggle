import pygame
import random

# need to add so that the food block doesn't appear where the snake is

pygame.init()

screen_size = (500, 500)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake")

run = True

clock = pygame.time.Clock()


class Player(object):
    def __init__(self, x, y, width, height, facing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = width
        self.facing = facing
        self.snake_rect = None

    def draw(self, screen):
        self.snake_rect = pygame.draw.rect(screen, (250, 0, 0),
                                           (player.x, player.y, player.width, player.height))


class Food:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.food_rect = None

    def draw(self, screen):
        self.food_rect = pygame.draw.rect(screen, (250, 250, 0),
                                          (food.x, food.y, food.width, food.height))


class Tail:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tail_rect = None

    def draw(self, screen):
        pygame.draw.rect(screen, (250, 0, 0),
                         (self.x, self.y, self.width, self.height))


def redraw_game_window():
    screen.fill((0, 0, 0))
    player.draw(screen)
    food.draw(screen)

    for item in tail_list:
        item.draw(screen)

    pygame.display.update()


player = Player(0, 0, 20, 20, "r")
food = Food(random.choice(range(0, 480, 20)), random.choice(
    range(0, 480, 20)), 20, 20)

tail_list = []
time_speed = 5


while run:
    redraw_game_window()

    clock.tick(time_speed)

    index = len(tail_list) - 1
    while index > 0:
        tail_list[index].x = tail_list[index - 1].x
        tail_list[index].y = tail_list[index - 1].y
        index -= 1
    try:
        tail_list[0] = Tail(player.x, player.y, 20, 20)
    except IndexError:
        pass

    if player.facing == "r" and player.x <= screen_size[0] - player.speed - player.width:
        player.x += player.speed
    elif player.facing == "r" and player.x == screen_size[0] - player.width:
        player.x = 0

    if player.facing == "l" and player.x >= player.speed:
        player.x -= player.speed
    elif player.facing == "l" and player.x == 0:
        player.x = screen_size[0] - player.width

    if player.facing == "u" and player.y >= player.speed:
        player.y -= player.speed
    elif player.facing == "u" and player.y == 0:
        player.y = screen_size[1] - player.height

    if player.facing == "d" and player.y <= screen_size[1] - player.speed - player.height:
        player.y += player.speed
    elif player.facing == "d" and player.y == screen_size[1] - player.height:
        player.y = 0

    for item in tail_list:
        if item.x == player.x and item.y == player.y:
            run = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and player.facing != "r":
                player.facing = "l"

            if event.key == pygame.K_RIGHT and player.facing != "l":
                player.facing = "r"

            if event.key == pygame.K_UP and player.facing != "d":
                player.facing = "u"

            if event.key == pygame.K_DOWN and player.facing != "u":
                player.facing = "d"

    if player.y == food.y and player.x == food.x:
        food = Food(random.choice(range(0, 480, 20)), random.choice(
            range(0, 480, 20)), 20, 20)

        tail_list.append(Tail(player.x, player.y, 20, 20))
        time_speed += 2

    redraw_game_window()


pygame.quit()
