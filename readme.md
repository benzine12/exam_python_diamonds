# Diamond Analysis Script

This Python script performs various analyses on a diamond dataset stored in a CSV file. It provides insights into diamond characteristics such as cut, color, carat, and price.

## Dependencies

The script requires the following Python libraries:
- pandas
- my_sefria (custom library for UI elements)

To install the required dependencies, run:

```
pip install pandas
```

Note: The `my_sefria` library is a custom library and should be available in your Python environment.

## Usage

1. Ensure you have a CSV file named `diamonds.csv` in the same directory as the script.
2. Run the script:

```
python diamond_analysis.py
```

3. Use the menu to select different analysis options.

## Features

The script offers the following analysis options:

1. Display the highest price of all diamonds
2. Calculate the average price of all diamonds
3. Count the number of diamonds with an Ideal cut
4. List all diamond colors and their counts
5. Calculate the median carat for Premium cut diamonds
6. Display the average carat for each cut type
7. Show the average price for each color

## Functions

- `read_file()`: Reads the diamond data from 'diamonds.csv'.
- `count_Ideal_diamonds()`: Counts and displays the number of diamonds with an Ideal cut.
- `diamond_colors()`: Lists all diamond colors and their frequencies.
- `median_carat_premium()`: Calculates and displays the median carat for Premium cut diamonds.
- `average_carat_per_cut()`: Shows the average carat for each cut type.
- `average_price_per_color()`: Displays the average price for each diamond color.
- `main()`: Runs the main program loop with a menu for user interaction.

## Note

This script uses a custom menu system from the `my_sefria` module. Make sure this module is properly set up in your environment.

## Contributing

Feel free to fork this repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
