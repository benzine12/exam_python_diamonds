import pandas as pd
from my_sefria import clearScreen,Selection,menu

# get the data from file where PATH is the path to the file
def read_file():
    PATH = 'diamonds.csv' 
    return pd.read_csv(PATH)

# print number of diamonds with udeal cut
def count_Ideal_diamonds():
    df = read_file()
    count_ideal = 0
    for cut_option in df['cut']:
        if cut_option == 'Ideal':
            count_ideal += 1
    print(f"number of diamonds with Ideal cut is :{count_ideal}")

#print all diamonds colors and how many
def diamond_colors():
    df = read_file()
    color_dict = {}
    for color in df['color']:
        color = color.strip().upper()
        if color not in color_dict:
            color_dict[color] = 1
        else:
            color_dict[color] += 1
    print(f'there is {len(color_dict)} colors ')
    for color, count in color_dict.items():
        print(f"color: {color}, how mach: {count}")

# print median of premium carat
def median_carat_premium():
    df = read_file()
    premium_carat_list = []
    for index, cut in enumerate(df['cut']):
        if cut == 'Premium':
            premium_carat_list.append(df['carat'][index])
    premium_carat_list.sort()
    n = len(premium_carat_list)
    if n % 2 == 1:
        median_carat = premium_carat_list[n // 2]
    else:
        median_carat = (premium_carat_list[n // 2 - 1] + premium_carat_list[n // 2]) / 2
    print(f'median premium diaminds carat is {median_carat}')

# print evarage carrat per every cut
def average_carat_per_cut():
    df = read_file()
    print(f"everage carat for every cut {df.groupby('cut')['carat'].mean()}")

#print average price per every color
def average_price_per_color():
    df = read_file()
    print(f"everage price for every color os {df.groupby('color')['price'].mean()}")

# main function with menu imported from my_sefria 
def main():
     df = read_file()
     while True:
        user_input = menu()
        if user_input == Selection.EXIT : exit()
        if user_input == Selection.highest_price: print(f"biggest value of all diamoind in price is : {df['price'].max()}")
        if user_input == Selection.average_price: print(f"average price of all diamonds is : {df['price'].mean()}")
        if user_input == Selection.count_ideal_diamonds: count_Ideal_diamonds()
        if user_input == Selection.diamond_colors: diamond_colors()
        if user_input == Selection.median_carat_premium: median_carat_premium()
        if user_input == Selection.average_carat_per_cut: average_carat_per_cut()
        if user_input == Selection.average_price_per_color: average_price_per_color()

# program start here but befire it clean the screen
if __name__ == '__main__':
    clearScreen()
    main()