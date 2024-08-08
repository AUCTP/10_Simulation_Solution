import random

def print_intro():
    print('Welcome to the Racquetball simulator. This program will simulate the winning probabilities of 2 players.')
    
def get_inputs():
    print('Enter winning probabilities for a serve.')
    probA = float(input('Player A: '))
    probB = float(input('Player B: '))
    n = int(input('Number of games to simulate: '))
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

def sim_one_game(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = random.choice(['playerA', 'playerB'])
    while scoreA < 15 and scoreB < 15:
        if serving == 'playerA':
            if random.random() <= probA:
                scoreA += 1
            else:
                serving = 'playerB'
        else:
            if random.random() <= probB:
                scoreB += 1
            else:
                serving = 'playerA'
    return scoreA, scoreB

def print_summary(winsA, winsB):
    games = winsA + winsB
    shareA = winsA/games * 100
    shareB = winsB/games * 100
    print(30*'\033[1m-\033[0m')
    print('\033[1mSummary of the simulation\033[0m')
    print(f'Player A: {winsA} ({shareA:.2f}%)')
    print(f'Player B: {winsB} ({shareB:.2f}%)')
    print(30*'\033[1m-\033[0m')


# MAIN
print_intro()
probA, probB, n = get_inputs()
winsA, winsB = sim_n_games(probA, probB, n)
print_summary(winsA, winsB)
