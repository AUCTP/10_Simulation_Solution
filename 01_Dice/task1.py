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


totalDice, avgPoints = roll_dice(10)
print(f'Total dice: {totalDice}, Avg. Points: {avgPoints}')