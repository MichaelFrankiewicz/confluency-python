# src/main.py

from .calculations import estimate_split_time
from .utils.cell_line_utils import find_doubling_time
from .utils.cellosaurus_parser import parse_cellosaurus_synonyms, match_cell_line

def main():
    cell_dict = parse_cellosaurus_synonyms()

    try:
        num_lines = int(input("How many cell lines do you want to enter? "))
        for i in range(num_lines):
            print(f"\n--- Cell line #{i+1} ---")
            user_input = input("Enter cell line name (e.g., HEK293): ")
            standardized_name = match_cell_line(user_input, cell_dict)
            if standardized_name is None:
                print(f"No confident match for '{user_input}'. Please verify or enter manually.")
                standardized_name = input("Enter standardized cell line name manually: ")
            else:
                print(f"✅ Matched to standardized name: {standardized_name}")

            doubling_time = find_doubling_time(standardized_name)
            if doubling_time is None:
                print("Doubling time not found automatically. Please enter manually.")
                doubling_time = float(input("Enter doubling time in hours: "))
            else:
                print(f"Doubling time found: {doubling_time} hours")

            start_density = float(input("Enter starting density (0–1): "))
            days_passed = float(input("How many days since plating? "))
            estimate_split_time(standardized_name, doubling_time, start_density, days_passed)
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
