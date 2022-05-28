import pygame
import time
import math

# initialize the game
pygame.init()

def get_click_alg(coordinates):
    mouse = pygame.mouse.get_pos()
    button_num = None
    for i in range(3):
            if (coordinates[i][0] <= mouse[0] <= coordinates[i][0]+100) and (coordinates[i][1] <= mouse[1] <= coordinates[i][1]+66):
                button_num = i+1
                return i+1
    return 0


def draw_buttons_alg(startX, startY, width, height, button_color):
    index = 0
    coordinates = []
    i = 0
    for j in range(3):
        pygame.draw.rect(screen, button_color, [(j) * 200 + startX, (i) * (100 + height) + startY, width, height], border_radius=15)
        coordinates.append(((j) * 200 + startX, (i) * (100 + height) + startY))
        screen.blit(alg_list[index], ((j) * 200 + startX + 18, (i) * (100 + height) + startY + 22))
        index += 1
    return coordinates


# Buttons
width = 100
height = 200 // 3
startX = 150
startY = 100 + height // 2
spaceX = 100
spaceY = 100
button_color = (19, 160, 195)

# Clock
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Show text
font = pygame.font.Font('freesansbold.ttf', 18)
alg1 = font.render('BK', True, (255, 255, 255), button_color)
alg2 = font.render('BK+FC', True, (255, 255, 255), button_color)
alg3 = font.render('BT+ARC', True, (255, 255, 255), button_color)
alg_list = [
    alg1,
    alg2,
    alg3
]

# create a rectangular object for the
# text surface object
# textRect = text.get_rect()

# set the center of the rectangular object.
# textRect.center = (screen_width // 2, screen_height // 2)

# Title and Icon
pygame.display.set_caption("Kenken Puzzle")
# icon = pygame.image.load("image path")
# pygame.display.set_icon(icon)

# Game Loop
running = True
page_num = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_num = get_click_alg(coordinates_alg_buttons)
            print("Button ", button_num, " is clicked")


    # Background Color
    screen.fill((255, 255, 255))
    coordinates_alg_buttons = draw_buttons_alg(startX, startY+100, width, height, button_color)
    # print(coordinates)
    button_num = get_click_alg(coordinates_alg_buttons)
    # if(button_num):
    #     print("BUTTON NUM IS:", button_num)
    # mouse = pygame.mouse.get_pos()
    # if (150 <= mouse[0] <= 250) and (233 <= mouse[1] <= 299) :
    #     print("BUTTON NUM IS:", 1)

    mos_x, mos_y = pygame.mouse.get_pos()
    pygame.display.update()
    clock.tick(30)