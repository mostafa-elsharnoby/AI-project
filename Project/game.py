import pygame
import math
import time 
import kenken_screen
import GlobalVariables
#global board_size


pygame.init()
class Screen():
    def __init__(self, screen_width, screen_height, title, fill=(255,255,255)):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = title
        self.fill = fill
        self.current = False
        
    def makeCurrent(self):
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        self.current = True

    def endCurrent(self):
        self.current = False

    def checkUpdate(self):
        return self.current

    def screenUpdate(self):
        if(self.current):
            self.screen.fill(self.fill)

    def returnTitle(self):
        return self.title

    # def fill():
    #     self.fill((255,255,255))


def draw_button(screen, screen_title, startX, startY, width, height, button_color):
    index = 0
    coordinates = []
    if screen_title == 'Start':
        for i in range (3):
            for j in range(3):
                if(i != 2):
                    pygame.draw.rect(screen, button_color, [(j)*200+startX, (i)*(100+height)+startY, width, height], border_radius=15)
                    coordinates.append(((j)*200+startX, (i)*(100+height)+startY))
                    screen.blit(text_list[index], ((j)*200+startX+18, (i)*(100+height)+startY+18))
                else:
                    pygame.draw.rect(screen, button_color, [(j+1)*200+startX, (i)*(100+height)+startY, width, height], border_radius=15)
                    coordinates.append(((j+1)*200+startX, (i)*(100+height)+startY))
                    screen.blit(text_list[-1], ((j+1)*200+startX+18, (i)*(100+height)+startY+18))
                    break
                index += 1
    elif screen_title == 'End':
        i = 0
        for j in range(3):
            pygame.draw.rect(screen, button_color, [(j) * 200 + startX, (i) * (100 + height) + startY, width, height], border_radius=15)
            coordinates.append(((j) * 200 + startX, (i) * (100 + height) + startY))
            time.sleep(3)
            screen.blit(alg_list[index], ((j) * 200 + startX + 18, (i) * (100 + height) + startY + 22))
            index += 1
    return coordinates
def draw_buttons_alg(screen ,startX, startY, width, height, button_color):
    index = 0
    coordinates = []
    i = 0
    for j in range(3):
        pygame.draw.rect(screen, button_color, [(j) * 200 + startX, (i) * (100 + height) + startY, width, height], border_radius=15)
        coordinates.append(((j) * 200 + startX, (i) * (100 + height) + startY))
        screen.blit(alg_list[index], ((j) * 200 + startX + 18, (i) * (100 + height) + startY + 22))
        index += 1
    return coordinates

def get_click(screen_title, width, height, coordinates):
    mouse = pygame.mouse.get_pos()
    button_num = None
    if screen_title == 'Start':
        for i in range(7):
                if (coordinates[i][0] <= mouse[0] <= coordinates[i][0]+width) and (coordinates[i][1] <= mouse[1] <= coordinates[i][1]+height):
                    button_num = i+1
                    return i+1
    elif screen_title == 'End':
        for i in range(3):
            if (coordinates[i][0] <= mouse[0] <= coordinates[i][0]+100) and (coordinates[i][1] <= mouse[1] <= coordinates[i][1]+66):
                button_num = i+1
                return i+1
    return 0

def navigate(button_number, page_number=0):
    page_number += 1


# Buttons
width = 100
height = 200//3
startX = 150
startY = 100 + height//2
spaceX = 100
spaceY = 100
button_color = (19,160,195)

# Clock
clock = pygame.time.Clock()

screen_width = 800
screen_height = 600
# screen = pygame.display.set_mode((screen_width,screen_height))
screen = Screen(screen_width, screen_height, "Start")
screen2 = Screen(screen_width, screen_height, "End")

screen.makeCurrent()

# Show text
font = pygame.font.Font('freesansbold.ttf', 35)
text1 = font.render('3x3', True, (255,255,255), button_color)
text2 = font.render('4x4', True, (255,255,255), button_color)
text3 = font.render('5x5', True, (255,255,255), button_color)
text4 = font.render('6x6', True, (255,255,255), button_color)
text5 = font.render('7x7', True, (255,255,255), button_color)
text6 = font.render('8x8', True, (255,255,255), button_color)
text7 = font.render('9x9', True, (255,255,255), button_color)

text_list = [
    text1,
    text2,
    text3,
    text4,
    text5,
    text6,
    text7
]

font2 = pygame.font.Font('freesansbold.ttf', 18)
alg1 = font2.render('BK', True, (255, 255, 255), button_color)
alg2 = font2.render('BK+FC', True, (255, 255, 255), button_color)
alg3 = font2.render('BT+ARC', True, (255, 255, 255), button_color)

alg_list = [
    alg1,
    alg2,
    alg3
]

index = 0

# Title and Icon
pygame.display.set_caption("Kenken Puzzle")
#icon = pygame.image.load("image path")
#pygame.display.set_icon(icon)

# Game Loop
running = True

def show_first_screen(running):
    while running :
        button_num = 0
        button_num2 = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_num = get_click(screen.returnTitle(), width, height, coordinates)
                print("Button ",button_num," is clicked")
            screen.screenUpdate()
            screen2.screenUpdate()
            if screen.checkUpdate():
                #### inside screen 1
                # screen.fill()
                coordinates = draw_button(screen.screen, screen.returnTitle(), startX, startY, width, height, button_color)
                mos_x, mos_y = pygame.mouse.get_pos()
                # button_num = get_click(screen.returnTitle(), width, height, coordinates)
                if button_num == 1:
                    GlobalVariables.board_size = 3
                    screen2.makeCurrent()
                    screen2.screenUpdate()
                    pygame.display.update()
                    screen.endCurrent()
                    print("The Button is : ",button_num)
                elif button_num == 2:
                    GlobalVariables.board_size = 4
                    screen2.makeCurrent()
                    screen2.screenUpdate()
                    pygame.display.update()
                    screen.endCurrent()
                    print("The Button is : ",button_num)
                elif button_num ==3:
                    GlobalVariables.board_size = 5
                    screen2.makeCurrent()
                    screen2.screenUpdate()
                    pygame.display.update()
                    screen.endCurrent()
                    print("The Button is : ",button_num)
                elif button_num==4 :
                    GlobalVariables.board_size = 6
                    screen2.makeCurrent()
                    screen2.screenUpdate()
                    pygame.display.update()
                    screen.endCurrent()
                    print("The Button is : ",button_num)
                elif button_num ==5:
                    GlobalVariables.board_size = 7
                    screen2.makeCurrent()
                    screen2.screenUpdate()
                    pygame.display.update()
                    screen.endCurrent()
                    print("The Button is : ",button_num)
                elif button_num ==6:
                    GlobalVariables.board_size = 8
                    screen2.makeCurrent()
                    screen2.screenUpdate()
                    pygame.display.update()
                    screen.endCurrent()
                    print("The Button is : ",button_num)
                elif button_num ==7:
                    GlobalVariables.board_size = 9
                    screen2.makeCurrent()
                    screen2.screenUpdate()
                    pygame.display.update()
                    screen.endCurrent()
                    print("The Button is : ",button_num)
                else:
                    print("No button")
            
            elif screen2.checkUpdate():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_num2 = get_click(screen.returnTitle(), width, height, coordinates)
                    print("Button ",button_num," is clicked")
                #### inside screen 2
                coordinates = draw_buttons_alg(screen2.screen,  startX, startY+100, width, height, button_color)
                mos_x, mos_y = pygame.mouse.get_pos()
                # button_num2 = get_click(screen2.returnTitle(), width, height, coordinates)
                print("Button of Screen2 = ",button_num2)
                if button_num2 == 1:
                    kenken_screen.show_kenken(False, GlobalVariables.board_size)
                    pygame.display.update()
                    screen2.endCurrent()
                    
                    #skenken_screen.done = False
                    print("a7a")
                    
                    # kenken_screen.scr
                    print("The Button is : ",button_num)
                elif button_num2 == 2:
                    kenken_screen.show_kenken(False, GlobalVariables.board_size)
                    pygame.display.update()
                    screen2.endCurrent()
                    
                    #skenken_screen.done = False
                    print("a7a2")
                    
                    # kenken_screen.scr
                    print("The Button is : ",button_num)
                elif button_num2 == 3:
                    kenken_screen.show_kenken(False, GlobalVariables.board_size)
                    pygame.display.update()
                    screen2.endCurrent()
                    #skenken_screen.done = False
                    print("a7a3")
                    
                    # kenken_screen.scr
                    print("The Button is : ",button_num)
                else:
                    print("No button")

        # Background Color
        pygame.display.update()
        clock.tick(30)
show_first_screen(True)