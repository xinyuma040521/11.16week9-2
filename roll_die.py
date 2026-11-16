import random

def roll(low=1, high=6):
    num = random.randint(low, high)
    return num

print(f"Your die has returned the number {roll()}")