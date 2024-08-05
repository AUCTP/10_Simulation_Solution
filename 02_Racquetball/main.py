import random

def print_intro():
    print('This program simulates a game called racquetball.')
    print('Two players (A and B) with different skill levels will compete and the program will analyze the winning probabilities for both players')


def get_inputs():
    print('Enter the chance of winning while serving')
    probA = float(input('Player A: '))
    probB = float(input('Player B: '))
    n = int(input('Number of simulation runs: '))
    return probA, probB, n

def sim_n_games(probA, probB, n):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = sim_one_game(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

print_intro()
probA, probB, n = get_inputs()
winsA, winsB = sim_n_games(probA, probB, n)