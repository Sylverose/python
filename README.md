# python_u2

This project consists of 4 parts.

## Features
**Part 1: characterstat.py**
- Reads names from `data/Navneliste.txt`
- Sorts names by length and alphabetically
- Prints the number of characters and the frequency of each character
- Visualizes character frequency as a text-based bar chart
- (Optional) Visualization with matplotlib/seaborn and wordcloud
- Exports both the bar chart and word cloud to a PDF file (`data/names/character_stats.pdf`)

**Part 2: logsort.py**
- Sorts and extracts log file lines by type (error, warning, info, success)
- Saves each type to a separate file in `data/logsort/`
- Prints statistics in the log file

**Part 2.1: logsort_extended.py**
- More efficient way to sort the log, on the go, instead of checking for each log type in turn

**Part 3:**
- Checks for correct formatting of data (ID is an integer and in ascending order, e-mail, empty lines)
- Analyzes `data/source_data.csv` for empty lines and invalid IDs
- Logs empty lines to `data/csv_log/empty_lines.txt` and invalid IDs to `data/csv_log/id_errors.txt`
- Prints summary statistics for empty lines and invalid IDs

**Part 4:**
- Analyzes housing price data from `data/DKHousingPricesSample100k.csv`
- Groups and displays the first 10 entries for each region and house type
- Calculates and prints average purchase price per region
- Saves grouped and statistical data to output files
- Plots average purchase price per region using matplotlib
- Continues with a realistic use case for typical financial report export
- Exports property value statistics to pdf, followed by a donut graph of the bonds
- Adds the current date of the generated report
- I used a branded color palette for the charts - feel free to edit the color codes in the order that you would like displayed
- If there aren't enough colors listed, simply add more in the chart description
- There is a font applied to the printed report, which matches the selected brand.
- To change the font, replace the current font in python_u2/fonts, and remember to update the font path

## Requirements
- Python 3.x
- (Optional) `matplotlib`, `seaborn`, `wordcloud`

## Usage
Run the scripts with:
python src/input_project_name.py

For data output, see corresponding feature sections.

**Character statistics:**
```
python src/characterstat.py
```

**Log sorting:**
```
python src/logsort.py
```

**Extended log sorting:**
```
python src/logsort_extended.py
```

**Housing price analysis and plotting:**
```
python src/housing.py
```

**Error handling and data validation:**
```
python src/error_handling.py
```

## Extensions
To use graphical visualization, install:
```
pip install matplotlib seaborn wordcloud
```

## File structure
- `src/characterstat.py` – Main script for character statistics (del 1)
- `src/logsort.py` – Main script for log sorting (del 2)
- `src/logsort_extended.py` – Extended log sorting (del2ex.py)
- `src/housing.py` – Housing price analysis and plotting (del 4)
- `src/error_handling.py` – Checks for empty lines and invalid IDs in source data, logs results, prints summary statistics (del 3)
- `data/Navneliste.txt` – Name list data for character statistics
- `data/app_log (logfil analyse) - random.txt` – Log file for log sorting
- `data/DKHousingPricesSample100k.csv` – Housing price data
- `data/names/character_stats.pdf` – PDF export of bar chart and word cloud (created by Part 1)
- `data/source_data.csv` – Source data for error handling
- `data/csv_log/empty_lines.txt` – Output: lines in source_data.csv that are empty
- `data/csv_log/id_errors.txt` – Output: lines in source_data.csv with invalid IDs

## Author
Andy Sylvia Rosenvold

## Acknowledgements
[GitHub Copilot](https://github.com/features/copilot) integration with VS  (formatting help, syntax suggestions)
[W3Schools](https://www.w3schools.com/)  
[Stack Overflow](https://stackoverflow.com/)  
[Python.org](https://www.python.org/)  
[Pandas GitHub](https://github.com/pandas-dev/pandas)
