import random
import os
import time

def clearConsole(): 
    command = 'clear' 
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def dead_state(height, width):
    state = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        state.append(row)
    return state

def random_state(height, width):
    state = dead_state(height, width)
    for i in range(width):
        for j in range(height):
            if random.random() >= 0.6:
                state[j][i] = 1
    return state

def render(state):
    border = "-" * (len(state[0]) + 2)
    print(border)
    for row in state:
        print("|", end="")
        for x in row:
            if x == 1:
                print("█", end="")
            else:
                print(" ", end="")
        print("|")
    print(border)

def next_cell_life(current_life, value):
    if current_life == 1:
        if value == 0 or value == 1:
            return 0
        elif value == 2 or value == 3:
            return 1
        else:
            return 0
    else:
        if value == 3:
            return 1
        else:
            return 0

def next_state(state):
    height = len(state)
    width = len(state[0])
    new_state = dead_state(height, width)

    for y in range(height):
        for x in range(width):
            if x == 0:
                if y == 0:
                    value = state[y][x+1] + state[y+1][x] + state[y+1][x+1]
                elif y == height - 1:
                    value = state[y-1][x] + state[y-1][x+1] + state[y][x+1]
                else:
                    value = state[y-1][x] + state[y-1][x+1] + state[y][x+1] + state[y+1][x+1] + state[y+1][x]
            elif x == width - 1:
                if y == 0:
                    value = state[y][x-1] + state[y+1][x-1] + state[y+1][x]
                elif y == height - 1:
                    value = state[y][x-1] + state[y-1][x-1] + state[y-1][x]
                else:
                    value = state[y-1][x] + state[y-1][x-1] + state[y][x-1] + state[y+1][x-1] + state[y+1][x]
            elif y == 0:
                value = state[y][x-1] + state[y+1][x-1] + state[y+1][x] + state[y+1][x+1] + state[y][x+1]
            elif y == height - 1:
                value = state[y][x-1] + state[y-1][x-1] + state[y-1][x] + state[y-1][x+1] + state[y][x+1]
            else:
                value = state[y-1][x-1] + state[y][x-1] + state[y+1][x-1] + state[y-1][x+1] + state[y][x+1] + state[y+1][x+1] + state[y-1][x] + state[y+1][x]

            new_state[y][x] = next_cell_life(state[y][x], value)

    return new_state

def load_board_state(filepath):
    state = []
    with open(filepath) as f:
        for line in f:
            row = []
            for x in line.strip():
                row.append(int(x))
            state.append(row)
    return state
            

#state = random_state(40,80)
#state = load_board_state("./presets/toad.txt")
state = load_board_state("./presets/gosper_glider_gun.txt")
#state = load_board_state("./presets/glider.txt")
#state = load_board_state("./presets/pulsar.txt")
render(state)
while 1:
    clearConsole()
    state = next_state(state)
    render(state)
    time.sleep(0.1)

