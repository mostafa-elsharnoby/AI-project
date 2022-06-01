import pygame
import random
import GlobalVariables
import scratch
from cage import Cage
from variable import Variable

#import scratch

Rows_Cols_Size = GlobalVariables.board_size

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
#****************************************
def show_numbers(values,Rows_Cols_Size):
    for row in range(Rows_Cols_Size):
        for column in range(Rows_Cols_Size):
            start_x = (MARGIN + WIDTH) * column + MARGIN
            start_y = (MARGIN + HEIGHT) * row + MARGIN
            font_num = pygame.font.Font('freesansbold.ttf', 25)
            txt = font_num.render(str(values[row][column]), True, black, white)
            scr.blit(txt, (start_x + 25, start_y + 25))

def make_cages(Row_Cols_Size,grid_values):
    grid_cage = [[0 for i in range(Row_Cols_Size)] for j in range(Row_Cols_Size)]
    sign_cage = [['' for i in range(Row_Cols_Size)] for j in range(Row_Cols_Size)]
    num_cage = [[0 for i in range(Row_Cols_Size)] for j in range(Row_Cols_Size)]
    signs = ['+','*','-','/']
    shapes = [
                [(1,1),(1,0)],
                [(1, 0),(1,-1)],
                [(1, 0)],
                [(0, 1)],
                [(-1, 0)],
                [(0, -1)],
                [(0,0)],
                [(0, 1),(0,2),(1,1)],
                [(1, 0),(2,0),(1,1)],
                [(1, 0), (2, 0), (-1, -1)],
                [(1, 0), (2, 0), (-1, -1),(1,1)],
                [(1, 0), (2, 0), (1, -1), (1, 1)],
                [(0,1),(0,2),(1,1),(1,2)]
    ]
    cnt = 0
    for r in range(Row_Cols_Size):
        for c in range(Row_Cols_Size):
            if not grid_cage[r][c]:
                count = 0
                cnt = cnt + 1
                flag = True
                while flag:
                    num = rand(len(shapes))
                    num = num - 1
                    if num == 6:
                        up = (-1+r,0+c)
                        down = (1+r, 0+c)
                        left = (0+r, -1+c)
                        right =(0+r, 1+c)
                        if 0 <= up[0] < Row_Cols_Size and 0 <= up[1] < Row_Cols_Size:
                            if not grid_cage[up[0]][up[1]]:
                                continue
                        if 0 <= down[0] < Row_Cols_Size and 0 <= down[1] < Row_Cols_Size:
                            if not grid_cage[down[0]][down[1]]:
                                continue
                        if 0 <= left[0] < Row_Cols_Size and 0 <= left[1] < Row_Cols_Size:
                            if not grid_cage[left[0]][left[1]]:
                                continue
                        if 0 <= right[0] < Row_Cols_Size and 0 <= right[1] < Row_Cols_Size:
                            if not grid_cage[right[0]][right[1]]:
                                continue

                    flag_in = 1
                    for tup in shapes[num]:
                        r_ind = r + tup[0]
                        c_ind = c + tup[1]
                        if not (r_ind >= 0 and r_ind < Row_Cols_Size and c_ind >=0 and c_ind<Row_Cols_Size):
                            flag_in = 0
                        elif grid_cage[r_ind][c_ind]:
                            flag_in=0
                    if flag_in:
                        flag = 0
                        grid_cage[r][c] = cnt
                        rand_sign_ind = 0
                        if len(shapes[num]) == 1:
                            rand_sign_ind = rand(len(signs)) - 1
                        else:
                            rand_sign_ind = rand(len(signs)-2) - 1
                        sign = signs[rand_sign_ind]
                        count += grid_values[r][c]
                        for tup in shapes[num]:
                            r_ind = r + tup[0]
                            c_ind = c + tup[1]
                            if sign is '+':
                                count += grid_values[r_ind][c_ind]
                            elif sign is '*':
                                count *= grid_values[r_ind][c_ind]
                            elif sign is '-':
                                count -= grid_values[r_ind][c_ind]
                                count = abs(count)
                            elif sign is '/' and( count % grid_values[r_ind][c_ind] ==0 or grid_values[r_ind][c_ind] % count ==0):
                                if count % grid_values[r_ind][c_ind] ==0:
                                    count = count / grid_values[r_ind][c_ind]
                                else:
                                    count = grid_values[r_ind][c_ind] / count
                                count = int(count)
                            else:
                                sign = '-'
                                count -= grid_values[r_ind][c_ind]
                                count = abs(count)
                            grid_cage[r_ind][c_ind] = cnt
                        num_cage[r][c] = count
                        if not (shapes[num][0][0]==0 and shapes[num][0][1]==0):
                            sign_cage[r][c] = sign
                        else:
                            num_cage[r][c]=grid_values[r][c]

    return grid_cage,sign_cage,num_cage

def draw_buttons_kenken(startX, startY, width, height, button_color):
    index = 0
    font = pygame.font.Font('freesansbold.ttf', 18)
    btn1 = font.render('Solve', True, (255, 255, 255), button_color)
    btn2 = font.render('Again', True, (255, 255, 255), button_color)
    kenken_button_list = [
        btn1,
        btn2
    ]
    coordinates = []
    j = 2
    for i in range(2):
        pygame.draw.rect(scr, button_color, [(j) * 200 + startX, (i) * (100 + height) + startY, width, height], border_radius=15)
        coordinates.append(((j) * 200 + startX, (i) * (100 + height) + startY))
        scr.blit(kenken_button_list[index], ((j) * 200 + startX + 18, (i) * (100 + height) + startY + 22))
        index += 1
    return coordinates

def get_click_alg(coordinates):
    mouse = pygame.mouse.get_pos()
    button_num = None
    for i in range(2):
            if (coordinates[i][0] <= mouse[0] <= coordinates[i][0]+100) and (coordinates[i][1] <= mouse[1] <= coordinates[i][1]+66):
                button_num = i+1
                return i+1
    return 0
#****************************************


# show_number = 0
pygame.init()   
window_size = [800, 600]
scr = pygame.display.set_mode(window_size)
pygame.display.set_caption("Grid")
done = False
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 15)

def generate_board_generator(board_size):
    size = board_size
    grid = draw_grid(Rows_Cols_Size)
    grid_values_back = generate_board(Rows_Cols_Size)
    grid_cages_back, sign_cages_back, num_cages_back = make_cages(size, grid_values_back)
    variables_back = []
    cages_back = []
    num_of_cages = 0
    for i in range(size):
        for j in range(size):
            num_of_cages = max(num_of_cages, grid_cages_back[i][j])
            variables_back.append(Variable((i, j), size))
    for i in range(1, num_of_cages + 1):
        index_list = []
        min_x_index = 10
        min_y_index = 10
        flag = 1
        for r in range(size):
            for c in range(size):
                if grid_cages_back[r][c] == i:
                    if flag:
                        min_x_index = r
                        min_y_index = c
                        flag = 0
                    index_list.append(variables_back[r * size + c])
        print(
            index_list,
            sign_cages_back[min_x_index][min_y_index],
            num_cages_back[min_x_index][min_y_index]
        )
        logic_sign = None
        if len(index_list) > 1:
            logic_sign = sign_cages_back[min_x_index][min_y_index]
        cages_back.append(
            Cage(
                index_list,
                logic_sign,
                num_cages_back[min_x_index][min_y_index]
            )
        )
    return cages_back, variables_back

# final_cages,final_var = generate_board_generator(5)

def show_kenken(done, board_size,algorithm_type):
    
    Rows_Cols_Size=board_size
    grid = draw_grid(Rows_Cols_Size)
    grid_values = generate_board(Rows_Cols_Size)
    grid_cages,sign_cages,num_cages = make_cages(Rows_Cols_Size,grid_values)
    

    show_number = 0
    while not done:
        show_screen_1 = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_num = get_click_alg(kenken_buttons_coordinates)
                print("Button ", button_num, " is clicked")
                if(button_num==1):
                    soln = scratch.send_board(grid_cages, sign_cages, num_cages, algorithm_type)
                    show_number = 1
                elif button_num == 2:
                    show_screen_1=1
                    import game
                    done = True
                    game.show_first_screen(True)
                    pygame.quit()
                    break

        if show_screen_1:
            break
        
        scr.fill((140,140,140))
        kenken_buttons_coordinates = draw_buttons_kenken(startX, startY, width, height, button_color)
        get_click_alg(kenken_buttons_coordinates)
        draw_border(Rows_Cols_Size, grid, grid_cages, sign_cages, num_cages)
        if(show_number):
            show_numbers(soln,Rows_Cols_Size)
        clock.tick(50)
        pygame.display.flip()   
# pygame.quit()
# import game