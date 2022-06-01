import time
import copy

from kenken_screen import generate_board_generator
from kenken import Kenken


def main():
    timings = [0, 0, 0]

    for _ in range(100):
        global_cages, global_variables = generate_board_generator(5)
        for i in range(3):
            variables = copy.deepcopy(global_variables)
            cages = copy.deepcopy(global_cages)
            kenken = Kenken(variables, cages)

            t = time.time()
            kenken.solve(solver=i)
            timings[i] += time.time() - t

    print(f"Timings for BT: {timings[0]} s")
    print(f"Timings for BT + FC: {timings[1]} s")
    print(f"Timings for BT + AC3: {timings[2]} s")


if __name__ == "__main__":
    main()
