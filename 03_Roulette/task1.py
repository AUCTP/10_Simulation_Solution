import random
import numpy as np

def simulate_n_games(n, bet, strategy):
    outcomes = []
    for i in range(n):
        if strategy == 0:
            outcome = straight_bet_one_game(bet)
            outcomes.append(outcome)
        elif strategy == 1:
            outcome = color_bet_one_game(bet)
            outcomes.append(outcome)
        elif strategy == 2:
            outcome = martingale_one_game(bet, maxBet)
            outcomes.append(outcome)
    avgReturn = np.mean(outcomes)
    return avgReturn

def straight_bet_one_game(bet):
    player = random.randint(0,36)
    casino = random.randint(0,36)
    if player == casino:
        return 35 * bet
    else:
        return -bet

def color_bet_one_game(bet):
    player = random.choice(['red', 'black'])
    casinoNumber = random.randint(0,36)
    casino = get_color(casinoNumber)
    if player == casino:
        return bet
    else:
        return -bet
    
def get_color(number):
    if number == 0:
        return 'green'
    elif number <= 10 or (number >= 19 and number <= 28):
        if number % 2 == 0:
            return 'black'
        else:
            return 'red'
    else:
        if number % 2 == 0:
            return 'red'
        else:
            return 'black'


def martingale_one_game(bet, maxBet):
    profit = 0
    while bet <= maxBet:
        outcome = color_bet_one_game(bet)
        profit += outcome
        if outcome == bet:
            break
        else:
            bet *= 2
    return profit
    
n = 10000000
bet = 1
strategy = 2
maxBet = 10000
avgReturn = simulate_n_games(n, bet, strategy)
print(f'Avg. Return of betting {bet}€: {avgReturn}')