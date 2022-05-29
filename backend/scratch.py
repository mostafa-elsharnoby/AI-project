from kenken import Kenken
from cage import Cage
from variable import Variable
from time import time

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
t1 = time()
solution1 = kenken.solve()
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
print(time()-t)
print(solution2 == solution1)
print(solution2)
