import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def play_one_session(capital, seed):
    rounds = 0
    random.seed(seed)
    while capital > 0:
        rounds += 1
        player = random.randint(1,6)
        bank = random.randint(1,6)
        if player > bank:
            capital += 1
        else:
            capital -= 1
    return rounds

n = 10000
capital = 100
results = []
for i in range(n):
    rounds = play_one_session(capital, i)
    results.append(rounds)

avg = np.mean(results)
min = np.min(results)
max = np.max(results)
print(f'Min: {min} Avg: {avg} Max: {max}')

df = pd.DataFrame({
    'rounds': results
})

df['rounds'].plot(kind='hist')
plt.savefig('01_Dice/rounds.png')
