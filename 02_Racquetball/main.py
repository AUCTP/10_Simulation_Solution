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

def sim_one_game(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = random.choice(['A', 'B'])
    while scoreA < 15 and scoreB < 15:
        if serving == 'A':
            if random.random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random.random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA, scoreB

def print_summary(winsA, winsB):
    games = winsA + winsB
    print(f'Simulated games: {games}')
    print(f'Wins Player A: {winsA} ({100 * winsA/games}%)')
    print(f'Wins Player B: {winsB} ({100 * winsB/games}%)')

# Main Program
print_intro()
probA, probB, n = get_inputs()
winsA, winsB = sim_n_games(probA, probB, n)
print_summary(winsA, winsB)