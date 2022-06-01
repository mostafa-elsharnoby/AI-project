from kenken import Kenken
from cage import Cage
from variable import Variable
from time import time
import GlobalVariables

# import game

size = GlobalVariables.board_size


def update_size():
    size = GlobalVariables.board_size
variables = []
cages = []
for i in range(size):
    for j in range(size):
        variables.append(Variable((i, j), size))

def send_board(grid_cages,sign_cages,num_cages,alg_type):
    print(grid_cages)
    size = GlobalVariables.board_size
    variables_back = []
    cages_back = []
    num_of_cages = 0
    for i in range(size):
        for j in range(size):
            num_of_cages = max(num_of_cages,grid_cages[i][j])
            variables_back.append(Variable((i, j), size))
    for i in range(1,num_of_cages+1):
        index_list = []
        min_x_index = 10
        min_y_index = 10
        flag = 1
        for r in range(size):
            for c in range(size):
                if grid_cages[r][c]==i:
                    if flag:
                        min_x_index = r
                        min_y_index = c
                        flag = 0
                    index_list.append(variables_back[r*size+c])
        print(
            index_list,
            sign_cages[min_x_index][min_y_index],
            num_cages[min_x_index][min_y_index]
        )
        logic_sign = None
        if len(index_list) >1:
            logic_sign = sign_cages[min_x_index][min_y_index]
        cages_back.append(
            Cage(
                index_list,
                logic_sign,
                num_cages[min_x_index][min_y_index]
            )
        )
    lol = cages_back
    kenken_back = Kenken(variables_back, cages_back)
    t1 = time()
    if alg_type==1:
        solution1_back = kenken_back.solve(solver=0)
    if alg_type == 2:
        solution1_back = kenken_back.solve(solver=1)
    if alg_type == 3:
        solution1_back = kenken_back.solve(solver=2)

    print(time() - t1)
    final_solution = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            final_solution[i][j]=solution1_back[i*size+j]
    return final_solution
    # kenken_back = Kenken(variables_back, cages_back)
    # t = time()
    # solution2_back = kenken_back.solve(solver=2)
    # print(time() - t)
    # print(solution2_back == solution1_back)
    # print(solution2_back)

cages = [
    Cage([
        variables[0],
        variables[1],
        variables[2]
    ], '*', 40),
    Cage([
        variables[3],
        variables[4],
        variables[8]
    ], '+', 9),
    Cage([
        variables[5],
        variables[10],
        variables[15]
    ], '+', 10),
    Cage([
        variables[6]
    ], None, 2),
    Cage([
        variables[7],
        variables[12]
    ], '-', 1),
    Cage([
        variables[9],
        variables[13],
        variables[14]
    ], '+', 10),
    Cage([
        variables[11],
        variables[16]
    ], '-', 2),
    Cage([
        variables[20],
        variables[21]
    ], '-', 2),
    Cage([
        variables[17],
        variables[22]
    ], '/', 2),
    Cage([
        variables[18],
        variables[19]
    ], '/', 2),
    Cage([
        variables[23],
        variables[24]
    ], '+', 5),
]

kenken = Kenken(variables, cages)
t1 = time()
solution1 = kenken.solve()

print(solution1)
print(time() - t1)

size = 5
variables = []
for i in range(size):
    for j in range(size):
        variables.append(Variable((i, j), size))

cages = [
    Cage([
        variables[0],
        variables[1],
        variables[2]
    ], '*', 40),
    Cage([
        variables[3],
        variables[4],
        variables[8]
    ], '+', 9),
    Cage([
        variables[5],
        variables[10],
        variables[15]
    ], '+', 10),
    Cage([
        variables[6]
    ], None, 2),
    Cage([
        variables[7],
        variables[12]
    ], '-', 1),
    Cage([
        variables[9],
        variables[13],
        variables[14]
    ], '+', 10),
    Cage([
        variables[11],
        variables[16]
    ], '-', 2),
    Cage([
        variables[20],
        variables[21]
    ], '-', 2),
    Cage([
        variables[17],
        variables[22]
    ], '/', 2),
    Cage([
        variables[18],
        variables[19]
    ], '/', 2),
    Cage([
        variables[23],
        variables[24]
    ], '+', 5),
]

kenken = Kenken(variables, cages)
t = time()
solution2 = kenken.solve(solver=2)
print(time() - t)
print(solution2 == solution1)
print(solution2)
