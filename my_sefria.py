import os
from enum import Enum

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Selection(Enum):
    highest_price = 1
    average_price  = 2
    count_ideal_diamonds = 3
    diamond_colors = 4
    median_carat_premium = 5
    average_carat_per_cut = 6
    average_price_per_color = 7
    EXIT = 8

def menu():
    for item in Selection:print(f'{item.value} - {item.name}')
    return   Selection(int( input("your selection: ")))