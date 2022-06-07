import random as rd
import time

pick_hit_rate = 0.60

def two_pick():
    """Simulate a two-pick power play."""
    pick_one = rd.random() <= pick_hit_rate     # True or False if pick_one hits
    pick_two = rd.random() <= pick_hit_rate     # True or False if pick_two hits
    return (pick_one and pick_two)              # True if two-pick is successful

def simulate_challenge(units):
    """Simulate a ladder challenge.
    Return the number of units gained."""
    days_won = 0
    units_of_profit = -units
    for day in range(7):                        # 7 days in a challenge
        if two_pick():
            days_won += 1
            units_of_profit += 3*units          # win 3x on successful two-pick
            units *= 2                          # double units for next day
            units_of_profit -= units            # two-pick entry cost for next day
        else:
            break                               # end challenge if two-pick fails
    return days_won, units_of_profit

def aggregate_challenge_simulator(units, trials):
    """Simulate a ladder challenge for a given number of trials.
    Return the average number of successful days per challenge
    and the total units of profit."""
    total_units_of_profit = 0
    total_days_won = 0
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    with open('challenge_simulator_results_'+timestr+'.txt', 'w') as f:
        for trial in range(trials):
            days_won, units_of_profit = simulate_challenge(units)
            total_days_won += days_won
            total_units_of_profit += units_of_profit
            f.write('Challenge {}: {} days won, {} units of profit\n'.format(trial, days_won, units_of_profit))
    return total_days_won/trials, total_units_of_profit

print(aggregate_challenge_simulator(1, 100))
