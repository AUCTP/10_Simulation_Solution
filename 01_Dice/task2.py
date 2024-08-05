import random
import numpy as np

def roll_dice(n):
    totalDice = 0
    points = []
    for i in range(n):
        totalDice += 1
        pointsRoll = random.randint(1,6)
        points.append(pointsRoll)
    avgPoints = np.mean(points)
    return totalDice, avgPoints


def test_seeds(n, seeds):
    points = []
    for seed in seeds:
        random.seed(seed)
        totalDice, avgPoints = roll_dice(n)
        points.append(avgPoints)
    return np.min(points), np.mean(points), np.max(points)

seeds = range(0, 50)

for n in [10, 100, 1000, 10000, 100000]:
    min, mean, max = test_seeds(n, seeds)
    print(f'n: {n} - Min: {min} Mean: {mean} Max: {max} Diff: {max-min}')