import re
import os

def find_doubling_time(cell_line_name, filepath=None):
    if filepath is None:
        # Default path relative to this module
        filepath = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'cellosaurus.txt')

    doubling_time = None
    current_entry = []
    found = False

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('ID   '):
                if found:
                    break
                current_entry = [line]
            elif line.startswith('//'):
                if found:
                    break
                current_entry = []
            else:
                current_entry.append(line)

            if cell_line_name in line:
                found = True

    if found:
        for entry_line in current_entry:
            if "Doubling time:" in entry_line:
                match = re.search(r'Doubling time:\s*([\d.]+)\s*(hour|hours|h|day|days)', entry_line, re.I)
                if match:
                    value, unit = match.groups()
                    value = float(value)
                    unit = unit.lower()
                    if unit in ["day", "days"]:
                        value *= 24
                    doubling_time = value  # numeric output
                break

    return doubling_time  # numeric or None if not found
