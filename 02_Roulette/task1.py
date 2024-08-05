import random
import numpy as np

def check_color(number):
    if number == 0:
        return 'green'
    elif (number <= 10) or (number >= 19 and number <= 28):
        if number % 2 == 0:
            return 'black'
        else:
            return 'red'
    else:
        if number % 2 == 0:
            return 'red'
        else:
            return 'black'
    
def bet_number(bet, number):
    result = random.randint(0,36)
    if number == result:
        return 35 * bet
    else:
        return -bet
    
def evaluate_straight_bet(bet, number, n):
    results = []
    for i in range(n):
        result = bet_number(bet, number)
        results.append(result)
    return np.mean(results)

def bet_color(bet, color):
    result = random.randint(0, 36)
    resultColor = check_color(result)
    if color == resultColor:
        return bet
    else:
        return -bet

def evaluate_color_bet(bet, color, n):
    results = []
    for i in range(n):
        result = bet_color(bet, color)
        results.append(result)
    return np.mean(results)

avgProfit = evaluate_straight_bet(1, 10, 1000000)
print(f'Straight bet: {avgProfit}')

avgProfit = evaluate_color_bet(1, 'black', 100000)
print(f'Color bet: {avgProfit}')
