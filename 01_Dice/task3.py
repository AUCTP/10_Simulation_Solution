import random
import pandas as pd
import matplotlib.pyplot as plt

def play_game(capital):
    rounds = 0
    while capital > 0:
        player = random.randint(1,6)
        bank = random.randint(1,6)
        if player > bank:
            capital += 1
        else:
            capital -= 1
        rounds += 1
    return rounds

def play_games(capital, n, seeds):
    rounds = []
    for seed in seeds:
        random.seed(seed)
        for i in range(n):
            result = play_game(capital)
            rounds.append(result)
    return rounds

seeds = range(10)
rounds = play_games(100, 1000, seeds)

results = pd.DataFrame({'rounds': rounds})
results.plot(kind='hist', column='rounds')
plt.savefig('01_Dice/rounds.png')
        


