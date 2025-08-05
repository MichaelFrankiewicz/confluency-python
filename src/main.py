from utils.cell_line_utils import find_doubling_time

def main():
    cell_line = input("Enter cell line: ")
    doubling_time = find_doubling_time(cell_line)

    if doubling_time:
        print(f"Doubling time for {cell_line}: {doubling_time} hours.")
        # Continue your calculations...
    else:
        print(f"Doubling time not found for {cell_line}.")
        # Prompt manual entry or handle gracefully.

if __name__ == "__main__":
    main()
