import pygame
import random


Rows_Cols_Size = 9


# Buttons
width = 100
height = 200 // 3
startX = 250
startY = 100 + height // 2
spaceX = 100
spaceY = 100
button_color = (19, 160, 195)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
WIDTH = 65
HEIGHT = 65
MARGIN = 1

def draw_grid(Rows_Cols_Size):
    grid = []
    for row in range(Rows_Cols_Size):
        grid.append([])
        for column in range(Rows_Cols_Size):
            grid[row].append(0)
    return grid

def draw_border(Rows_Cols_Size , grid , grid_cages , sign_cages , num_cages):
    for row in range(Rows_Cols_Size):
        for column in range(Rows_Cols_Size):
            color = white
            if grid[row][column] == 1:
                color = red
            pygame.draw.rect(scr,color,[(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN,WIDTH,HEIGHT])
            start_x = (MARGIN + WIDTH) * column + MARGIN
            start_y = (MARGIN + HEIGHT) * row + MARGIN
            end_x = (MARGIN + WIDTH) * column + MARGIN + WIDTH
            end_y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT
            if(row==0):
                pygame.draw.line(scr, (0, 0 , 0), (start_x, start_y), (end_x, start_y), 5) #up
            if(column==0):
                pygame.draw.line(scr, (0, 0 , 0), (start_x, start_y), (start_x, end_y), 5) #left
            if (row == Rows_Cols_Size-1):
                pygame.draw.line(scr, (0, 0, 0), (start_x, end_y), (end_x, end_y), 5)   #down
            if (column == Rows_Cols_Size-1):
                pygame.draw.line(scr, (0, 0 , 0), (end_x, start_y), (end_x, end_y), 5) #right
            if(row>0 and grid_cages[row][column]!=grid_cages[row-1][column]):
                pygame.draw.line(scr, (0, 0, 0), (start_x, start_y), (end_x, start_y), 5)  # up
            if (column > 0 and grid_cages[row][column] != grid_cages[row][column-1]):
                pygame.draw.line(scr, (0, 0, 0), (start_x, start_y), (start_x, end_y), 5)  # left
            if (row<Rows_Cols_Size-1 and grid_cages[row][column]!=grid_cages[row+1][column]):
                pygame.draw.line(scr, (0, 0, 0), (start_x, end_y), (end_x, end_y), 5)  # down
            if (column < Rows_Cols_Size - 1 and grid_cages[row][column] != grid_cages[row][column+1]):
                pygame.draw.line(scr, (0, 0, 0), (end_x, start_y), (end_x, end_y), 5)  # right
            if(num_cages[row][column]):
                txt = font.render(str(num_cages[row][column])+str(sign_cages[row][column]), True, black, white)
                scr.blit(txt, (start_x+5,start_y+5))
def rand(num):
    return random.randint(1, num)

def shift_right(arr):
    shifted_arr = [0]*len(arr)
    for i in range (len(arr)):
        shifted_arr[(i+1)%len(arr)]=arr[i]
    return shifted_arr

def generate_board(Row_Cols_Size):
    grid_values = [[0 for i in range(Row_Cols_Size)] for j in range(Row_Cols_Size)]
    dict_ = {}
    for c in range(Row_Cols_Size):
        num = rand(Row_Cols_Size)
        while num in dict_.keys():
            num = rand(Row_Cols_Size)
        dict_[num] = 1
        grid_values[0][c] = num
    arr = grid_values[0]
    dict_.clear()
    dict_[0] = 1
    for c in range(Row_Cols_Size-1):
        num = rand(Row_Cols_Size)
        while num-1 in dict_.keys():
            num = rand(Row_Cols_Size)
        grid_values[num-1] = shift_right(arr)
        arr = grid_values[num-1]
        dict_[num-1]=1
    return grid_values



pygame.init()
window_size = [800, 600]
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid")
done = False
clock = pygame.time.Clock()
grid = draw_grid(Rows_Cols_Size)
grid_values = generate_board(Rows_Cols_Size)
grid_cages,sign_cages,num_cages = make_cages(Rows_Cols_Size,grid_values)
font = pygame.font.Font('freesansbold.ttf', 15)

show_number = 0


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_num = get_click_alg(kenken_buttons_coordinates)
            print("Button ", button_num, " is clicked")
            if(button_num==1):
                show_number = 1

        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     pos = pygame.mouse.get_pos()
        #     column = pos[0] // (WIDTH + MARGIN)
        #     row = pos[1] // (HEIGHT + MARGIN)
        #     grid[row][column] = 1
    scr.fill((140,140,140))
    kenken_buttons_coordinates = draw_buttons_kenken(startX, startY, width, height, button_color)
    get_click_alg(kenken_buttons_coordinates)
    draw_border(Rows_Cols_Size, grid, grid_cages, sign_cages, num_cages)
    if(show_number):
        show_numbers(grid_values,Rows_Cols_Size)
    clock.tick(50)
    pygame.display.flip()
pygame.quit()