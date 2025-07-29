# Step 1: Define cell line doubling times
cell_lines = {
    "HEK293": 24,
    "HeLa": 20,
    "A549": 22,
    "MCF7": 30
}

def estimate_split_time(cell_line: str, start_density: float, days_passed: float):
    if cell_line not in cell_lines:
        print(f"Cell line '{cell_line}' not found in database.")
        return

    doubling_time = cell_lines[cell_line]
    hours_passed = days_passed * 24
    doublings = hours_passed / doubling_time
    estimated_density = start_density * (2 ** doublings)

    print(f"\n{cell_line} estimate:")
    print(f"Estimated current density: {min(estimated_density, 1.0):.2f} (1.0 = confluency)")

    if estimated_density >= 0.9:
        print("✅ You should split your cells.")
    elif estimated_density >= 0.7:
        print("⚠️  Cells are approaching confluency.")
    else:
        print("🕒 Still growing, no need to split yet.")

# Step 2: Get input for multiple cell lines
try:
    num_lines = int(input("How many cell lines do you want to enter? "))
    for i in range(num_lines):
        print(f"\n--- Cell line #{i+1} ---")
        cell_line = input("Enter cell line name (e.g., HEK293): ")
        start_density = float(input("Enter starting density as a decimal (e.g., 0.3 for 30%): "))
        days_passed = float(input("How many days since plating? "))
        estimate_split_time(cell_line, start_density, days_passed)
except ValueError:
    print("Invalid input. Please enter numerical values for counts, density, and days.")

